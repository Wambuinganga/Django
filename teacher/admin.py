from django.contrib import admin
from .models import Teacher

class TeacherAdmin(admin.ModelAdmin):
	list_display=("first_name","last_name","registration_number","email")
	search_fields=("registration_number","email", "last_name")
	
admin.site.register(Teacher,TeacherAdmin)
