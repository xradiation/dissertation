

- Start with a good french greeting
- Describe your work in few sentences
- What problems we're trying to solve here
    - Virtualization is slow
    - Containerization is insecure


# Application Phase

## Projector

```
xrandr --output HDMI-2 --auto [POSITION] eDP-1 --mode [RESOLUTION]
xrandr --output HDMI-2 --auto --above eDP-1 --mode 1920x1080
xrandr --output HDMI-2 --auto --above eDP-1 --mode 1280x720
```

Make the projector as another monitor using the above command, replace `POSITION` with

```
--above
--right-of
--left-of
--bellow
```

Change the `RESOLUTION` if the output image is distorted or unaligned

```
1280x720, 1920x1080
```


Switch between different monitors using the `mouse` or the following keyboard shortcuts

```
Mod + ,
Mod + .
```

Move windows between monitors using

```
Mod + Shift + ,
Mod + Shift + .
```

## Connections

Start the fedora VM only, to keep containers snappy; After the containers tests start the archlinux VM while keeping the fedora VM running to provide DNS services

- Use `scrcpy` to cast your android screen.
    - Connect you android phone using USB
    - Enable ADB
    - Set USB to `PTP` mode if ADB access is denied
    - Or use ADB over network if USB ADB didn't work
    - Use the following command

    ```
    scrcpy --max-fps 30 --max-size 1920 --show-touches --fullscreen --turn-screen-off --record-format mp4 --record diss_and_rec.mp4
    ```

    - Use `win+r` for landscape mode
    - `win+n` enable wifi, connect to the access point

## Test Containers

- Show the network configuration of the containers `docker network ls` & `docker network inspect nextc-sqll_default`
- Show the docker images `stress` & `perkeep's` Dockerfile

- Test Cgroups resource limits first
    - Recreate the stress test on the paper
    - Show resource consumption on `portainer`

- Test SELinux Access Control Second
    - Start with permissive mode `setenforce 0`
    - Recreate the access scenario on the paper
    - `setenfoce 1`
    - Make sure to show them the "Access Denied" error message

- Allow members to test the setup, One by one in order lower resource consumption

## Test Qemu/KVM UI

- Test Qemu/KVM web UI
    - Connect to the UI `http://arch.dom.net`
    - Create a `FreeBSD` or `OpenBSD` VM
    - Try `Windows 10` or `Ubuntu Desktop` VM for gui interface
    - Head over to the `Start VM` tab and run `debian` VM to demonstrate start functionality

