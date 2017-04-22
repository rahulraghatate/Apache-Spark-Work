#!/bin/bash

# Change Directory for playbook_run:

cd $HOME/github/cloudmesh.street/ansible

#Run ansible playbook:

ansible-playbook opencv_setup.yaml --ask-sudo-pass -v


