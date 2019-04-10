from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, View
from .models import Course, Lesson


class CourseListView(ListView):
    model = Course


class CourseDetailView(DetailView):
    model = Course


class LessonDetailView(LoginRequiredMixin, View):

    def get(self, request, course_slug, lesson_slug, *args, **kwargs):
        course = get_object_or_404(Course, slug=course_slug)
        lesson = get_object_or_404(Lesson, slug=lesson_slug)
        context = {'object': lesson}
        return render(request, "sop/lesson_detail.html", context)