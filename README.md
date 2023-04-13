# Container Images Sync

Github Actions for [Container Images Sync](https://github.com/marketplace/actions/container-images-sync)

## How to Use by Github Actions

```
    - name: Container Images Sync
      uses: cnxyz/skopeo-ctl@v1.0.0
      env:
        GIT_ORG: "cn-xyz"
        GIT_REPO: "image-sync"
        GIT_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        SRC_IMAGE_LIST_URL: "https://raw.githubusercontent.com/cn-xyz/image-sync/main/k8s.txt"
        DEST_REPO: "docker.io/cnxyz"
        SRC_TRANSPORT: "docker"
        DEST_TRANSPORT: "docker"
        DEST_TRANSPORT_USER: "user"
        DEST_TRANSPORT_PASSWORD: "password"
        LOG_LEVEL: "DEBUG"
```

Environment Variables:

- GIT_ORG: github org
- GIT_REPO: github repo
- GIT_TOKEN: github token
- SRC_IMAGE_LIST_URL: SRC_IMAGE_LIST_URL, default: "https://raw.githubusercontent.com/cn-xyz/image-sync/main/k8s.txt"
- DEST_REPO: DEST register REPO
- SRC_TRANSPORT: SRC TRANSPORT
- DEST_TRANSPORT: DEST TRANSPORT
- DEST_TRANSPORT_USER: "user"
- DEST_TRANSPORT_PASSWORD: "password"
- THREAD_POOL_NUM: sync thread pool num

## Dev and Test

- local run

```
# install
pip3 install -r requirements.txt
python3 setup.py install

# set env
export GIT_ORG="cn-xyz"
export GIT_REPO="image-sync"
export GIT_TOKEN='${{ secrets.GITHUB_TOKEN }}'
export SRC_IMAGE_LIST_URL="https://raw.githubusercontent.com/cn-xyz/image-sync/main/k8s.txt"
export DEST_REPO="docker.io/cnxyz"
export SRC_TRANSPORT="docker"
export DEST_TRANSPORT="docker"
export DEST_TRANSPORT_USER="user"
export DEST_TRANSPORT_PASSWORD="password"

# run sync
skopeoctl
```

- tests

```
python3 -m unittest skopeoctl.tests.unit.test_skopeo.SkopeoTestCase.test_do_sync
```

- [Docker API Rate Limiting](https://docs.docker.com/docker-hub/api/latest/#tag/rate-limiting)

- X-RateLimit-Limit - The limit of requests per minute.
- X-RateLimit-Remaining - The remaining amount of calls within the limit period.
- X-RateLimit-Reset - The unix timestamp of when the remaining resets.

If you have hit the limit, you will receive a response status of 429 and the X-Retry-After header in the response.

The X-Retry-After header is a unix timestamp of when you can call the API again.

```
< x-ratelimit-limit: 180
< x-ratelimit-reset: 1646881125
< x-ratelimit-remaining: 180
```