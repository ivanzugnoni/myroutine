from routines.models import Exercise, Routine
from .serializers import ExerciseSerializer, RoutineSerializer

from rest_framework import viewsets


class ExerciseViewSet(viewsets.ModelViewSet):

    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer


class RoutineViewSet(viewsets.ModelViewSet):

    queryset = Routine.objects.all()
    serializer_class = RoutineSerializer
