from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):

        # User goes to homepage.
        self.browser.get('http://localhost:8000')

        # Page title and header mention to-do lists.
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # User is invited to enter a to-do item straight away.
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # User types "Buy peacock feathers" into a text box.
        inputbox.send_keys('Buy peacock feathers')

        # When user hits enter, the page updates, and now the page lists
        # "1. Buy peacock feather" as an item in a to-do list.
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows),
            "New to-do item did not appear in table"
        )

        # There is still a box inviting the user to add another item. The user
        # enters "Use peacock feather to make a fly".
        self.fail('Finish the test!')

        # The page updates again, and now shows both items on her list.

        # The site has generated a unique URL for the user -- there is some
        # text to explain this.

        # By visiting this unique URL, the user has access to her to-do list
        # again.

if __name__ == '__main__':
    unittest.main(warnings='ignore')
