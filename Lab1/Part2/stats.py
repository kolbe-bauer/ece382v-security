from ipwhois import IPWhois
def main():
    port_80s = []
    with open("Port22Results") as f:
        [port_80s.append(line.strip()) for line in f.readlines()]
    port_22s = []
    with open("Port22Results.csv") as f:
        [port_22s.append(line.strip()) for line in f.readlines()]
    port_433 = []
    with open("Port433Results.csv") as f:
        [port_433.append(line.strip()) for line in f.readlines()]
   
    with open('DeepDiveResults.csv','w') as file:
        file.write(f"Number of IPs with Port 80,'{len(port_80s)}'\n")
        file.write(f"Number of IPs with Port 22,'{len(port_22s)}'\n")
        file.write(f"Number of IPs with Port 433,'{len(port_433)}'\n\n")
        a = set()
        for ip in port_80s:
            a.add(ip)
        b = set()
        ab = set()
        for ip in port_22s:
            if {ip}.issubset(a):
                ab.add(ip)
            b.add(ip)
        c = set()
        ac = set()
        bc = set()
        abc = set()
        for ip in port_433:
            if {ip}.issubset(a):
                ac.add(ip)
                if {ip}.issubset(b):
                    abc.add(ip)
            if {ip}.issubset(b):
                bc.add(ip)
            c.add(ip)
        file.write(f"Number of Devices with Ports 80 and 22 open,'{len(ab)}'\n")
        file.write(f"Number of Devices with Ports 80 and 433 open,'{len(ac)}'\n")
        file.write(f"Number of Devices with Ports 22 and 433 open,'{len(bc)}'\n")
        file.write(f"Number of Devices with Ports 80, 22, and 433 open,'{len(abc)}'\n")
                

if __name__ == "__main__":
    main()