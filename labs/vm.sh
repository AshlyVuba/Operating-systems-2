#!/bin/bash
az vm create \
  --resource-group learn-4ea6852d-73d2-41ec-8c22-1d3e6498b73d \
  --name my-vm \
  --public-ip-sku Standard \
  --image Ubuntu2204 \
  --admin-username azureuser \
  --generate-ssh-keys
