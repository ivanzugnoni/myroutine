from routines.models import Exercise, Routine
from .serializers import (ExerciseSerializer, BaseRoutineSerializer,
                          FullRoutineSerializer)

from rest_framework import viewsets, mixins
from rest_framework.response import Response


class ExerciseViewSet(mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.CreateModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):

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


class RoutineViewSet(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):

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
