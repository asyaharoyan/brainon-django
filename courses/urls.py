from django.urls import path
from . import views

urlpatterns = [
    path('', views.LessonList.as_view(), name='courses'),
    path('<slug:slug>/', views.course_detail, name='course_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
]
