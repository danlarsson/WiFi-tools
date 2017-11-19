#!/usr/bin/python

###
#
# Scan WiFi network for Probe Requests from Clients. Store the SSID and client MAC-adress in a list.
#
# ToDo: 
# - Get Keyboard interuppt to work
# - Show toplist of mostly found/used SSID
# - Just show SSID from open networks?!?
# - Commandline code, record/show toplist, choose filename / just list, no record?
#
###
import pyshark

WiFi_card = 'en0'
FileName = 'probe_ssid_unique.txt'

def main():
    # Subtype 4 = Probe Request
    capture = pyshark.LiveCapture(WiFi_card, display_filter='wlan.fcs.status eq 1 && wlan.fc.type_subtype eq 4 && !wlan.tag.length eq 0', monitor_mode=True)
    lista = open_file()
    fp = open(FileName, 'a')

    print ('Looking for new SSID not in: ' + FileName)

    try: 
        for packet in capture.sniff_continuously():
            tmp = packet.__dict__
            ssid_name = (tmp['layers'][3].get_field_value("ssid"))
            ta_address = (tmp['layers'][2].get_field_value("ta"))
            if ssid_name+ta_address not in lista:
                lista.append(ssid_name+ta_address)
                print ssid_name + ' ' + ta_address
                fp.write(ssid_name + ta_address + '\n')
    except:
        print('Goodby')
        exit()


def open_file():
    try:
        fp = open(FileName, 'r')
        x = fp.read().splitlines()
        fp.close()
        return x
    except:
        return []


if __name__ == '__main__':
    main()
