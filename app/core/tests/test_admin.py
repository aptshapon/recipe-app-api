# from django.test import TestCase, Client
# from django.contrib.auth import get_user_model
# from django.urls import reverse


# class AdminSiteTests(TestCase):

#     def setUp(self):
#         self.client = Client()
#         self.admin_user = get_user_model().objects.create_superuser(
#             email='shsheikhbd@gmail.com',
#             password='django'
#         )
#         self.client.force_login(self.admin_user)
#         self.user = get_user_model().objects.create_user(
#             email='test@mail.com',
#             password='django'
#             name='Test user full name'
#         )

#     def test_user_listed(self):
#         """Test that users are listed on user page"""
#         url = reverse('admin:core_user_changelist')
#         res = self.client.get(url)

#         self.assertContains(res, self.user.name)
#         self.assertContains(res, self.user.email)

#     def test_user_change_page(self):
#         """Test that the user edit page works"""
#         url = reverse('admin:core_user_change', args=[self.user.id])
#         res = self.client.get(url)

#         self.assertEqual(rest.status_code, 200)


