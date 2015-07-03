from routines.models import Exercise, Routine
from .serializers import ExerciseSerializer, RoutineSerializer

from rest_framework import viewsets


class ExerciseViewSet(viewsets.ModelViewSet):

    """
    This endpoint represents Exercises.

    ## Allowed actions:

    *   List all exercises:

        `GET /exercises`

    *   Retrieve one particular exercise:

        `GET /exercises/:id`
    """

    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer


class RoutineViewSet(viewsets.ModelViewSet):

    """
    This endpoint represents Routines.

    ## Allowed actions:

    *   List all routines:

        `GET /routines`

    *   Retrieve one particular routine:

        `GET /routines/:id`
    """

    queryset = Routine.objects.all()
    serializer_class = RoutineSerializer
