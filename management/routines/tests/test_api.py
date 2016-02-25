from __future__ import division, unicode_literals, absolute_import

import json

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
        response = self.client.get('/exercises/')
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
        response = self.client.get('/exercises/{}/'.format(self.exer1.id))
        expected = {
            'id': self.exer1.id,
            'name': self.exer1.name,
            'description': self.exer1.description,
            'muscle_group': self.exer1.muscle_group
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected)


class TestExerciseCreate(APITestCase):

    def setUp(self):
        pass

    def test_create(self):
        """Should create exercise when POSTed payload is valid"""
        self.assertEqual(Exercise.objects.count(), 0)
        payload = {
            'name': 'Pecho plano',
            'description': 'Some description',
            'muscle_group': 'pecho'
        }
        self.client.post('/exercises/', data=payload)
        self.assertEqual(Exercise.objects.count(), 1)

    def test_create_empty_payload(self):
        """Should return 400 bad request when given payload is empty"""
        response = self.client.post('/exercises/', data={})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class TestExerciseUpdate(APITestCase):

    def setUp(self):
        super(TestExerciseUpdate, self).setUp()
        self.exer1 = Exercise.objects.create(
            id='a' * 16, name="Pecho plano", description="Some description",
            muscle_group="pecho")

    def test_update(self):
        """Should update exercise data when PUTing with valid payload"""
        payload = {
            'name': 'Pecho inclinado',
            'description': "New description",
            'muscle_group': "pecho"
        }
        response = self.client.put(
                '/exercises/{}/'.format(self.exer1.id), data=payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            Exercise.objects.get(id=self.exer1.id).name, payload['name'])

    def test_update_incomplete_payload(self):
        """Should return 400 bad request when PUTing when incomplete payload"""
        payload = {'name': 'Pecho inclinado'}
        response = self.client.put(
                '/exercises/{}/'.format(self.exer1.id), data=payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        content = {
            'muscle_group': ['This field is required.'],
        }
        self.assertEqual(json.loads(response.content), content)


class TestRoutine(APITestCase):

    def setUp(self):
        super(TestRoutine, self).setUp()
        self.rout1 = Routine.objects.create(
            id='a' * 16, name="Monday routine")
        self.rout2 = Routine.objects.create(
            id='b' * 16, name="Tuesday routine")

    def test_list(self):
        """Should return all paginated routines"""
        response = self.client.get('/routines/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 2)
        self.assertEqual(len(response.data['results']), 2)
        self.assertEqual(response.data['results'][0]['id'], self.rout1.id)

    def test_detail(self):
        """Should return routine when given hash id is valid"""
        response = self.client.get('/routines/{}/'.format(self.rout1.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], self.rout1.id)


class TestRoutineCreate(APITestCase):

    def setUp(self):
        self.exer1 = Exercise.objects.create(
            name="Pecho plano", description="Some description",
            muscle_group='pecho'
        )
        self.exercises = []
        self.exercises.append(self.exer1)

    def test_create(self):
        """Should create routine when POSTed payload is valid"""
        self.assertEqual(Routine.objects.count(), 0)
        payload = {
            'name': 'Monday routine',
        }
        self.client.post('/routines/', data=payload)
        self.assertEqual(Routine.objects.count(), 1)

    def test_create_empty_payload(self):
        """Should return 400 bad request when given payload is empty"""
        response = self.client.post('/routines/', data={})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class TestRoutineUpdate(APITestCase):

    def setUp(self):
        super(TestRoutineUpdate, self).setUp()
        self.exer1 = Exercise.objects.create(
            name="Pecho plano", description="Some description",
            muscle_group='pecho'
        )
        self.rout1 = Routine.objects.create(
            id='a' * 16, name="Monday routine")
        self.rout1.exercises.add(self.exer1)

    def test_update(self):
        """Should update routine data when PUTing with valid payload"""
        payload = {
            'id': self.rout1.id,
            'name': 'Tuesday routine',
            'exercises': [self.exer1.id]
        }
        response = self.client.put(
                '/routines/{}/'.format(self.rout1.id), data=payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            Routine.objects.get(id=self.rout1.id).name, payload['name'])
