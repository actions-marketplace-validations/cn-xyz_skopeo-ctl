"""test utils."""

import unittest

from skopeoctl.shell import CIS


class CISTestCase(unittest.TestCase):

    def setUp(self):
        self.cis = CIS()

    def test_gcrio_sort_tags(self):
        src_repo, name = 'k8s.gcr.io', 'kube-apiserver'
        self.cis.init_source_registry_api(src_repo, None)
        print(self.cis._source_registry.sort_tags(name))

        src_repo, name = 'gcr.io/ml-pipeline', 'api-server'
        if '/' in src_repo:
            registry_url, repo = src_repo.split('/')
            self.cis.init_source_registry_api(registry_url, repo)
        else:
            self.cis.init_source_registry_api(src_repo)
        print(self.cis._source_registry.sort_tags(name))

    def test_sync_image_k8s_pause(self):
        image = 'k8s.gcr.io/pause'
        print(self.cis.sync_image(image))

    def test_sync_image_ml(self):
        image = 'gcr.io/ml-pipeline/api-server'
        print(self.cis.sync_image(image))

    def test_sync_image_nginx_ingress_controller(self):
        image = 'k8s.gcr.io/ingress-nginx/controller'
        print(self.cis.sync_image(image))

    def test_sync_image_quayio_metallb_controller(self):
        image = 'quay.io/metallb/controller'
        print(self.cis.sync_image(image))

    def test_sync_image_knative_serving_webhook(self):
        image = 'gcr.io/knative-releases/knative.dev/serving/cmd/webhook'
        print(self.cis.sync_image(image))

    def test_sync_image_tektoncd_dashboard_dashboard(self):
        image = 'gcr.io/tekton-releases/github.com/tektoncd/dashboard/cmd/dashboard'
        print(self.cis.sync_image(image))

    def test_sync_image_distroless_base(self):
        image = 'gcr.io/distroless/base'
        print(self.cis.sync_image(image))

    def test_sync_image_gke_mpi_metadata_server(self):
        image = 'us.gcr.io/k8s-artifacts-prod/gke-mpi-metadata-server'
        print(self.cis.sync_image(image))
