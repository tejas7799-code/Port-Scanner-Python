# Port Scanner (Python)

## Intern Details

| Field | Details |
|---|---|
| **Intern ID** | CITS8842 |
| **Full Name** | KOLA TEJAS |
| **No. of Weeks** | 8 Weeks |
| **Project Name** | Port Scanner (Python) |
| **Project Scope** | A basic Python-based network security tool that checks the availability of TCP ports on an authorized target and identifies open ports. |

---

## Project Overview

Port Scanner (Python) is a basic cybersecurity project developed using Python.

The application checks a selected range of TCP ports on a target hostname or IP address and identifies which ports are accepting connections.

This project demonstrates basic networking concepts, socket programming, and port scanning techniques.

---

## Objectives

The main objectives of this project are:

- To understand basic computer networking concepts.
- To understand TCP ports and their purpose.
- To identify open TCP ports on an authorized system.
- To demonstrate Python socket programming.
- To provide a simple cybersecurity scanning tool.
- To understand how network services can be detected through port availability.

---

## Features

- Hostname and IP address support.
- TCP port scanning.
- Custom starting port.
- Custom ending port.
- Open port detection.
- Simple command-line interface.
- Error handling for invalid hostnames and port numbers.
- No external Python packages required.

---

## Technologies Used

- **Python 3**
- **Socket Programming**
- **TCP/IP Networking**
- **GitHub**

The project uses Python's built-in `socket` module and does not require external Python packages.

---

## How the Program Works

1. The user enters a hostname or IP address.
2. The program resolves the hostname into an IP address.
3. The user enters a starting port.
4. The user enters an ending port.
5. The program attempts a TCP connection to each port in the selected range.
6. If a connection is successful, the port is reported as **OPEN**.
7. After scanning, the program displays the list of detected open ports.

---

## How to Run

### Option 1: Run on Your Computer

1. Install Python 3.x.
2. Download or clone this repository.
3. Open a terminal or command prompt inside the project folder.
4. Run:

### Option 2: Run Using an Online Python Compiler

The project can also be tested using an online Python compiler that supports Python socket operations.

#### Steps:

1. Open an online Python compiler such as **Programiz, OnlineGDB, or Replit**.
2. Open `port_scanner.py` from this GitHub repository.
3. Copy the complete Python source code.
4. Paste the code into the online Python editor.
5. Click the **Run** button.
6. Enter an authorized target hostname or IP address.
7. Enter the starting and ending port numbers.
8. The program will display the open ports detected within the selected range.

No external packages need to be installed because the project uses Python's built-in `socket` module.

> **Note:** Some online Python environments may restrict network socket connections. If the scanner does not work online, run the program locally using Python.

Example output:
==================================================
          PYTHON PORT SCANNER
==================================================
Enter target hostname or IP address: 127.0.0.1

Target: 127.0.0.1
IP Address: 127.0.0.1
Enter starting port: 1
Enter ending port: 100

Scanning ports...
--------------------------------------------------
Port 22: OPEN
--------------------------------------------------
Open ports found: [22]
==================================================
Port scanning completed.
==================================================


```bash
python port_scanner.py
