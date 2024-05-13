from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from .models import Course, Lesson


# Create your views here.

class LessonList(ListView):
    queryset = Lesson.objects.filter(status=1)
    template_name = 'courses/online_courses.html'
    context_object_name = 'lessons'
    paginate_by = 6

def course_detail(request, slug):
    """
    Display an individual :model:`course.Lesson`.

    **Context**

    ``Lesson``
        An instance of :model:`course.Lesson`.

    **Template:**

    :template:`courses/course_detail.html`
    """

    queryset = Lesson.objects.filter(status=1)
    lesson = get_object_or_404(queryset, slug=slug)


    return render(
        request,
        "courses/course_detail.html",
        {
            "lesson": lesson,
            
            },
    )