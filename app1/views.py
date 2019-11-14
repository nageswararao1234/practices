# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import Course, Student, Staff
from django .http import HttpResponseRedirect
from django.shortcuts import reverse
from django.http import HttpResponse
from django.shortcuts import render,  get_object_or_404


def home(request):
    """

    :param request: request form the user to create home page
    :return:if created page will goes to home.html and display
    """

    return render(request, "app1/home.html", {})


def course(request):
    """

    :param request: request form the user to create course id
    :return:if id is created page will goes to course.html and display
    """
    course_list = Course.objects.order_by('id')
    return render(request, "app1/course.html", {"course_list": course_list})


def add_course(request):
    """
    :param request:request from the user to create
    :return:if form is valid page will  redirected to course,
    in case form is not valid  page will goes to add_course html and display
    """
    if request.method == 'POST':
        Course.objects.create(name=request.POST['name'],
                              course_duration=request.POST['course_duration'],
                              time=request.POST['time'],
                              fee=request.POST['fee'])

        return HttpResponseRedirect(reverse("app1:course"))
    return render(request, "app1/add_course.html", {})


def student_reg(request):

    """

    :param request:request from the user to create
    :return:if form is valid page will  response to sucess,
    in case form is not valid  page will goes to student_reg html and display
    """
    if request.method == 'POST':
        print request.POST["team"]
        # if request method is post then get the course id
        cr = Course.objects.get(pk=request.POST['team'])

        st = Student.objects.create(name=request.POST['name'],
                                    email=request.POST['email'],
                                    qualification=request.POST['qualification'],
                                    mobile=request.POST['mobile'],
                                    batch=request.POST['batch'],
                                    status=request.POST['status']
                                    )
        # if create the student id then get student.id
        st1 = Student.objects.get(pk=st.id)
        # course should be include in the student
        st1.course.add(cr)
        st1.save()
        return HttpResponse("sucess")

    else:
        course = Course.objects.all()
        return render(request, "app1/student_reg.html", {"course": course})


def staff_reg(request):

    """

    :param request:request from the user to create
    :return:if form is valid page will  response to sucess,
    in case form is not valid  page will goes to staff_reg html and display
    """
    if request.method == 'POST':
        print request.POST["team"]
        # if request method is post then get the course id
        cr = Course.objects.get(pk=request.POST['team'])
        stf = Staff.objects.create(name=request.POST['name'],
                                   exp=request.POST['exp'],
                                   salary=request.POST['salary'])
        # if create the staff id then get staff.id
        st2 = Staff.objects.get(pk=stf.id)
        # course should be include in the staff
        st2.course.add(cr)
        st2.save()
        return HttpResponse("sucess")

    else:
        course=Course.objects.all()
        return render(request, "app1/staff_reg.html", {"course": course})


def course_list(request):
    """

    :param request:
    :return:
    """
    student = Student.objects.all()
    l = []
    for s in student:
        for j in s.course.all():
            l.append(j)

    l = set(l)
    return render(request, 'app1/course_list.html', {'courselist': l})


def student_list(request, course_id):
    """

    :param request:
    :param course_id:
    :return:
    """
    # import pdb
    # pdb.set_trace()
    c = Course.objects.get(pk=course_id)
    student_list = c.student_set.all()

    staff_list = c.staff_set.all()
    students = c.student_set.all()
    return render(request, "app1/student_display.html", {"student_list": student_list, "staff_list": staff_list,"students": students})


def staff_course(request):
    """

    :param request:
    :return:
    """
    staff = Staff.objects.all()
    a = []
    for t in staff:
        for k in t.course.all():
            a.append(k)

    a = set(a)
    return render(request, 'app1/staff_course.html', {'staffcourse': a})


def staff_list(request, course_id):
    """

    :param request:request from the to get the course.id
    :param course_id:if the staff_id get
    :return: get the course id and display the staff name in the course staff
    """
    cf = Course.objects.get(pk=course_id)
    staff_list = cf.staff_set.all()
    return render(request, "app1/staff_display.html", {"staff_list": staff_list})


def student_details(request, student_id):
    """

    :param request:request from the user to detail student
    :param student_id:if the student_id created
    :return:if student.id is created then display the all student details page will be goes to the
    student_details.html
    """

    student = Student.objects.get(id=student_id)
    return render(request, "app1/student_details.html", {"student": student})


def staff_details(request, staff_id):
    """

    :param request:request from the user to detail staff
    :param staff_id:if the staff_id created
    :return:if staff details will display the page will be goes to
    the staff_details.html
    """
    staff = Staff.objects.get(id=staff_id)
    return render(request, "app1/staff_details.html", {"staff": staff})


def student_update(request, student_id):
    """

    :param request:request from the user to update
    :param student_id: update student status
    :return: if update is valid page will be redirect to student_details.html,
     in case  not valid  page will goes to update. html and display

    """
    if request.method == "POST":
        # you need to filter student id and update the status in student
        Student.objects.filter(pk=student_id).update(status=request.POST['status'])
        # student = Student.objects.get(pk=student_id)
        # student.status=request.POST['status']
        # student.save()
        return HttpResponseRedirect(reverse('app1:student_details', args=student_id))
    return render(request, "app1/update.html", {})

