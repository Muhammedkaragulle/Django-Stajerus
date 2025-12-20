from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Course, Note, Comment
from django.http import JsonResponse, HttpResponseForbidden
from django.views.decorators.http import require_POST


@login_required
def home(request):
    user = request.user

    # Handle create course
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'add_course':
            name = request.POST.get('course_name', '').strip()
            if name:
                Course.objects.get_or_create(user=user, name=name)
            return redirect('Notlar:index')
        if action == 'add_note':
            course_id = request.POST.get('course_id')
            title = request.POST.get('note_title', '').strip()
            content = request.POST.get('note_content', '').strip()
            is_public = bool(request.POST.get('is_public'))
            course = None
            if course_id:
                try:
                    course = Course.objects.get(id=course_id, user=user)
                except Course.DoesNotExist:
                    course = None
            Note.objects.create(user=user, course=course, title=title, content=content, is_public=is_public)
            return redirect('Notlar:index')
        if action == 'clear_notes':
            course_id = request.POST.get('course_id')
            if course_id:
                Note.objects.filter(user=user, course_id=course_id).delete()
            return redirect('Notlar:index')

    courses = Course.objects.filter(user=user).order_by('-created')
    selected_course_id = request.GET.get('course')
    selected_course = None
    notes = []
    if selected_course_id:
        selected_course = get_object_or_404(Course, id=selected_course_id, user=user)
        notes = selected_course.notes.order_by('-created')
    elif courses.exists():
        selected_course = courses.first()
        notes = selected_course.notes.order_by('-created')

    return render(request, 'index.html', {
        'courses': courses,
        'selected_course': selected_course,
        'notes': notes,
    })


def public_courses(request):
    # list distinct course names that have at least one public note
    names = Course.objects.filter(notes__is_public=True).values_list('name', flat=True).distinct()
    return render(request, 'public_courses.html', {'course_names': names})


def public_course_detail(request, course_name):
    # show public notes across users for a given course name
    notes = Note.objects.filter(course__name=course_name, is_public=True).order_by('-created')
    return render(request, 'course_public_detail.html', {'course_name': course_name, 'notes': notes})


@login_required
@require_POST
def toggle_like(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    user = request.user
    if note.likes.filter(id=user.id).exists():
        note.likes.remove(user)
        liked = False
    else:
        note.likes.add(user)
        note.dislikes.remove(user)
        liked = True
    return JsonResponse({'liked': liked, 'likes_count': note.likes.count(), 'dislikes_count': note.dislikes.count()})


@login_required
@require_POST
def toggle_dislike(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    user = request.user
    if note.dislikes.filter(id=user.id).exists():
        note.dislikes.remove(user)
        disliked = False
    else:
        note.dislikes.add(user)
        note.likes.remove(user)
        disliked = True
    return JsonResponse({'disliked': disliked, 'likes_count': note.likes.count(), 'dislikes_count': note.dislikes.count()})


@login_required
@require_POST
def add_comment(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    content = request.POST.get('content', '').strip()
    if not content:
        return JsonResponse({'error': 'empty'}, status=400)
    comment = Comment.objects.create(user=request.user, note=note, content=content)
    return JsonResponse({'id': comment.id, 'user': comment.user.username, 'content': comment.content, 'created': comment.created.isoformat()})
