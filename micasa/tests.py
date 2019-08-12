from django.test import TestCase
from .models import Hood, Profile, Business, Post
from django.contrib.auth.models import User

# Create your tests here.
class HoodTestClass(TestCase):
    def setUp(self):
        self.my_hood =Hood(name='wendani',location='kiambu',occupants=5)
        self.my_hood.save()

    def tearDown(self):
        Hood.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.my_hood,Hood))

    def test_save_hood(self):
        self.my_hood.save_hood()
        hood = Hood.objects.all()
        self.assertTrue(len(Hood)>0)