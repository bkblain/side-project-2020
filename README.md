# side-project-2020

useful links
- https://gqrx.dk/doc/practical-tricks-and-tips
- https://payatu.com/getting-started-radio-hacking-part-2-listening-fm-using-rtl-sdr-gqrx
- https://www.nooelec.com/store/downloads/dl/file/id/72/product/0/nesdr_installation_manual_for_ubuntu.pdf

## Steps
1. Format SD Card
2. Install the RPI Installer and create Raspbian SD
3. Put raspberry pi hardware together
4. Install and setup OS
5. Enable SSH via ``sudo raspi-config``
6. Install rtl-sdr ``sudo apt install rtl-sdr``
7. install sox
8. ``sudo rtl_fm -g 50 -f 89.5M -M wbfm -s 256k | play -r 32k -es -t raw -b 16 -c 1 -| omxplayer -o hdmi -p``

TODO:
- static IP?
- TeamViewer for screen sharing


# Advanced

Using k3s

show the nodes
``sudo k3s kubectl get node``

taint the master node
``sudo k3s kubectl taint nodes brian-zenbook key=value:NoSchedule``
