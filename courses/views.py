from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.views.generic import ListView
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Course, Lesson, Comment
from .forms import CommentForm

# Create your views here.


class LessonList(ListView):
    """
    Renders all the lessons published by admin
    **Context**
    ``queryset``
      All published instances of :model:class.Lesson
    ``paginate_by``
      Number of posts per page
    **Template**
    :templates:courses/online_courses.html
    """
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
    :template:courses/course_detail.html
    """

    queryset = Lesson.objects.filter(status=1)
    lesson = get_object_or_404(queryset, slug=slug)
    comments = lesson.comments.all().order_by("-created_on")
    comment_count = lesson.comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.commenter = request.user
            comment.course = lesson
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

    comment_form = CommentForm()

    return render(
        request,
        "courses/course_detail.html",
        {
            "lesson": lesson,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
            },
    )


def comment_edit(request, slug, comment_id):
    """
    Display an individual comment for edit.

    **Context**
    ``lesson``
        An instance of :model:`course.Lesson`.
    ``comment``
        A single comment related to the lesson.
    ``comment_form``
        An instance of :form:`course.CommentForm`
    """
    if request.method == "POST":

        queryset = Lesson.objects.filter(status=1)
        lesson = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.commenter == request.user:
            comment = comment_form.save(commit=False)
            comment.lesson = lesson
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(
                request,
                messages.ERROR,
                'Error updating comment!'
                )

    return HttpResponseRedirect(reverse('course_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    Display an individual comment for delete.

    **Context**
    ``lesson``
        An instance of :model:`course.Lesson`.
    ``comment``
        A single comment related to the lesson.
    ``comment_form``
        An instance of :form:`course.CommentForm`
    """
    queryset = Lesson.objects.filter(status=1)
    lesson = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.commenter == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(
            request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('course_detail', args=[slug]))
