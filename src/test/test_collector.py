#!/usr/bin/env python3

import unittest
from collect.src.main.app import check_connection


class TestCollector(unittest.TestCase):

    def test_connection(self):
        connection = check_connection()
        self.assertEqual(connection, 200)


if __name__ == '__main__':
    unittest.main()
