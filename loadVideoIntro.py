#!/usr/bin/sudo /usr/bin/python3

def loadVideo(fileDir):
    with open("/etc/rc.local", "w+") as file:
        data = """#!/bin/sh -e
#
# rc.local
#
# This script is executed at the end of each multiuser runlevel.
# Make sure that the script will "exit 0" on success or any other
# value on error.
#
# In order to enable or disable this script just change the execution
# bits.
#
# By default this script does nothing.

# Print the IP address
_IP=$(hostname -I) || true
if [ "$_IP" ]; then
  printf "My IP address is %s\n" "$_IP"
fi

#Run video on boot
cvlc {} &
exit 0
""".format(fileDir)
        file.write(data)
loadVideo("/home/pi/Desktop/ProyectoFinal/VIdeoIntro/logo2.mov")
    