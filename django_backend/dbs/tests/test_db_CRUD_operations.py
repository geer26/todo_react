from django.test import TestCase
from ..models import CustomUser, Group
from datetime import datetime


class AddCustomUser(TestCase):

    def test_add_custom_user(self):
        time = datetime.now()
        u = CustomUser.objects.create_user(username= 'testuser', email= 'test@test.te', password= "testpassword")

        # Test for create model:
        self.assertTrue(isinstance(u, CustomUser))

        # Test for correct field contents:
        self.assertEqual(u.username, 'testuser')

        # Test for correct times:
        self.assertNotEqual(u.date_joined, time)


