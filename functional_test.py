from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):

        self.browser = webdriver.Firefox()
    def tearDown(self):

        self.browser.quit()
    def test_can_start_a_list_and_retrieve_it_later(self):

 # Эдит слышала про крутое новое онлайн-приложение со
 # списком неотложных дел. Она решает оценить его
 # домашнюю страницу
        self.browser.get('http://localhost:8000')
 # Она видит, что заголовок и шапка страницы говорят о
 # списках неотложных дел
        self.assertIn('To-Do', self.browser.title)
        self.fail('Закончить тест!')
 # Ей сразу же предлагается ввести элемент списка

if __name__ == '__main__':
    unittest.main(warnings='ignore')
