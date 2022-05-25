#!/usr/bin/env python3

import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
  def test_first_last_name(self):
    formatted_name = get_formatted_name('Tim', 'Furz')
    self.assertEqual(formatted_name, 'Tim Furz')
  
  def test_another_first_last_name(self):
    formatted_name = get_formatted_name('Jim', 'Puller')
    self.assertEqual(formatted_name, 'Lola Puller')

if __name__ == '__main__':
  unittest.main()