from django.test import TestCase
from django.test import Client
from .views import index, addStatus, DeleteStatus, profile
from .models import Statuy
from django.urls import resolve

# Create your tests here.
class Lab6Test(TestCase):
	def test_request_lab6(self):
		response = Client().get('/lab-6/status/')
		self.assertEqual(response.status_code,200)
	
	# def test_template_lab6(self):
	# 	response = Client().get('/lab-6/status')
	# 	self.assertTemplateUsed(response, 'status.html')

	def test_func_lab6(self):
		found = resolve('/lab-6/status/')
		self.assertEqual(found.func, index)

	def test_model_can_create_new_status(self):
		new_status = Statuy.objects.create(isi_status = 'Bikin Kopi')
		counting_status = Statuy.objects.all().count()
		self.assertEqual(counting_status, 1)

	def test_profile_url_is_exist(self):
		response = Client().get('/lab-6/')
		self.assertEqual(response.status_code, 200)

	# def test_template_profile(self):
	# 	response = Client().get('/lab-6')	
	# 	self.assertTemplateUsed(response, 'profile.html')

	def test_func_profile(self):
		found = resolve('/lab-6/')
		self.assertEqual(found.func, profile)
