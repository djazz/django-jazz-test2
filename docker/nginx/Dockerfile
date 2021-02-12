# Docker image instructions for the `nginx` service for all non-`local` application modes.

# nginx on debian:slim
# Doc: https://hub.docker.com/_/nginx/
# Dockerfile Ref: https://docs.docker.com/engine/reference/builder/

FROM nginx:1.19.6


# CONFIGURATION ====================================================================================

# Copy config files.
COPY ./conf.d/ /etc/nginx/conf.d/


# STARTUP ==========================================================================================

# Keep base image defaults.
