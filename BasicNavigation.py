#!usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 21 Feb 2020

@author: Tolgahan Bardakcı
@author-email: tolgahanbardakci@hotmail.com
"""

__version__ = "0.4"
__author__ = "Tolgahan Bardakcı"
__url__ = "https://github.com/2tolgahan2/BasicNavigation/blob/master/BasicNavigation.py"


import unittest
from selenium import webdriver
import validators
from selenium.webdriver.chrome.options import Options

# Setting up the Test Environment
class BaseTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
        chrome_options.add_experimental_option('prefs', {'intl.accept_languages': 'en_UK'})
        chrome_options.add_argument('--headless')
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.implicitly_wait(5)
        # Navigate to the application home page
        cls.driver.get("https://www.python.org/")
        
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


# Test 1
class NavigateTo(BaseTestCase):
    def test_Navigate(self):
        # Check Navigation: "Start with Our Beginner's Guide"
        self.navigate_link = self.driver.find_element_by_link_text('Start with our Beginner’s Guide')
        self.navigate_link.click()

        # URL Validation
        try:
            self.url = "https://www.python.org/about/gettingstarted/"
            self.validate = validators.url(self.url)
        except:
            assert False, "URL Validation is failed. Please check the url!"
            
        # Case:
        self.control = self.driver.title
        try:
            self.assertEqual(self.control, "Python For Beginners | Python.org")
        except AssertionError:
            assert False, "Navigate To: 'Start with our Beginner's Guide Page = Failed\n \t\tLook for: test_Navigate() "


# Test 2
class CheckField(BaseTestCase):
    def test_CheckField(self):
        # Check field for hedaer "Python For Beginners"
        self.driver.get("https://www.python.org/about/gettingstarted/")
        self.header = self.driver.find_element_by_xpath('//*[@id="content"]/div/section/article/header/h1')
        self.control = self.header.text

        try:
            self.assertEqual(self.control, "Python For Beginners")
        except AssertionError:
            assert False, "Check Field & Data Type: Heading: 'Python for Beginners' = Failed\n \t\tLook for: test_CheckField() "


# Test 3
#class CheckValidation(BaseTestCase):
    #def test_CheckValidation(self):
    #   ...


if __name__ == '__main__':
    unittest.main()
