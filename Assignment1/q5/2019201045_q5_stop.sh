#!/bin/bash
sudo sed -i '1d' /etc/resolv.conf
rm iiitvpn.ovpn
sudo killall openvpn
