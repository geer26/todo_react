from django.test import TestCase
from ..models import CustomUser, Group


class UsermodelTestCase(TestCase):
    def setUp(self):
        #Animal.objects.create(name="lion", sound="roar")
        #Animal.objects.create(name="cat", sound="meow")
        pass

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        #lion = Animal.objects.get(name="lion")
        #cat = Animal.objects.get(name="cat")
        #self.assertEqual(lion.speak(), 'The lion says "roar"')
        #self.assertEqual(cat.speak(), 'The cat says "meow"')
        print('Hello from test!')
        pass


class GroupmodelTestCase(TestCase):
    def setUp(self):
        #Animal.objects.create(name="lion", sound="roar")
        #Animal.objects.create(name="cat", sound="meow")
        pass

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        #lion = Animal.objects.get(name="lion")
        #cat = Animal.objects.get(name="cat")
        #self.assertEqual(lion.speak(), 'The lion says "roar"')
        #self.assertEqual(cat.speak(), 'The cat says "meow"')
        pass