#!/bin/bash

echo "Content-type: text/html"
echo ""

vm_path="/srv/http/vm"
iso_path="/srv/http/iso"
server_ip="192.168.122.3"

read POST_STRING

vm_name=`echo "$POST_STRING" | sed -n 's/^.*vm_name=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
storage_format=`echo "$POST_STRING" | sed -n 's/^.*storage_format=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`

if [[ $(ls -w1 $vm_path | grep -x ${vm_name}) ]];then
	echo "<h1> Downloading...<h1>\
		<script> window.location.href = \"http://$server_ip/vm/$vm_name\"; \
		</script>"
	exit 0
else
	echo "<h1> Redirection ...<h1>\
		<script> alert(\"The Image : _ $vm_name _ is not available !!!\"); \
		window.history.back(); </script>"
	exit 1
fi

