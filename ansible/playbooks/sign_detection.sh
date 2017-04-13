#!/bin/sh
ansible-playbook local_machine_setup.yaml --ask-sudo-pass -vvvv
ansible-playbook cloud_cluster_setup.yaml --ask-sudo-pass -vvvv
ansible-playbook hadoop_spark_deploy.yaml --ask-sudo-pass -vvvv
ansible-playbook opencv_setup.yaml --ask-sudo-pass -vvvv

