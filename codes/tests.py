from django.test import TestCase
from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile

from .models import File, Shared
from accounts.models import Account


class TestCases(TestCase):

    def setUp(self):
        self.user = Account(email="testuser@admin.com")
        self.user.set_password("test123")
        self.user.save()
        for i in range(4):
            file = File(owner=self.user,
                 file=SimpleUploadedFile(f'testfile{i}.txt',
                     b'this is test file'
                 )
            )
            file.save()
            Shared(file=file, code=f"{i}").save()

    def test_add_new_file(self):
        pre_count = File.objects.count()
        new_file = File(owner=self.user)
        new_file.file = SimpleUploadedFile('testfile.txt',
            b'this is just a test file, do not care about it.'
        )
        new_file.save()
        post_count = File.objects.count()
        self.assertEqual(pre_count+1, post_count)
    
    def test_auto_add_file_name_slug(self):
        file = File.objects.get(id=1)
        self.assertNotEqual("", file.name)
        self.assertNotEqual("", file.slug)
        self.assertIsNotNone(file.name)
        self.assertIsNotNone(file.slug)

    def test_delete_file(self):
        pre_count = File.objects.count()
        File.objects.get(id=1).delete()
        post_count = File.objects.count()
        self.assertEqual(pre_count-1, post_count)
    
    def test_add_shared(self):
        pre_count = Shared.objects.count()
        new_file = File(owner=self.user)
        new_file.file = SimpleUploadedFile(
            'testfile.txt',
            b'this is just a test file, do not care about it.'
        )
        new_file.save()
        Shared(file=new_file, code="1234").save()
        post_count = Shared.objects.count()
        self.assertEqual(pre_count+1, post_count)
    
    def test_delete_shared(self):
        pre_count = Shared.objects.count()
        Shared.objects.get(id=1).delete()
        post_count = Shared.objects.count()
        self.assertEqual(pre_count-1, post_count)

