from __future__ import division, unicode_literals, absolute_import

from rest_framework import status
from rest_framework.test import APITestCase

from routines.models import Exercise, Routine


class TestExercise(APITestCase):

    def setUp(self):
        super(TestExercise, self).setUp()
        self.exer1 = Exercise.objects.create(
            id='a' * 16, name="Pecho plano", description="Some description",
            muscle_group="pecho")
        self.exer2 = Exercise.objects.create(
            id='b' * 16, name="Pecho inclinado",
            description="Some other description", muscle_group="pecho")

    def test_list(self):
        """Should return all paginated exercises"""
        response = self.client.get('/api/exercises/')
        expected = {
            'id': self.exer1.id,
            'name': self.exer1.name,
            'description': self.exer1.description,
            'muscle_group': self.exer1.muscle_group
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 2)
        self.assertEqual(len(response.data['results']), 2)
        self.assertEqual(response.data['results'][0], expected)

    def test_detail(self):
        """Should return exercise when given hash id is valid"""
        response = self.client.get('/api/exercises/{}/'.format(self.exer1.id))
        expected = {
            'id': self.exer1.id,
            'name': self.exer1.name,
            'description': self.exer1.description,
            'muscle_group': self.exer1.muscle_group
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected)


class TestRoutine(APITestCase):

    def setUp(self):
        super(TestRoutine, self).setUp()
        self.rout1 = Routine.objects.create(
            id='a' * 16, name="Monday routine")
        self.rout2 = Routine.objects.create(
            id='b' * 16, name="Tuesday routine")

    def test_list(self):
        """Should return all paginated routines"""
        response = self.client.get('/api/routines/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 2)
        self.assertEqual(len(response.data['results']), 2)
        self.assertEqual(response.data['results'][0]['id'], self.rout1.id)

    def test_detail(self):
        """Should return routine when given hash id is valid"""
        response = self.client.get('/api/routines/{}/'.format(self.rout1.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], self.rout1.id)
