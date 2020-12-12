
from django.test import SimpleTestCase
from django.urls import reverse, resolve

from feedback.api.views import doctors_feedback

class TestUrls(SimpleTestCase) :

    def test_doctors_feedback_is_resolved(self):
        url = reverse('doctors_feedback',args=['some-slug'])
        print(resolve(url))
        self.assertEqual(resolve(url).func, doctors_feedback)