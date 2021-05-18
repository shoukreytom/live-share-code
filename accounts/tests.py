from django.test import TestCase

from .models import Account


class TestCases(TestCase):

    def setUp(self):
        for i in range(5):
            account = Account(email=f"testuser{i}@admin.com")
            account.set_password(f"test123{i}")
            account.save()
        
    def test_add_new_account(self):
        pre_count = Account.objects.count()
        account = Account(email="demouser@admin.com")
        account.set_password("demo123")
        account.save()
        post_count = Account.objects.count()
        self.assertEqual(pre_count+1, post_count)
    
    def test_delete_account(self):
        pre_count = Account.objects.count()
        Account.objects.get(id=1).delete()
        post_count = Account.objects.count()
        self.assertEqual(pre_count-1, post_count)

    def test_auto_add_username(self):
        account = Account(email="test@admin.com")
        account.set_password("test123")
        account.save()
        expected_username = str(account.email).split("@")[0]
        self.assertEqual(account.username, expected_username)
