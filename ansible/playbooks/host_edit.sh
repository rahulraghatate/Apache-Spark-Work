#!/bin/sh
cm cluster nodes cluster-002|awk '{print $2 " " $1}'> ip_list
sed -i 's/$/ ansible_ssh_user=cc/' ip_list
sed '/\[all_nodes\]/a ip_list hosts
