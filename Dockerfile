FROM ubuntu:22.04

# Dockerfile build cache 
ENV REFRESHED_AT 2023-01-01

LABEL "com.github.actions.name"="Container Images Sync"
LABEL "com.github.actions.description"="Container Images Sync"
LABEL "com.github.actions.icon"="repeat"
LABEL "com.github.actions.color"="blue"
LABEL "repository"="http://github.com/cn-xyz/skopeo-ctl"
LABEL "homepage"="http://github.com/cn-xyz/skopeo-ctl"
LABEL "maintainer"="admin<admin@china.cn>"

LABEL "Name"="Container Images Sync"
LABEL "Version"="1.0.0"

ENV LC_ALL C.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8

# apt install -y docker-ce docker-ce-cli containerd.io systemctl start docker
RUN apt update && \
    apt install -y git python3 python3-pip skopeo jq && \
    cd ~ && \
    git clone https://github.com/cn-xyz/skopeo-ctl.git && \
    cd skopeo-ctl && \
    #git checkout v1.0.0 && \
    pip3 install -r requirements.txt && \
    python3 setup.py --version && \
    python3 setup.py install

ADD entrypoint.sh /
RUN chmod +x /entrypoint.sh

WORKDIR /github/workspace
ENTRYPOINT ["/entrypoint.sh"]
