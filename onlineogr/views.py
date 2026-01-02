from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from Notlar.models import Course, Note

def home(request):
    public_courses = Course.objects.filter(notes__is_public=True).values_list('name', flat=True).distinct().order_by('name')
    return render(request, 'anasayfa.html', {'public_courses': public_courses})


def search_public_courses(request):
    query = request.GET.get('q', '').strip()
    if len(query) < 1:
        return JsonResponse({'results': []})
    public_courses = Course.objects.filter(notes__is_public=True, name__icontains=query).values_list('name', flat=True).distinct().order_by('name')
    results = [{'name': name, 'url': f'/Notlar/public/{name}/'} for name in public_courses[:10]]
    return JsonResponse({'results': results})


def ulas(request):
    return render(request, 'bizeulasin.html')

def hakkimiz(request):
    return render(request, 'hakkimizda.html')
