from django.test import TestCase
from django.urls import reverse

from catalog.models import User, Book
from catalog.forms import UserForm


class UserListViewTest(TestCase):

    def test_view_url_in_correct_location(self):
        response = self.client.get('/catalog/')
        self.assertEqual(response.status_code, 200)

    def test_view_available_by_name_and_uses_correct_template(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


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
        self.assertTemplateUsed(response, 'catalog/book_form.html')

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
