import unittest

import src.faviconer.main as faviconer

class DefaultWidgetSizeTestCase(unittest.TestCase):
    def test_geturl1(self):
        url = "https://example.com/aaa/?teateate"
        actual = faviconer.get_url(url)
        self.assertEqual(actual, 'https://example.com/')

    def test_geturl2(self):
        url = "https://example.com"
        actual = faviconer.get_url(url)
        self.assertEqual(actual, 'https://example.com/')

    def test_favicon_by_url(self):
        actual = faviconer.get_by_url("https://example.com/aaa/?teateate")
        self.assertEqual(actual, 'https://example.com/favicon.ico')

    def test_favicon_by_html(self):
        html = '<html><head><link rel="shortcut icon" href="https://cdn.sstatic.net/Sites/stackoverflow/img/favicon.ico"></head><body></body</html>';
        actual = faviconer.get_by_html(html)
        self.assertEqual(actual, 'https://cdn.sstatic.net/Sites/stackoverflow/img/favicon.ico')