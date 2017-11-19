# WiFi-tools
Some small WiFi-tools coded in Python and uses the pyshark plugin. Pyshark uses tshark from Wireshark and 
has the same sort of filters that are used in Wireshark. 

That is, for this to work you need to install both tshark, that comes with Wireshark and pyshark.
You also need to have a WiFi-adapter that supports monitor-mode to capture the packets. 
I have run the scripts on a MacBook with the internal WiFi card, and on a Linux computer (Odroid)
with a USB-WiFi-adapter that i don't know the model of

For more information on Pyshark 
https://kiminewt.github.io/pyshark/

To install pyshark just use pip: `pip install pyshark`


## number-of-retrys.py
Looks at a specific WiFi channel for WiFi-packets with or without the retry flag set. And shows the percentage of packets.
 Good to use to se if there is a lot of resend on the network, could be interference or that the stations don't hear
 each other.

In the next version (maybe) could show a list of STA-AP that shows retrys and not a whole channel or that you can specify
  a specific BSSID or ClientMAC to listen for.

## ssid-strength-meter.py
Show the average signal strength for a specific BSSID. Looks att RSSI on Beacon frames. 
You have to set the BSSID in the script. The plan is to use the cript to 
measure wall dampening, to do a reading on each side of a wall and se the difference.


## unique-probe-requests.py
This script shows uniqe probe becons from clients. A client that are not connected to a WiFi-network sends probe-becons
 with the name of SSIDs it has been connected to before. The script listens for them and saves the SSID+ClientMAC to a file
 and displays new unique SSIDs. Unfortunately most clients today do a random MAC-adress for probe-requests, that makes 
 it hard for the script to se real unique SSIDn. 
 
 The script is most useful at places with many clients, for example a Airport or a public Café. Where lot of clients pass 
 that are not connected to a WiFi-network.
 
 The toplist of my most found SSIDs: homerun1x ; Telia wifi1x ; **Airport-Guest** ; **SJ** ; **WiFi Hotel Palacio** ;
  _VINCI Airports wifi ; **Radisson_Guest** ; **eduroam** ; Telia wifi ; testos ; **All Station Guests** ; 
  Coopers_WiFi ; AD-team

