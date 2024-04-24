#!/usr/bin/env python3

import unittest
from analyze.src.main.app import watering_time, get_health, get_metrics


class TestAnalyzer(unittest.TestCase):

    def test_watering_time(self):
        suggestion = watering_time(0, 0)
        self.assertEqual(suggestion, 20)

    def test_health(self):
        health = get_health()
        self.assertEqual(health.status_code, 200)

    def test_metrics(self):
        metrics = get_metrics()
        self.assertEqual(metrics.data, b"request count: 2.0")


if __name__ == '__main__':
    unittest.main()
