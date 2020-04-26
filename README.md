# side-project-2020

useful links
- https://gqrx.dk/doc/practical-tricks-and-tips
- https://payatu.com/getting-started-radio-hacking-part-2-listening-fm-using-rtl-sdr-gqrx
- https://www.nooelec.com/store/downloads/dl/file/id/72/product/0/nesdr_installation_manual_for_ubuntu.pdf

## Steps
1. Format SD Card
2. Install the Raspberry Pi Imager and create Raspbian SD
3. Put raspberry pi hardware together
4. Install and setup OS
5. Enable SSH via ``sudo raspi-config``
6. Install rtl-sdr ``sudo apt install rtl-sdr``
7. install sox
8. ``sudo rtl_fm -g 50 -f 89.5M -M wbfm -s 256k | play -r 32k -es -t raw -b 16 -c 1 -| omxplayer -o hdmi -p``

TODO:
- static IP?
- TeamViewer for screen sharing


## Advanced

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

