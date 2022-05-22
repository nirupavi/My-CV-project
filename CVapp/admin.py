from django.contrib import admin
from .models import Resume

# Register your models here.
@admin.register(Resume)

class ResumeAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','mobile','locality','city','pin','state','School','School_marks',
                    'Degree','University','Degree_percentage','previous_roll','previous_experience',
                    'Tech_skill','profile_image','file']