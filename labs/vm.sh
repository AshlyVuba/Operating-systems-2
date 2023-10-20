#!/bin/bash
az vm create \
  --resource-group Ops2\
  --name my-vm \
  --public-ip-sku Standard \
  --image Ubuntu2204 \
  --admin-username azureuser \
  --generate-ssh-keys
