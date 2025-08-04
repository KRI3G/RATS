# Pull containerssh agent image for its binary
FROM quay.io/containerssh/agent AS agent

# Set UBI as last layer
FROM registry.access.redhat.com/ubi9/ubi-init
USER root

# Copy containerssh agent binary
COPY --from=agent /usr/bin/containerssh-agent /usr/bin/containerssh-agent

# Install necessary packages
RUN dnf -y install openssh openssh-server ncurses sudo bash-completion ping nc

# Enable necessary packages
RUN systemctl enable sshd

# Create test student
RUN useradd student && \
    mkdir -p /home/student && \
    chown student:student /home/student && \
    echo "redhat" | passwd student --stdin

# Expose SSH
EXPOSE 22

# Enter into init process
CMD [ "/sbin/init" ]
