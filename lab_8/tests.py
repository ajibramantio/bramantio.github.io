from django.test import TestCase
from django.test import Client
from django.urls import resolve
from django.http import HttpRequest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import unittest
import time

from .views import index
# Create your tests here.

response = {}
class Lab8UnitTest(TestCase):
    def test_url_is_exist(self):
        response = Client().get('/lab-8')
        self.assertEqual(response.status_code, 301)

    def test_using_status_form_template(self):
        response = Client().get('/lab-8/')
        self.assertTemplateUsed(response, 'home.html')
    
    def test_using_make_status_func(self):
        found = resolve('/lab-8/')
        self.assertEqual(found.func, index)

class Lab8FunctionalTest(unittest.TestCase):
        def setUp(self):
                chrome_options = Options()
                chrome_options.add_argument('--dns-prefetch-disable')
                chrome_options.add_argument('--no-sandbox')
                chrome_options.add_argument('--headless')
                chrome_options.add_argument('disable-gpu')
                service_log_path = "./chromedriver.log"
                service_args = ['--verbose']
                self.selenium = webdriver.Chrome(
                    './chromedriver', chrome_options=chrome_options
                )

                super(Lab8FunctionalTest, self).setUp()

        def tearDown(self):
                self.selenium.quit()
                super(Lab8FunctionalTest, self).tearDown()

        def test_content(self):
                selenium = self.selenium

                selenium.get('http://localhost:8000/lab-8/')
                selenium.implicitly_wait(10)

                self.content3 = selenium.find_elements_by_tag_name('h1')
                # content1 = selenium.find_element_by_xpath("//h1[@id='olla']")
                self.content2 = selenium.find_element_by_tag_name('body').value_of_css_property('background')
                self.content4 = selenium.find_element_by_xpath("//button[@id='gantiTema']").click()
               
                self.assertIn('Hello let me introduce my self...', selenium.page_source)
                self.assertIn('Bramantio Krisno Aji',selenium.page_source)
