from django.test import TestCase
from django.urls import reverse
from .models import JobApplication, Positions
from .forms import JobApplicationForm


class JobApplicationTests(TestCase):
    def setUp(self):
        self.position = Positions.objects.create(name='Position 1', salary=1000)


    def test_job_application_form_invalid_data(self):
        form_data = {
            'name': '',
            'email': 'invalid_email',
            'cover_letter': 'Cover letter text',
        }
        form = JobApplicationForm(data=form_data)
        self.assertFalse(form.is_valid())


    def test_job_application_create_invalid_form(self):
        form_data = {
            'name': '',
            'email': 'invalid_email',
            'cover_letter': 'Cover letter text',
        }
        response = self.client.post(reverse('job_application', args=(self.position.id,)), data=form_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(JobApplication.objects.count(), 0)