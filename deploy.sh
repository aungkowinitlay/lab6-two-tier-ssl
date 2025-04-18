#!/bin/bash

cd /path/to/lab6-two-tier-ssl

# Stop running containers
docker compose down

# Rebuild and run containers
docker compose up -d --build

# Reload nginx
sudo nginx -t && sudo systemctl reload nginx
