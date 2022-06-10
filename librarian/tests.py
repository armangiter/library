from django.test import TestCase
from accounts.models import Member
from .models import Barrow, Book, Author, Publisher


class BarrowSystemTest(TestCase):

    def setUp(self) -> None:
        self.author = Author.objects.create()
        self.member1 = Member.objects.create(username='member1', role='member', password='member12334')
        self.publisher = Publisher.objects.create()
        self.book_1 = Book.objects.create(name='book1', isbn='isbn1', author=self.author, publisher=self.publisher,
                                          inventory=5)
        self.book_2 = Book.objects.create(name='book2', isbn='isbn2', author=self.author, publisher=self.publisher,
                                          inventory=2)
        self.book_3 = Book.objects.create(name='book3', isbn='isbn3', author=self.author, publisher=self.publisher,
                                          inventory=1)
        self.book_4 = Book.objects.create(name='book4', isbn='isbn4', author=self.author, publisher=self.publisher,
                                          inventory=0)

    def test_book_inventory_method(self):
        book4 = self.book_4.subtract_inventory()
        book3 = self.book_3.subtract_inventory()
        book1 = self.book_1.subtract_inventory(amount=6)
        self.book_2.add_inventory()
        self.assertEqual(book1, False, 'method subtract_inventory in book model is not working correctly')
        self.assertEqual(self.book_2.inventory, 3, 'method add_inventory in book model is not working correctly')
        self.assertEqual(book3, True, 'method subtract_inventory in book model is not working correctly')
        self.assertEqual(book4, False, 'method subtract_inventory in book model is not working correctly')

    def test_barrow_system(self):
        barrow1 = Barrow.objects.create(book=self.book_4, member=self.member1)
        barrow2 = Barrow.objects.create(book=self.book_3, member=self.member1)
        barrow3 = Barrow.objects.create(book=self.book_3, member=self.member1)
        self.assertEqual(barrow1.return_date, None, 'barrow save method not working correctly')
        self.assertIsInstance(barrow2, Barrow, 'barrow save method is working correctly')
        self.assertEqual(barrow3.return_date, None, 'barrow save method is not working correctly')
