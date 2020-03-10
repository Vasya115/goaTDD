from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):

        self.browser = webdriver.Firefox()
    def tearDown(self):
        self.browser.quit()


    def check_for_row_in_list_table(self, row_text):
        '''подтверждение строки в таблице списка'''
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])


    def test_can_start_a_list_and_retrieve_it_later(self):

 # Эдит слышала про крутое новое онлайн-приложение со
 # списком неотложных дел. Она решает оценить его
 # домашнюю страницу
        self.browser.get('http://127.0.0.1:8000')
 # Она видит, что заголовок и шапка страницы говорят о
 # списках неотложных дел
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
        inputbox.get_attribute('placeholder'),
        'Enter a to-do item'
        )
        inputbox.send_keys('Купить павлиньи перья')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table('Купить павлиньи перья')

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Сделать мушку из павлиньих перьев')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        self.check_for_row_in_list_table('Купить павлиньи перья')
        self.check_for_row_in_list_table('Сделать мушку из павлиньих перьев')

        self.fail('Закончить тест!')
 # Ей сразу же предлагается ввести элемент списка

if __name__ == '__main__':
    unittest.main(warnings='ignore')
