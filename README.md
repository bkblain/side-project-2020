# side-project-2020

## Recommended Hardware List

- Raspberry Pi 4 and case
- Nooelec NESDR SMArt Bundle RTL-SDR
- 32 GB microSD
- keyboard and mouse
- HDMI cable and display
- USB memory card reader

# Raspbian Installation

1. Install the Raspberry Pi Imager and create Raspbian microSD
2. Install the microSD and setup OS
3. Continue configuring the OS through the __Raspberry Pi Software Configuration Tool__
4. Run `sudo raspi-config` to open the config tool 

## Raspbian Lite Configuration

1. Configure the keyboard first. A bad keyboard layout can mess up other steps.
    - Select _Localisation Options_
    - Select _Change Keyboard Layout_
    - Select _Generic 105-key PC_
    - If the keyboard list is showing non US layouts
      - Select _Other_
      - Select _English (US)_
      - The layout list will reload with english layouts.
    - Select _English (US)_
    - Select _The default for the keyboard layout_
    - Select _No compose key_
2. Select _Change User Password_ to change the default password
3. Select _Network Options_ to change the hostname
    - Select _Hostname_ and follow the instructions
4. Select _Network Options_ to connect to wifi
    - Select _Wi-fi_ and follow the instructions
5. Select _Interfacing Options_ to configure SSH
    - Select _SSH_ and follow the instructions
6. Exit the config tool
7. Run `ifconfig` to make sure that `wlan0` has received an IP address

## Raspbian Desktop

1. Select _Change User Password_ to change the default password
2. Select _Network Options_ to change the hostname
    - Select _Hostname_ and follow the instructions
3. Select _Interfacing Options_ to configure SSH
    - Select _SSH_ and follow the instructions
4. Exit the config tool
5. Run `ifconfig` to make sure that `wlan0` has received an IP address

## Configure Firewall

1. Run `sudo apt install ufw` to install __Uncomplicated Firewall__
2. Run `sudo ufw allow from 192.168.100.0/24 to any port 22` substitute the IP address with the domain ranges
3. Run `sudo ufw default deny incoming && sudo ufw default allow outgoing` to configure default rules
4. Run `sudo ufw enable` to enable the firewall
5. Run `sudo systemctl enable ufw` to start the service on boot

## Configure RTL-SDR

1. Run `sudo apt install rtl-sdr` to install RTL-SDR libraries
2. Run `sudo apt install sox` to install SoX which will stream audio


This command will stream audio through the hdmi port
``sudo rtl_fm -g 50 -f 89.5M -M wbfm -s 256k | play -r 32k -es -t raw -b 16 -c 1 -| omxplayer -o hdmi -p``

Install PIP for package management

`sudo apt install python3-pip`

Don't install through pip, instead install pipenv which can be used to generate an environment for the project much like npm.

`pip3 install pipenv`

`pipenv install pyrtlsdr`

install the python rtlsdr wrapper. this wraps the librtlsdr

`pip3 install pyrtlsdr`

- https://mode-s.org/decode/
- https://www.allaboutcircuits.com/projects/track-overhead-flights-raspberry-pi-zero-w-software-defined-radio/
- https://pypi.org/project/pyrtlsdr/
- https://inst.eecs.berkeley.edu/~ee123/sp16/labs.html
- https://wiki.gnuradio.org/index.php/Guided_Tutorial_GNU_Radio_in_Python
- https://github.com/itdaniher/rtlsdr-rds-demod

## Advanced

Streaming links
- https://pypi.org/project/pyrtlsdr/
- https://docs.python.org/3/library/asyncio.html
- https://pyrtlsdr.readthedocs.io/en/latest/Overview.html
- https://pyrtlsdr.readthedocs.io/en/latest/rtlsdraio.html
- https://realpython.com/async-io-python/

Kubernetes

- https://kubernetes.io/docs/tasks/tools/install-kubectl/#install-kubectl-on-linux

Using k3s

- https://github.com/teamserverless/k8s-on-raspbian/blob/master/GUIDE.md
- https://medium.com/parkbee/life-on-the-edge-a-first-look-at-ranchers-lightweight-kubernetes-distro-k3s-15a3aab1f0fb

show the nodes
``sudo k3s kubectl get node``

taint the master node
``sudo k3s kubectl taint nodes brian-zenbook key=value:NoSchedule``

remove swap to increase k8s performance
```
sudo dphys-swapfile swapoff && \
sudo dphys-swapfile uninstall && \
sudo update-rc.d dphys-swapfile remove
```

``sudo systemctl disable dphys-swapfile``

add a role to the new node
``sudo k3s kubectl label node raspberrypi node-role.kubernetes.io/node=""``

delete a label
``sudo k3s kubectl label node raspberrypi node-role.kubernetes.io/node-``

show node labels
``sudo k3s kubectl get nodes --show-labels``

### nginx test

http://192.168.1.2:30124/

use nginx-test.yml

deploy pod
``sudo k3s kubectl apply -f nginx-test.yml``

delete pod
``sudo k3s kubectl delete -f nginx-test.yml``

get all pods on all nodes
``kubectl get pod -o=custom-columns=NODE:.spec.nodeName,NAME:.metadata.name --all-namespaces``


### docker

- https://www.docker.com/blog/getting-started-with-docker-for-arm-on-linux/

Add the current user to the docker group to avoid needing sudo to run the docker command:
``sudo usermod -aG docker $USER``

relogin into user for group to take affect or `su - $USER`

The problem with building images is that the Pi is ARMv7 (armhf) so we need to enable the experimental `buildx` for docker to build multi architecture containers
https://github.com/docker/buildx

``
export DOCKER_CLI_EXPERIMENTAL=enabled
export DOCKER_BUILDKIT=1
docker build --platform=local -o . git://github.com/docker/buildx
mkdir -p ~/.docker/cli-plugins
mv buildx ~/.docker/cli-plugins/docker-buildx
``

``docker --help`` should confirm the new `buildx` command

grab the latest QEMU (amd64 version)
https://hub.docker.com/r/docker/binfmt/tags

`docker pull docker/binfmt:a7996909642ee92942dcd6cff44b9b95f08dad64-amd64`

this doesnt last a reboot?
`docker run --rm --privileged docker/binfmt:a7996909642ee92942dcd6cff44b9b95f08dad64-amd64`

check QEMU
`cat /proc/sys/fs/binfmt_misc/qemu-aarch64`




### Creating Raspberry Pi Container

http://www.guoyiang.com/2016/11/04/Build-My-Own-Raspbian-Docker-Image/

``losetup -f`` will find the next unused loop device location

``sudo losetup -Pr `losetup -f` <file>``

``losetup --list`` to list all devices


This will create a tar that doesn't have a '.' directory in the beginning.
``sudo find /mnt/rpi/ -printf "%P\n" | sudo tar -C /mnt/rpi -czpf ~/Downloads/2020-02-13-raspbian-buster-lite.tar.gz --numeric-owner --no-recursion -T -``




useful links
- https://gqrx.dk/doc/practical-tricks-and-tips
- https://payatu.com/getting-started-radio-hacking-part-2-listening-fm-using-rtl-sdr-gqrx
- https://www.nooelec.com/store/downloads/dl/file/id/72/product/0/nesdr_installation_manual_for_ubuntu.pdf


Install docker
https://linuxconfig.org/how-to-install-docker-on-ubuntu-20-04-lts-focal-fossa
