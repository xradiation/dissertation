

Based on what we've seen, we can conclude that containerization isn't really going to contain cyber threats at least not as good as the virtualization does. *ARES Algeria* decided to take containerization security a step further in their infrastructure by implementing a hybrid solution where both technologies notably virtualization & containerization work side by side for better security standards across the board.

# Working Plan

The network topology contains 3 machines in total, A single Host which is running `Archlinux` [ Linux ] as an operating system, And two guest VMs on top of the host one for Containerization & the other is for Virtualization; Both of which are running `Fedora` and `Archlinux` respectively.

I.  The main machine or the host is running the following
    + Qemu/KVM
    + Libvirt
    + VirtManager
    + Openvswitch (OVS)

II.  The first guest is a Fedora containerization VM running
     + Docker
     + Docker Compose
       * Nextcloud
       * Syncthing
       * Duplicati
       * Perkeep
       * Postgresql
       * Adminer
       * Jellyfin
     + SELinux
     + cgroups

III.  The Second guest is an Archlinux virtualization VM running Qemu/KVM
      + Qemu/KVM
      + Apache Web Server
      + Custom Qemu/KVM Web UI
