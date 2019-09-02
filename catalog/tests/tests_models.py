from django.test import TestCase

from catalog.models import User, Book
# Create your tests here.


class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(username='Username', first_name='Ihar', last_name='Nikanovich')

    def test_get_absolute_url(self):
        user = User.objects.get(id=1)
        self.assertEquals(user.get_absolute_url(), '/catalog/user/1')

class BookModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Book.objects.create(title='Alphabet', author='Best author', genre='science')

    def test_title_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

    def test_author_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('author').verbose_name
        self.assertEquals(field_label, 'author')

    def test_genre_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('genre').verbose_name
        self.assertEquals(field_label, 'genre')

    def test_title_max_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field('title').max_length
        self.assertEquals(max_length, 200)

    def test_author_max_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field('author').max_length
        self.assertEquals(max_length, 100)

    def test_genre_max_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field('genre').max_length
        self.assertEquals(max_length, 100)

    def test_object_name_is_title(self):
        book = Book.objects.get(id=1)
        object_name = book.title
        self.assertEquals(object_name, str(book.title))

    def test_get_absolute_url(self):
        book = Book.objects.get(id=1)
        self.assertEquals(book.get_absolute_url(), '/catalog/book/1')
