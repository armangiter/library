from django.test import TestCase
from .models import Member


class MemberTest(TestCase):

    def setUp(self) -> None:
        self.member = Member.objects.create(username='member1', role='member', password='member12345')
        self.staff = Member.objects.create(username='staff1', role='staff', password='staff1234')

    def test_role(self):
        self.assertEqual(self.staff.is_staff, True, 'is staff is not True')
        self.assertEqual(self.member.is_staff, False, 'is staff is not False')
