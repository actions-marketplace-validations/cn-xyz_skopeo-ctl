import os


CURRENT_PATH = os.getcwd()

# Github info display sync result
GIT_TOKEN = os.environ.get('GIT_TOKEN', 'github_token')
GIT_ORG = os.environ.get('GIT_ORG', 'cn-xyz')
GIT_REPO = os.environ.get('GIT_REPO', 'image-sync')
SKIP_LONG_TAG = False
if os.environ.get('SKIP_LONG_TAG', False) in (True, "true", 1):
    SKIP_LONG_TAG = True

# skopeo args
"""
list like:
k8s.gcr.io/pause-amd64
gcr.io/ml-pipeline/api-server
"""
SRC_IMAGE_LIST_URL = os.environ.get(
    'SRC_IMAGE_LIST_URL',
    'https://raw.githubusercontent.com/cn-xyz/image-sync/main/k8s.txt')
DEST_REPO = os.environ.get('DEST_REPO', f'docker.io/{GIT_REPO}')
SRC_TRANSPORT = os.environ.get('SRC_TRANSPORT', 'docker')
DEST_TRANSPORT = os.environ.get('DEST_TRANSPORT', 'docker')

# thread pool
THREAD_POOL_NUM = int(os.environ.get('THREAD_POOL_NUM', 2))
LOG_LEVEL = os.environ.get('LOG_LEVEL', 'DEBUG')

# Only work when source is docker, because https://docs.docker.com/docker-hub/api/latest/#tag/rate-limiting
JOB_BATCH_COUNT = int(os.environ.get('JOB_BATCH_COUNT', 3))
