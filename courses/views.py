from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Course, Module, Enrollment, Feedback, Payment

def course_list(request):
    courses = Course.objects.all()
    return render(
        request,
        "courses/course_list.html",
        {"courses": courses}
    )

@login_required
def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    modules = Module.objects.filter(course=course)
    feedbacks = Feedback.objects.filter(course=course)

    return render(
        request,
        "courses/course_detail.html",
        {
            "course": course,
            "modules": modules,
            "feedbacks": feedbacks
        }
    )

@login_required
def enroll(request, course_id):
    course = Course.objects.get(id=course_id)

    Enrollment.objects.get_or_create(
        user=request.user,
        course=course
    )

    return render(request, "courses/enroll_success.html", {
        "course": course
    })

@login_required
def make_payment(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    Payment.objects.get_or_create(
        user=request.user,
        course=course,
        defaults={
            "amount": course.price,  
            "status": "PAID"
        }
    )

    return render(request, "courses/payment_success.html", {
        "course": course
    })

@login_required
def dashboard(request):
    enrollments = Enrollment.objects.filter(user=request.user)
    payments = Payment.objects.filter(user=request.user)

    return render(
        request,
        "courses/dashboard.html",
        {
            "enrollments": enrollments,
            "payments": payments
        }
    )

@login_required
def feedback(request, course_id):
    course = Course.objects.get(id=course_id)

    if request.method == "POST":
        rating = request.POST.get("rating")
        comment = request.POST.get("comment")

        Feedback.objects.create(
            course=course,
            user=request.user,
            rating=rating,
            comment=comment
        )

        return redirect("course_list")  

    return render(request, "courses/feedback.html", {
        "course": course
    })