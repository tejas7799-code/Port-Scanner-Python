import socket


def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)

        result = sock.connect_ex((target, port))
        sock.close()

        return result == 0

    except socket.error:
        return False


print("=" * 50)
print("          PYTHON PORT SCANNER")
print("=" * 50)

target = input("Enter target hostname or IP address: ")

try:
    target_ip = socket.gethostbyname(target)

    print("\nTarget:", target)
    print("IP Address:", target_ip)

    start_port = int(input("Enter starting port: "))
    end_port = int(input("Enter ending port: "))

    if start_port < 1 or end_port > 65535 or start_port > end_port:
        print("\nInvalid port range.")
    else:
        print("\nScanning ports...")
        print("-" * 50)

        open_ports = []

        for port in range(start_port, end_port + 1):
            if scan_port(target_ip, port):
                print(f"Port {port}: OPEN")
                open_ports.append(port)

        print("-" * 50)

        if open_ports:
            print("Open ports found:", open_ports)
        else:
            print("No open ports found in the selected range.")

except socket.gaierror:
    print("\nError: Could not resolve the hostname.")

except ValueError:
    print("\nError: Please enter valid port numbers.")

print("=" * 50)
print("Port scanning completed.")
print("=" * 50)
