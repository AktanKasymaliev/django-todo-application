from django.contrib import admin

from todo.models import MemberOfTeam, Task

class MemberInline(admin.StackedInline):
    model = MemberOfTeam
    

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    inlines = [MemberInline,]