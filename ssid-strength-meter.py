'''
Messure the signal strength of a specific BSSID and present the MIN, MAX and AVERAGE values.

SA3ARK, 2017-11-06
'''
import pyshark

#sudo tcpdump  -I -i enX -p
#sudo killall airportd

# ToDo: Set channel to capture on
# CHANNEL = 1
BSSID = '30:85:a9:6a:0a:df'
NR_OF_MESSUREMENTS = 200
SHOW_EVERY = 10

# Get beacon frames with correct checksum for transmitter address...
capture_filter = 'wlan.fc.type_subtype eq 8 && wlan.sa == ' + BSSID + ' && wlan.fcs.status == 1'
capture = pyshark.LiveCapture('en0', display_filter=capture_filter, monitor_mode=True)

start_ssid = ''
start_mac = ''
start_channel = 0
signal_values = []
head = False
force_result = True

for packet in capture.sniff_continuously():
    tmp = packet.__dict__
    wlan =  tmp['layers'][1]
    signal = int(tmp['layers'][1].get_field_value('signal_dbm'))
    channel = int(tmp['layers'][1].get_field_value('channel'))
    mac_address = (tmp['layers'][2].get_field_value("ta"))
    ssid_name = (tmp['layers'][3].get_field_value("ssid"))

    if mac_address != start_mac:
        print 'BSSID: %s' %  mac_address
        start_mac = mac_address
        head = True

    if ssid_name != start_ssid:
        print 'SSID: %s ' % ssid_name
        start_ssid = ssid_name
        head = True

    if channel != start_channel:
        print 'Channel: %i' % channel
        start_channel = channel
        head = True

    if NR_OF_MESSUREMENTS-1 <= len(signal_values):
        force_result = True
        head = True

    if head:
        print
        print 'Nr     Signal   MAX    MIN   AVG'
        head = False

    signal_values.append(signal)
    average = sum(signal_values)/len(signal_values)
    if len(signal_values)%SHOW_EVERY == 0 or force_result:
        print '%-6s %s      %s    %s    %i' % (len(signal_values), signal, min(signal_values), max(signal_values), average)
        force_result = False

    if NR_OF_MESSUREMENTS <= len(signal_values):
        exit()
