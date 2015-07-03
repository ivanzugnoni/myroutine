from rest_framework import serializers

from routines.models import Exercise, Routine


class ExerciseSerializer(serializers.ModelSerializer):

    class Meta():
        model = Exercise
        fields = ('id', 'name', 'description', 'muscle_group')

