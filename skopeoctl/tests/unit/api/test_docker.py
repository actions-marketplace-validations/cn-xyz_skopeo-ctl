"""test python skopeo utils."""

import unittest

from skopeoctl.api.docker import DockerV2


class DockerV2TestCase(unittest.TestCase):

    def setUp(self):
        self.docker = DockerV2()

    def test_last_tag(self):
        name = 'gcmirrors/kube-apiserver'
        print(self.docker.last_tag(name))

        name = 'gcmirrors/no-exist'
        print(self.docker.last_tag(name))

    def test_last_tag(self):
        name = 'gcmirrors/kube-apiserver'
        print(self.docker.last_tag(name))

        name = 'gcmirrors/no-exist'
        print(self.docker.last_tag(name))
