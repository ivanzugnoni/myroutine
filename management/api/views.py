from routines.models import Exercise, Routine
from .serializers import ExerciseSerializer, BaseRoutineSerializer, FullRoutineSerializer

from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response


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
    serializer_class = BaseRoutineSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = FullRoutineSerializer(instance)
        return Response(serializer.data)
