# TCP Attacks Lab

## Overview
This project is part of the SEED Labs and focuses on understanding and implementing various TCP-based attacks. The primary goal is to demonstrate vulnerabilities in the TCP protocol through hands-on experience with SYN Flooding, TCP RST attacks, TCP Session Hijacking, and creating a Reverse Shell using TCP Session Hijacking.

## Tasks and Learnings

### 1. SYN Flooding Attack
- **Objective:** Conduct a SYN Flooding attack to understand how a Denial of Service (DoS) can be performed by exhausting the connection queue of a target server.
- **Key Learnings:**
  - **Mechanism:** Attackers send numerous SYN requests without completing the handshake, filling up the connection queue.
  - **Countermeasure:** The use of SYN cookies helps mitigate this attack.
- **Execution:** 
  - Disabled SYN cookies and observed connection failures during the attack.
  - Enabled SYN cookies and confirmed successful connections despite the attack.

### 2. TCP RST Attacks on Telnet Connections
- **Objective:** Perform a TCP RST attack to terminate an existing telnet connection.
- **Key Learnings:**
  - **Mechanism:** Send spoofed TCP RST packets to disrupt an active connection.
- **Execution:**
  - Used Scapy to craft and send TCP RST packets.
  - Observed successful termination of telnet sessions using Wireshark.

### 3. TCP Session Hijacking
- **Objective:** Hijack an existing TCP session and inject malicious commands.
- **Key Learnings:**
  - **Mechanism:** Inject packets into an established TCP session to take control of the session.
- **Execution:**
  - Crafted and sent packets with Scapy to inject commands.
  - Verified hijack success by creating a test file on the victim machine.

### 4. Creating Reverse Shell using TCP Session Hijacking
- **Objective:** Establish a reverse shell on the victim’s machine via session hijacking.
- **Key Learnings:**
  - **Mechanism:** Execute a command that initiates a reverse shell connection back to the attacker's machine.
- **Execution:**
  - Injected a reverse shell command through a hijacked session.
  - Confirmed control by interacting with the victim’s machine through the reverse shell.

## Additional Notes
- **Tools Used:** Docker for environment setup, Scapy for packet crafting, Wireshark for network traffic analysis.

## Conclusion
This lab provides practical insights into TCP vulnerabilities and their exploitation. It highlights the importance of understanding network security mechanisms and countermeasures to protect against such attacks.

## Usage
To replicate the tasks:
1. Set up the environment using the provided Docker setup files.
2. Follow the instructions in each task to perform and observe the attacks.
3. Utilize Wireshark to monitor network traffic and verify the success of each attack.

For detailed instructions, refer to the lab documentation linked [here](https://seedsecuritylabs.org/Labs_20.04/Files/TCP_Attacks/TCP_Attacks.pdf).

---

Feel free to clone this repository and explore the provided scripts to gain a deeper understanding of TCP attacks and their mitigations.
