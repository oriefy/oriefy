from django.db import models
from memberships.models import Membership
from django.urls import reverse


# Create your models here.
class Course(models.Model):
    """
    Course Model
    """
    slug = models.SlugField()
    title = models.CharField('Title', max_length=120)
    description = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('courses:detail', kwargs={'slug': self.slug})
    
    @property
    def lessons(self):
        return self.lesson_set.all().order_by('position')



class Lesson(models.Model):
    slug = models.SlugField()
    title = models.CharField('Title', max_length=120)
    description = models.TextField('Description')
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    video_url = models.CharField(max_length=200)
    thumbnail = models.ImageField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('courses:lesson-detail', 
        kwargs={
            'course_slug': self.course.slug,
            'lesson_slug' : self.slug,
            })