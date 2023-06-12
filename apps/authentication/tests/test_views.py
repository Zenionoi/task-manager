from django.test import TestCase
from django.urls import reverse


class ResponseForLoggingTest(TestCase):
    def test_login(self):
        res = self.client.get(reverse("login"))
        self.assertEqual(res.status_code, 200)

    def test_register(self):
        res = self.client.get(reverse("register"))
        self.assertEqual(res.status_code, 200)
