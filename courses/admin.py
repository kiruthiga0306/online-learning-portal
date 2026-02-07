from django.contrib import admin
from .models import Course, Module, Enrollment, Feedback, Payment

admin.site.register(Course)
admin.site.register(Module)
admin.site.register(Enrollment)
admin.site.register(Feedback)
admin.site.register(Payment)