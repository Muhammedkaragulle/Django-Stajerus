import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'onlineogr.settings')
django.setup()

from django.contrib.auth import get_user_model
from django.test import Client
from Notlar.models import Course, Note

User = get_user_model()

username = 'testuser'
password = 'testpass123'

# create user if not exists
user, created = User.objects.get_or_create(username=username)
if created:
    user.set_password(password)
    user.save()
    print('Created user')
else:
    print('User exists')

c = Client()
# login
logged_in = c.login(username=username, password=password)
print('Logged in:', logged_in)

# create a course via POST
resp = c.post('/Notlar/', {'action': 'add_course', 'course_name': 'TestCourse'}, follow=True)
print('Add course status code:', resp.status_code)

course = Course.objects.filter(user=user, name='TestCourse').first()
print('Course created:', bool(course))

# add a note
resp2 = c.post('/Notlar/', {
    'action': 'add_note',
    'course_id': course.id if course else '',
    'note_title': 'Test Title',
    'note_content': 'This is the test content.'
}, follow=True)
print('Add note status code:', resp2.status_code)

# check note exists
note = Note.objects.filter(user=user, course=course, title='Test Title').first()
print('Note created:', bool(note))
if note:
    print('Note content:', note.content)

# fetch Notlar page
resp3 = c.get('/Notlar/')
print('GET /Notlar/ status:', resp3.status_code)
print('Page contains title?', 'Test Title' in resp3.content.decode('utf-8'))
print('Page contains content?', 'This is the test content.' in resp3.content.decode('utf-8'))
