from selenium import webdriver
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

        # Page title mentions to-do lists.
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # User is immediately invited to enter a to-do item.

        # User types "Buy peacock feathers".

        # When user hits enter, the page updates, and now the page lists
        # "1. Buy peacock feather" as an item in a to-do list.

        # There is still a box inviting the user to add another item. She
        # enters "Use peacock feather to make a fly".

        # The page updates again, and now shows both items on her list.

        # The site has generated a unique URL for the user -- there is some
        # text to explain this.

        # By visiting this unique URL, the user has access to her to-do list
        # again.

if __name__ == '__main__':
    unittest.main(warnings='ignore')
