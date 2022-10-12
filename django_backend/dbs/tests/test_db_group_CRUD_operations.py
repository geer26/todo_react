from django.test import TestCase
from ..models import CustomUser
from datetime import datetime


# Create test cases here!
class AddCustomUser(TestCase):

    def test_add_custom_user(self):

        time = datetime.now()
        u = CustomUser.objects.create_user(username= 'testuser', email= 'test@test.te', password= "testpassword")

        # Test on instantiating model:
        self.assertTrue(isinstance(u, CustomUser))

        # Test for correct field contents:
        self.assertEqual(u.username, 'testuser')

        # Test for correct times:
        self.assertNotEqual(u.date_joined, time)

        # Test for DB create operations
        self.assertEqual(len(CustomUser.objects.all()), 1)
        u2 = CustomUser.objects.create_user(username='testuser2', email='test@test.te', password="testpassword")
        self.assertEqual(len(CustomUser.objects.all()), 2)

        # Test for create illegal user instances
        with self.assertRaises(TypeError):
            u_illegal = CustomUser.objects.create_user()

        with self.assertRaises(ValueError):
            u_illegal = CustomUser.objects.create_user(username='')


class ReadCustomUser(TestCase):
    def setUp(self):
        u1 = CustomUser.objects.create_user(username='testuser1', email='test@test.te', password="testpassword1")
        u2 = CustomUser.objects.create_user(username='testuser2', email='test@test.te', password="testpassword2")

    def test_read_customuser_table(self):

        # Test case on queryng all enries
        self.assertEqual(len(CustomUser.objects.all()), 2)

        # Test case quering first entry
        self.assertEqual(CustomUser.objects.get(pk=1).username, 'testuser1')

        # Test case quering non-existing entry
        with self.assertRaises(CustomUser.DoesNotExist):
            should_not_exist = CustomUser.objects.get(pk=5)

        # Test QuerySet access
        allnames = []
        for userobject in CustomUser.objects.all():
            allnames.append(userobject.username)
        self.assertEqual(allnames, ['testuser1', 'testuser2'])


class UpdateCustomUser(TestCase):
    def setUp(self):
        u1 = CustomUser.objects.create_user(username='testuser1', email='test@test.te', password="testpassword1")
        u2 = CustomUser.objects.create_user(username='testuser2', email='test@test.te', password="testpassword2")

    def test_update_customuser_table(self):

        # Test for update username
        u_to_update = CustomUser.objects.get(pk=1)
        u_to_update.username = 'updateduser'
        u_to_update.save()
        self.assertEqual(CustomUser.objects.get(pk=1).username, 'updateduser')

        # Test for update password
        u_to_update = CustomUser.objects.get(pk=1)
        self.assertEqual(u_to_update.check_password('updated_password'), False)
        u_to_update.set_password('updated_password')
        u_to_update.save()
        self.assertEqual(u_to_update.check_password('updated_password'), True)


class DeleteCustomUser(TestCase):

    def setUp(self):
        u1 = CustomUser.objects.create_user(username='testuser1', email='test@test.te', password="testpassword1")
        u2 = CustomUser.objects.create_user(username='testuser2', email='test@test.te', password="testpassword2")

    def test_delete_customuser(self):

        self.assertEqual(len(CustomUser.objects.all()), 2)
        CustomUser.objects.get(pk=1).delete()
        self.assertEqual(len(CustomUser.objects.all()), 1)
        self.assertEqual(CustomUser.objects.get(pk=2).username, 'testuser2')
        with self.assertRaises(CustomUser.DoesNotExist):
            should_not_exist = CustomUser.objects.get(pk=1)