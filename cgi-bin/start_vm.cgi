#!/bin/bash

echo "Content-type: text/html"
echo ""

vnc_db="/srv/http/vm/vncdb"
vm_path="/srv/http/vm"

read POST_STRING

operating_system=`echo "$POST_STRING" | sed -n 's/^.*operating_system=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
vm_name=`echo "$POST_STRING" | sed -n 's/^.*vm_name=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
storage_format=`echo "$POST_STRING" | sed -n 's/^.*storage_format=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
memory=`echo "$POST_STRING" | sed -n 's/^.*memory=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
vnc_port=`echo "$POST_STRING" | sed -n 's/^.*vnc_port=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
kb_layout=`echo "$POST_STRING" | sed -n 's/^.*kb_layout=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`

ps aux | grep -Eo "vnc :[0-9]{1,4}" | awk -F ':' '{print $2}' > $vnc_db

if [[ $vnc_port -eq 0 ]];then
	vnc_port=$(shuf -i 0-1000 | head -n 1)
elif [[ $(grep -x $vnc_port $vnc_db) ]];then
	echo "<h1> Redirection ...<h1>\
		<script> alert(\"The VNC Port : _ $vnc_port _ is not available !!!\"); \
		window.history.back(); </script>"
	exit 1
elif [[ $(ls -w1 $vm_path | grep -x $vm_name.pid) ]]; then
	echo "<h1> Redirection ...<h1>\
		<script> alert(\"Virtual Machine _ $vm_name _ Already Running !!!\");\
		window.history.back(); </script>"
	exit 1
else :;fi

qemu_vnc=$((5900+$vnc_port))
echo "<script> alert(\"Please Connect to VNC Port : $qemu_vnc\") </script>"

qemu-system-x86_64 \
		 -daemonize \
		 -k $kb_layout \
		 -monitor none \
		 -smp 1 -cpu host \
		 -boot menu=on \
		 -machine accel=kvm -m $memory \
		 -name $vm_name \
		 -vnc :$vnc_port \
		 -drive file=/srv/http/vm/$vm_name,index=0,if=ide,media=disk \
		 -pidfile "/srv/http/vm/$vm_name.pid"
echo "<h1> Redirection ...<h1>\
<script> window.history.back();</script>"

