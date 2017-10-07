#/bin/bash
sudo ifconfig rename3 down
sudo ifconfig rename3 up
processo=`ps -A | grep Network* |awk {'print $1'}`
sudo kill -9 $processo



