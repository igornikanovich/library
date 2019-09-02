from django.test import TestCase
from django.urls import reverse

from catalog.models import User, Book
from catalog.forms import UserForm


class UserListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_users = 20
        for user_id in range(number_of_users):
            User.objects.create(username='Username {0}'.format(user_id))

    def test_view_url_in_correct_location(self):
        response = self.client.get('/catalog/')
        self.assertEqual(response.status_code, 200)

    def test_view_available_by_name_and_uses_correct_template(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_pagination_is_fifteen(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] is True)
        self.assertTrue(len(response.context['user_list']) == 15)

    def test_lists_all_users(self):
        response = self.client.get(reverse('index') + '?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] is True)
        self.assertTrue(len(response.context['user_list']) == 5)


class UserDetailViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='Username')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_view_available_by_name_and_uses_correct_template(self):
        response = self.client.get(reverse('user-detail', kwargs={'pk': self.user.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/user_detail.html')


class BookUpdateViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='Username')
        self.book = Book.objects.create(title='testBook', user=self.user,
                                        author='testAuthor', genre='testGenre')
        self.user.save()
        self.book.save()

    def tearDown(self):
        self.user.delete()
        self.book.delete()

    def test_view_available_by_name_and_uses_correct_template(self):
        response = self.client.get(reverse('book-detail', kwargs={'pk': self.book.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/book_detail.html')

    def test_redirects_to_user_detail_view_on_success(self):
        response = self.client.post(reverse('book-detail', kwargs={'pk': self.book.pk}),
                                    {'title': 'testBookUpd', 'author': 'testAuthorUpd', 'genre': 'testGenreUpd'})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/catalog/user/'))


class BookCreateViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='Username')
        self.book = Book.objects.create(title='testBook', user=self.user,
                                        author='testAuthor', genre='testGenre')
        self.user.save()
        self.book.save()

    def tearDown(self):
        self.user.delete()
        self.book.delete()

    def test_view_available_by_name_and_uses_correct_template(self):
        response = self.client.get(reverse('book-create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/book_form.html')

    def test_redirects_to_user_detail_view_on_success(self):
        response = self.client.post(reverse('book-detail', kwargs={'pk': self.book.pk}),
                                    {'title': 'testBook1', 'user': self.user,
                                     'author': 'testAuthor', 'genre': 'testGenre'})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/catalog/user/'))


class UserCreateViewTest(TestCase):

    def test_view_available_by_name_and_uses_correct_template(self):
        response = self.client.get(reverse('user-create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/user_form.html')

    def test_redirects_to_user_detail_on_success(self):
        response = self.client.post(reverse('user-create'),
                                    {'username': 'Username', 'first_name': 'testname', 'last_name': 'testlname'})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/catalog/user/'))
