"""test utils."""

import unittest

from skopeoctl import utils


class UtilsTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def test_date2timestamp(self):  # noqa
        date_time = '2020-06-28T11:46:53.539425Z'
        print(utils.date2timestamp(date_time))

    def test_generate_dest_name(self):  # noqa
        # eventing-in_memory-channel_controller
        print(utils.generate_dest_name('gcr.io/knative-releases/knative.dev/eventing/cmd/in_memory', 'channel_controller'))
        print(utils.generate_dest_name('gcr.io/knative-releases/knative.dev/eventing/cmd', 'appender'))
        print(utils.generate_dest_name('gcr.io/tekton-releases/github.com/tektoncd/triggers/cmd', 'webhook'))
