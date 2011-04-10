"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase
from jobslist.models import *

class CompanyTest(TestCase):
    def setUp(self):
        self.yahoo = Company.objects.create (name="yahoo",
                desc = "The decsending company", 
                url = "yahoo.com")
        self.google = Company.objects.create (name="google",
                desc = "The Evil company who claims don't do evil",
                url = "google.com")

    def testName(self):
        self.assertEqual(self.yahoo.name, "yahoo")
        self.assertEqual(self.google.name, "google")

__test__ = {"doctest": """
Another way to test that 1 + 1 is equal to 2.

>>> 1 + 1 == 2
True
"""}

