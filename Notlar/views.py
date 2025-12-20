from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Course, Note


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
            course = None
            if course_id:
                try:
                    course = Course.objects.get(id=course_id, user=user)
                except Course.DoesNotExist:
                    course = None
            Note.objects.create(user=user, course=course, title=title, content=content)
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
