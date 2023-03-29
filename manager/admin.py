from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from manager.models import Task, Position, Worker, TaskType


@admin.register(Worker)
class WorkerAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("position",)
    fieldsets = UserAdmin.fieldsets + (
        (("Additional info", {"fields": ("position",)}),)
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                        "position",
                    )
                },
            ),
        )
    )


@admin.register(Task)
class Task(admin.ModelAdmin):
    list_display = ["name", "task_type", "priority", "deadline", "is_completed", "description"]
    list_filter = ["task_type", "priority", "is_completed"]
    search_fields = ["task_type", "priority", "name"]


admin.site.register(Position)
admin.site.register(TaskType)
