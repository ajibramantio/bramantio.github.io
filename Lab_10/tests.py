from django.test import TestCase
from django.test import Client
from django.urls import resolve
from .views import subscribe
from .models import Subscriber
from django.db import IntegrityError


# Create your tests here.

class SubscribeUnitTest(TestCase):
    def test_url_page_is_exist(self):
        response = Client().get('/Lab_10/')
        self.assertEqual(response.status_code, 200)

    def test_using_index_function(self):
        found = resolve('/Lab_10/')
        self.assertEqual(found.func, subscribe)

    def test_model_can_create_object(self):
        Subscriber.objects.create(nama='aji', email="ajia@gmail.com", password="cekcek")
        counting_all_input = Subscriber.objects.all().count()
        self.assertEqual(counting_all_input, 1)

    def test_nama_max_length(self):
        nama = Subscriber.objects.create(
            nama="paling banyak 30 karakter cuy")
        self.assertLessEqual(len(str(nama)), 30)

    def test_unique_email(self):
        Subscriber.objects.create(email="ajia@email.com")
        with self.assertRaises(IntegrityError):
            Subscriber.objects.create(email="ajia@email.com")

    def test_check_email_view_get_return_200(self):
        email = "ajia@gmail.com"
        Client().post('/Lab_10/checkEmail', {'email': email})
        response = Client().post('/Lab_10/checkEmail', {'email': 'ajia@gmail.com'})
        self.assertEqual(response.status_code, 200)

    def test_check_email_already_exist_view_get_return_200(self):
        Subscriber.objects.create(nama="Aji",
                                     email="ajia@gmail.com",
                                     password="cekcek")
        response = Client().post('/Lab_10/checkEmail', {
            "email": "ajia@gmail.com"
        })
        self.assertEqual(response.json()['is_email'], True)

    def test_subscribe_should_return_status_subscribe_true(self):
        response = Client().post('/Lab_10/', {
            "email": "ajia@gmail.com",
            "nama": "Aji",
            "password":  "sikasik",
        })
        self.assertEqual(response.json()['status_subscribe'], True)

    def test_subscribe_should_return_status_subscribe_false(self):
        nama, email, password = "Aji", "ajia@gmail.com", "sikasik"
        Subscriber.objects.create(nama=nama, email=email, password=password)
        response = Client().post('/Lab_10/', {
            "email": email,
            "nama": nama,
            "password":  password,
        })
        self.assertEqual(response.json()['status_subscribe'], False)
