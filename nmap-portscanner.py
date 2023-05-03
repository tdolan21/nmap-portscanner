import nmap

def main():
    nm = nmap.PortScanner()

    # Define the target host and port range to scan
    target_host = 'scanme.nmap.org'
    target_ports = '22-80'

    print(f'Scanning {target_host} for open ports in the range {target_ports}...')

    # Perform the scan
    nm.scan(target_host, target_ports)

    # Print the scan results
    for host in nm.all_hosts():
        print(f'Host: {host} ({nm[host].hostname()})')
        print('State: ' + nm[host].state())

        for proto in nm[host].all_protocols():
            print(f'Protocol: {proto}')
            ports = nm[host][proto].keys()
            for port in ports:
                print(f'Port: {port}, State: {nm[host][proto][port]["state"]}')

if __name__ == "__main__":
    main()
