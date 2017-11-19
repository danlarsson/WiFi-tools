'''
Show the number of retrys on a specific channel

Listen to all traffic
Count packets / wlan.fc.retry == 1
Show % of number of retry vs packets.

'''
import pyshark

BSSID = ''

# Get beacon frames with correct checksum for transmitter address...
capture_filter = 'wlan.fcs.status == 1'
capture = pyshark.LiveCapture('en0', display_filter=capture_filter, monitor_mode=True)

a = 1
packets = 1
packets100 = 1
retrys = 1
retrys100 = 1

for packet in capture.sniff_continuously():
    tmp = packet.__dict__
    # fields = tmp['layers'][2].__dict__
    retry = int(tmp['layers'][2].get_field_value('wlan.fc.retry'))
    channel = int(tmp['layers'][1].get_field_value('channel'))

    if a == 1:
        print 'Capturing on channel: %i' % channel

    elif a % 100 == 0:
        print 'Packets: %i, Retrys: %i, Persentage: %.2f%% (%.2f%%)' % \
              (packets, retrys, (float(retrys) / packets) * 100,
              (float(retrys100) / packets100) * 100)
        packets100 = 1
        retrys100 = 1

    if retry == 1:
        retrys += 1
        retrys100 += 1

    else:
        packets += 1
        packets100 += 1

    a += 1
    if a >= 10000:
        exit()

