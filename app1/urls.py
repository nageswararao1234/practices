from django.conf.urls import url
from .import views


app_name = "app1"
urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^course/$', views.course, name="course"),
    url(r'^add_course/$', views.add_course, name="add_course"),
    url(r'^student_reg/$', views.student_reg, name="student_reg"),
    url(r'^staff_reg/$', views.staff_reg, name="staff_reg"),
    url(r'^course_list/$', views.course_list, name="course_list"),
    url(r'^(?P<course_id>[0-9]+)/student_list/$', views.student_list, name="student_list"),
    url(r'^staff_course/$', views.staff_course, name="staff_course"),
    url(r'^(?P<course_id>[0-9]+)/staff_list/$', views.staff_list, name="staff_list"),
    url(r'^(?P<student_id>[0-9]+)/student_details/$', views.student_details, name="student_details"),
    url(r'^(?P<staff_id>[0-9]+)/staff_details/$', views.staff_details, name="staff_details"),
    url(r'^(?P<student_id>[0-9]+)/student_update/$', views.student_update, name="student_update"),

    ]