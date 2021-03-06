#!/bin/bash

echo "Content-type: text/html"
echo ""

vnc_db="/srv/http/vm/vncdb"
iso_db="/srv/http/iso/isodb"
vm_path="/srv/http/vm"
iso_path="/srv/http/iso"

read POST_STRING

operating_system=`echo "$POST_STRING" | sed -n 's/^.*operating_system=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
vm_name=`echo "$POST_STRING" | sed -n 's/^.*vm_name=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
storage_format=`echo "$POST_STRING" | sed -n 's/^.*storage_format=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
memory=`echo "$POST_STRING" | sed -n 's/^.*memory=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
disk_space=`echo "$POST_STRING" | sed -n 's/^.*disk_space=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
vnc_port=`echo "$POST_STRING" | sed -n 's/^.*vnc_port=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
kb_layout=`echo "$POST_STRING" | sed -n 's/^.*kb_layout=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`

ps aux | grep -Eo "vnc :[0-9]{1,4}" | awk -F ':' '{print $2}' > $vnc_db
ls -w1 $iso_path > $iso_db 

if [[ $vnc_port -eq 0 ]];then
	vnc_port=$(shuf -i 0-1000 | head -n 1)
fi

if [[ $(grep -x $vnc_port $vnc_db) ]];then
	echo "<h1> Redirection ...<h1>\
		<script> alert(\"The VNC Port : _ $vnc_port _ is not available !!!\"); \
		window.history.back(); </script>"
	exit 1
elif [[ $(ls -w1 $vm_path | grep -x $vm_name) ]] || [[ $(ls -w1 $vm_path | grep -x $vm_name.pid) ]]; then
	echo "<h1> Redirection ...<h1>\
		<script> alert(\"Virtual Machine Name _ $vm_name _ Already Exists !!!\");\
		window.history.back(); </script>"
	exit 1
elif ! [[ $(grep -x "$operating_system.iso" $iso_db) ]];then
	echo "<h1> Redirection ...<h1>\
		<script> alert(\"Please Select an Operating System To Install !!!\");\
		window.history.back(); </script>"
	exit 1
else :;fi

qemu_vnc=$((5900+$vnc_port))
echo "<script> alert(\"Please Connect to VNC Port : $qemu_vnc\") </script>"

if [[ $disk_space -eq 0 ]];then
use_disk=''
else use_disk="-drive file=/srv/http/vm/$vm_name,index=2,if=ide,media=disk"
	if [[ $(qemu-img create -f $storage_format \
		/srv/http/vm/$vm_name $disk_space"G") ]];then :
	else exit 1;fi
fi
qemu-system-x86_64 \
		 -daemonize \
		 -k $kb_layout \
		 -monitor none \
		 -smp 1 -cpu host \
		 -boot order=cd,menu=on \
		 -machine accel=kvm -m $memory \
		 -name $vm_name \
		 -vnc :$vnc_port \
		 -drive file="/srv/http/iso/$operating_system.iso",index=0,if=ide,media=cdrom \
		 -pidfile "/srv/http/vm/$vm_name.pid" $use_disk
echo "<h1> Redirection ...<h1>\
<script> window.history.back();</script>"

