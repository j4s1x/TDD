from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.keys import Keys

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
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
        # she is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),'enter a to-do item')
        # she types "Buy peacock feathers" into a text box
        # her hobby is fly fishing lures
        inputbox.send_keys('Buy peacock feathers')
        # when she hits enter, the page updates and now the page lists
        # 1.  Buy peacock feathers to make a fly
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Buy peacock feathers', [row.text for row in rows])
        self.assertIn(
            '2: Use peacock feathers to make a fly',
            [row.text for row in rows]
        )
        # the page updates again and shows both items on her lists

        # Edith wonders whether the site will remember her list.  Then she sees
        # that the site has generated a unique url for her.  --
        # There is some explanatory text to that effect.

        # she visits that url, her list is still There

        # Satisfied, she goes back to sleep
        self.fail('finish the test')
if __name__ == '__main__':
    unittest.main(warnings='ignore')
