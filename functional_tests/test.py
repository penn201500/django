#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        self.browser.implicitly_wait(100)
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('td')
        self.assertIn(row_text, [row.text for row in rows])


    def test_can_start_a_list_and_retrieve_it_later(self):
        # visit to-do list website
        self.browser.get(self.live_server_url)

        # website homepage title and header include "To-Do" key word
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name("h1").text
        self.assertIn('To-Do', header_text)

        # input 1 to-do item
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        inputbox.send_keys('Buy peacock feathers')

        # press Enter, page will refresh
        inputbox.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('1: Buy peacock feathers')

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

        # table = self.browser.find_element_by_id('id_list_table')
        # rows = table.find_elements_by_tag_name('tr')
        # self.assertIn(
        #     # any(row.text == 'buy 1 thing' for row in rows),
        #     '1: Buy peacock feathers', [row.text for row in rows]
        #     # "New to-do item did not appear in table -- its text was:\n%s" % (
        #         # table.text,
        #     # )
        # )

        # input 2nd to-do item
        # inputbox = self.browser.find_element_by_id('id_new_item')
        # inputbox.send_keys('Use peacock feathers to make a fly')
        # inputbox.send_keys(Keys.ENTER)

        # # press Enter, page will refresh
        # table = self.browser.find_element_by_id('id_list_table')
        # rows = table.find_elements_by_tag_name('tr')
        # self.assertIn(
        #     '1: Buy peacock feathers', [row.text for row in rows]
        # )
        # self.assertIn(
        #     '2: Use peacock feathers to make a fly',
        #     [row.text for row in rows]
        # )

        self.fail('Finish the test!')


