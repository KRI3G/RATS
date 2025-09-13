#!/bin/sh

ssh-keygen -q -N "" -t rsa -b 4096 -f ssh_host_rsa_key
ssh-keygen -q -N "" -t ed25519 -f ssh_host_ed25519_key

# Public key files are not needed
rm ssh_host_*_key.pub

# WATCH THE UID:GID SETTINGS, they must match containerssh's running user
