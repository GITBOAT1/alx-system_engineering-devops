#!/usr/bin/env bash
sudo ufw enable 
sudo ufw status;

if [ $# -gt 0 ]; then
	for i in $*; do
		echo "enablin .." $i;
		sudo ufw allow $i;
	done
	echo "--------------------------------"
	echo "current port enables "
	sudo ufw status;
else
    echo "Usage <port or service name> to enable"
fi
