from django.contrib import admin
from .models import userlogin,user_details,staff_details,feedback,feedback_response,gasrefill_booking

# Register your models here.
admin.site.register(userlogin)
admin.site.register(user_details)
admin.site.register(staff_details)
admin.site.register(gasrefill_booking)
admin.site.register(feedback)
admin.site.register(feedback_response)
