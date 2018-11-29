from django.test import TestCase
from django.test import Client
from django.urls import resolve
from django.http import HttpRequest
from .views import indexlab11, index, booklist
import unittest
import time

# Create your tests here.
class Lab11_Test(TestCase):
    def test_lab_11_url_is_exist(self):
        response = Client().get('/lab11/')
        self.assertEqual(response.status_code, 200)

    def test_lab_11_booklist_is_exist(self):
        response = Client().get('/lab11/book-list/')
        self.assertEqual(response.status_code, 200)

    def test_json_data_url_exists(self):
        response = Client().get('/lab11/book-list/json/')
        self.assertEqual(response.status_code, 200)

    def test_lab11_using_signin_template(self):
        response = Client().get('/lab11/')
        self.assertTemplateUsed(response, 'signin.html')

    def test_lab11_using_indexlab11_func(self):
        found = resolve('/lab11/')
        self.assertEqual(found.func, indexlab11)

    def test_lab11_using_index_func(self):
        found = resolve('/lab11/book-list/')
        self.assertEqual(found.func, index)

    def test_lab11_using_booklist_func(self):
        found = resolve('/lab11/book-list/json/')
        self.assertEqual(found.func, booklist)