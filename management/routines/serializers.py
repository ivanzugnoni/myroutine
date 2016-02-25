from rest_framework import serializers

from routines.models import Exercise, Routine


class ExerciseSerializer(serializers.ModelSerializer):

    class Meta():
        model = Exercise
        fields = ('id', 'name', 'description', 'muscle_group')


class BaseRoutineSerializer(serializers.ModelSerializer):

    class Meta():
        model = Routine
        fields = ('id', 'name', 'exercises')


class FullRoutineSerializer(BaseRoutineSerializer):

    exercises = ExerciseSerializer(many=True)
