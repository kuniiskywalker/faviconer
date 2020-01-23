import unittest
from unittest.mock import patch

import src.faviconer.main as faviconer

class FaviconerTestCase(unittest.TestCase):

    @patch('faviconer.requests.get')
    def test_get_by_url1(self, mock_get):
        """When the favicon url is specified in the meta tag"""
        class MockResponse:
            def __init__(self):
                self.status_code = 200
                self.text = '<html><head><link rel="shortcut icon" href="https://cdn.sstatic.net/Sites/stackoverflow/img/favicon.ico"></head><body></body</html>'

        mock_get.return_value = MockResponse()

        url = "https://example.com/aaa/?teateate"
        actual = faviconer.get_by_url(url)
        self.assertEqual(actual, 'https://cdn.sstatic.net/Sites/stackoverflow/img/favicon.ico')

    # @patch('faviconer.requests.get')
    # def test_get_by_url2(self, mock_get):
    #     """When the favicon url is not specified in the meta tag"""
    #     class MockResponse:
    #         def __init__(self):
    #             self.status_code = 200
    #             self.text = '<html><head></head><body></body</html>'
    #
    #     mock_get.return_value = MockResponse()
    #
    #     url = "https://example.com/aaa/?teateate"
    #     actual = faviconer.get_by_url(url)
    #     self.assertEqual(actual, 'https://example.com/favicon.ico')

    def test_get_url1(self):
        """Perform conversion to scheme and domain"""
        url = "https://example.com/aaa/?teateate"
        actual = faviconer.get_url(url)
        self.assertEqual(actual, 'https://example.com/')

    def test_get_url2(self):
        """Perform conversion to scheme and domain"""
        url = "https://example.com"
        actual = faviconer.get_url(url)
        self.assertEqual(actual, 'https://example.com/')

    def test_get_default(self):
        """Convert a specific URL to a standard favicon url"""
        actual = faviconer.get_default("https://example.com/aaa/?teateate")
        self.assertEqual(actual, 'https://example.com/favicon.ico')

    def test_favicon_by_html(self):
        """Get favicon url from meta tag"""
        html = '<html><head><link rel="shortcut icon" href="https://cdn.sstatic.net/Sites/stackoverflow/img/favicon.ico"></head><body></body</html>';
        actual = faviconer.get_by_html(html)
        self.assertEqual(actual, 'https://cdn.sstatic.net/Sites/stackoverflow/img/favicon.ico')