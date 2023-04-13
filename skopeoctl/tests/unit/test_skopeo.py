"""test python skopeo utils."""

import unittest

from skopeoctl.skopeo import Skopeo


class SkopeoTestCase(unittest.TestCase):

    def setUp(self):
        self.skopeo = Skopeo()

    def test_do_sync(self):
        src_repo = 'k8s.gcr.io'
        dest_repo = 'docker.io/gcmirrors'
        name = 'pause-amd64'
        src_transport = 'docker'
        dest_transport = 'docker'

        self.skopeo.do_sync(src_repo, dest_repo, name, src_transport, dest_transport)
