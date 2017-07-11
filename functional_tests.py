from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to do app.  She goes
        # to check out it's homepage
        self.browser.get('http://localhost:8000')
        # she notices the title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish The Test!')

        # she is invited to enter a to-do item straight away

        # she types "Buy peacock feathers" into a text box
        # her hobby is fly fishing lures

        # when she hits enter, the page updates and now the page lists
        # 1.  Buy peacock feathers to make a fly

        # the page updates again and shows both items on her lists

        # Edith wonders whether the site will remember her list.  Then she sees
        # that the site has generated a unique url for her.  --
        # There is some explanatory text to that effect.

        # she visits that url, her list is still There

        # Satisfied, she goes back to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')
