from django.contrib import admin

from .models import Question

class RTQAAdmin(admin.ModelAdmin):  
  list_display = ('title', 'description', 'completed') 

# Register your models here.
admin.site.register(Question, RTQAAdmin) 