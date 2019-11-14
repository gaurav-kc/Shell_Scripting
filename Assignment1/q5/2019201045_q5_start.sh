temp1=$( which openvpn )
if ! [ $temp1 != "" ] ;
then
	sudo apt install openvpn
fi
sudo chmod 777 /etc/resolv.conf
wget -O iiitvpn.ovpn --user gaurav.chaudhari@students.iiit.ac.in --password Gauravkc307 "https://vpn.iiit.ac.in/secure/ubuntu.ovpn"
sudo sed -i '1s/^/nameserver 10.4.20.204\n/' /etc/resolv.conf
sudo openvpn --config  iiitvpn.ovpn
