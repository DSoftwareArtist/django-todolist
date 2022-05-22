from django.contrib import admin


# Register your models here.
from lists.models import Todo

class TodoAdmin(admin.ModelAdmin):
	list_display = ('creator','description','created_at','finished_at','is_finished', 'position')

admin.site.register(Todo, TodoAdmin)


# Register your models here.
from lists.models import TodoList

class TodolistAdmin(admin.ModelAdmin):
	list_display = ('creator','title','created_at','count','count_finished','count_open')

admin.site.register(TodoList, TodolistAdmin)