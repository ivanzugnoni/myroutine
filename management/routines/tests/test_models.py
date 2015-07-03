from django.test import TestCase
from routines.models import Exercise, Routine


class TestExercise(TestCase):

    def setUp(self):
        pass

    def test_create_exercise(self):
        """Should create an Exercise object when given data is valid"""
        e = Exercise.objects.create(
            name="Pecho plano", description="Some description",
            muscle_group="pecho",
        )
        self.assertEqual(Exercise.objects.count(), 1)
        self.assertEqual(len(e.id), 16)
        self.assertEqual(e.name, "Pecho plano")
        self.assertEqual(e.description, "Some description")
        self.assertEqual(e.muscle_group, "pecho")


class TestRoutine(TestCase):

    def setUp(self):
        pass

    def test_create_exercise(self):
        """Should create a Routine object when given data is valid"""
        r = Routine.objects.create(
            name="Rutina de prueba",
        )
        self.assertEqual(Routine.objects.count(), 1)
        self.assertEqual(len(r.id), 16)
        self.assertEqual(r.name, "Rutina de prueba")

