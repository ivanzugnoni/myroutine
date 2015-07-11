from django.contrib import admin

from .models import Exercise, Routine


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'muscle_group', 'description')
    search_fields = ('name', 'description', 'muscle_group')
    readonly_fields = ('id',)


@admin.register(Routine)
class RoutineAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    search_fields = ('name',)
    readonly_fields = ('id',)
