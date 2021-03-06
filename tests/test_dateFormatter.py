#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author:
# Linwood Creekmore
# Email: valinvescap@gmail.com

from unittest import TestCase

from gdelt.dateFuncs import dateformatter


class TestDateFormatter(TestCase):
    def test_dateFormatter(self):
        date_string = 'March 22 2016'
        formatter_test = dateformatter(date_string)
        exp = '2016-03-22'
        self.assertEqual(formatter_test, exp, "dateformatter working")

