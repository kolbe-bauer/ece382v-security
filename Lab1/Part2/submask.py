from ipwhois import IPWhois
def main():
    target_ips = []
    with open("Port80Results.csv") as f:
        [target_ips.append(line.strip()) for line in f.readlines()]
    subnets = {}
    for i in range(37620):
        if (i % 3700 == 0):
            print(f"Currently on line number: '{i}'\n")
        ip = target_ips[i]
        try:
            obj = IPWhois(ip)
            ret = obj.lookup_whois()
            # print(ret)
            if ret.get('asn_cidr'):
                cidr = ret.get('asn_cidr')
            if subnets.get(cidr):
                subnets[cidr].add(ip)
            else:
                subnets[cidr] = {ip}
        except:
            print("Exception Occurred")
    with open('NetworkResults.csv','w') as file:
        file.write(f"Number of Networks, '{len(subnets)}'\n")
        file.write(f"Ip Address, Number of IPs, Number of Machines Probed\n")
        for cidr in subnets:
            probed = subnets[cidr]
            ips = 2**(32 - int(cidr.split('/')[1]))
            file.write(f"'{cidr}','{ips}','{len(probed)}'\n")
    # print(f"Number of Networks: '{len(subnets)}'")
    # for cidr in subnets:
    #     probed = subnets[cidr]
    #     ips = 2**(32 - int(cidr.split('/')[1]))
    #     print(f"IP Address: '{cidr}'\tNumber of IPs: '{ips}'\tNumber of machines probed: '{len(probed)}'")

if __name__ == "__main__":
    main()

# sudo zmap -p 80 -b blacklist.txt -o Port80Results -t 7200
# sudo zmap -p 80 -w whitelist.txt -o Port82Results -t 600
# sudo zmap -p 22 -w whitelist.txt -o Port22Results -t 600
# sudo zmap -p 433 -w whitelist.txt -o Port433Results -t 600