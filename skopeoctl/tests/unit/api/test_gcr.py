"""test python skopeo utils."""

import unittest

from skopeoctl.api.gcr import GoogleContainerRegisterV2


class GoogleContainerRegisterV2TestCase(unittest.TestCase):

    def setUp(self):
        self.gcr = GoogleContainerRegisterV2()

    def test_list_tags(self):
        name = 'kube-apiserver'
        print(self.gcr.list_tags(name))

    def test_sort_tags(self):
        name = 'kube-apiserver'
        print(self.gcr.sort_tags(name))
