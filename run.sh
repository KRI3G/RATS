#!/usr/bin/env bash

# Allow systemd to run in selinux systems
if command -v gentenforce &>/dev/null; then
    setsebool -P container_manage_cgroup 1
fi

# Create containerssh user
sudo useradd containerssh
sudo id containerssh -u > id.env

# Enable podman on user socket

# Create student-guest image from Dockerfile

# Run containerssh binary

# Configure config file with env vars
# (please refer to documentation)
source *.env
envsubst < ./config/config.template.yaml > ./config/config.yaml


