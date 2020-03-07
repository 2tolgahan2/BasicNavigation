#!usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 21 Feb 2020

@author: Tolgahan Bardakcı
@author-email: bardakcitolgahan@gmail.com
"""

__version__ = "0.3"
__author__ = "Tolgahan Bardakcı"
__url__ = "https://github.com/2tolgahan2/BasicNavigation/blob/master/BasicNavigation.py"


import unittest
from selenium import webdriver
import validators

# Case: 1
class NavigateTo(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
        chrome_options.add_experimental_option('prefs', {'intl.accept_languages': 'en_UK'})
        inst.driver = webdriver.Chrome(options=chrome_options)
        inst.driver.implicitly_wait(20)
        inst.driver.maximize_window()
        # Navigate to the application home page
        inst.driver.get("https://www.python.org/")
        

    def test_Navigate(self):
        # Check Navigation: "Start with Our Beginner's Guide"
        self.navigate_link = self.driver.find_element_by_link_text('Start with our Beginner’s Guide')
        self.navigate_link.click()

        # URL Validation
        try:
            self.url = "https://www.python.org/about/gettingstarted/"
            self.validate = validators.url(self.url)
            return self.validate.public
        except:
            assert False, "URL Validation is failed. Please check the url!"
            
        # Case:
        self.control = self.driver.title
        try:
            self.assertEqual(self.control, "Python For Beginners | Python.org")
        except AssertionError:
            assert False, "Navigate To: 'Start with our Beginner's Guide Page = Failed\n \t\tLook for: test_Navigate() "
        
    @classmethod
    def tearDownClass(inst):
        inst.driver.quit()


# Case: 2
class CheckField(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
        chrome_options.add_experimental_option('prefs', {'intl.accept_languages': 'en_UK'})
        inst.driver = webdriver.Chrome(options=chrome_options)
        inst.driver.implicitly_wait(20)
        inst.driver.maximize_window()
        # Navigate to the application home page
        inst.driver.get("https://www.python.org/about/gettingstarted/")
        

    def test_CheckField(self):
        # Check Field & Data Type: Heading: "Python for Beginners"
        
        self.header = self.driver.find_element_by_xpath('//*[@id="content"]/div/section/article/header/h1')
        self.control = self.header.text

        try:
            self.assertEqual(self.control, "Python For Beginners")
        except AssertionError:
            assert False, "Check Field & Data Type: Heading: 'Python for Beginners' = Failed\n \t\tLook for: test_CheckField() "


    #def test_CheckField(self):
        ## Check Validation: "..."


    #def test_CheckContent(self):
        ## Check Validation: "..."

    @classmethod
    def tearDownClass(inst):
        inst.driver.quit()


if __name__ == '__main__':
    unittest.main()
