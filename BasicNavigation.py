import unittest
from selenium import webdriver


class PythonTest(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
        chrome_options.add_experimental_option('prefs', {'intl.accept_languages': 'en_UK'})
        inst.driver = webdriver.Chrome(options=chrome_options)
        inst.driver.implicitly_wait(30)
        inst.driver.maximize_window()
        # Navigate to the application home page
        inst.driver.get("https://www.python.org/")
        

    def test_Navigate(self):
        # Check Navigation: "Start with Our Beginner's Guide"
        # URL validation canbe added
        
        self.navigate_link = self.driver.find_element_by_link_text('Start with our Beginner’s Guide')
        self.navigate_link.click()

        #self.url = self.driver.current_url
        self.control = self.driver.title

        try:
            self.assertEqual(self.control, "Python For Beginners | Python.org")
        except AssertionError:
            assert False, "Navigate To: 'Start with our Beginner's Guide Page = Failed\n \t\tLook for: test_Navigate() "
        

    @classmethod
    def tearDownClass(inst):
        # close the browser window
        inst.driver.quit()

if __name__ == '__main__':
    unittest.main()
