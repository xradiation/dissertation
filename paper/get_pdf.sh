#!/usr/bin/guestfish -f
add-drive /home/hicham/.vms/arch.qcow2 --rw
run
mount /dev/sda1 /
copy-in /home/hicham/Downloads/git/project/paper/text_en.md /home/user/paper
copy-out /home/user/paper/text_en.pdf /home/hicham/Downloads/git/project/paper/
umount /dev/sda1
shutdown
exit

