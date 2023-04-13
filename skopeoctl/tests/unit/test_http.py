"""test utils."""

import unittest

from skopeoctl import constants
from skopeoctl import http


class HTTPTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def test_http_get(self):
        headers = {
            'Content-Type': 'application/text'
        }
        result, resp = http.http_get(url=constants.SRC_IMAGE_LIST_URL, headers=headers)
        print(resp.split('\n'))
