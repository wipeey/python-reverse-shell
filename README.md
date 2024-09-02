# Python Reverse Shell

---

## Background

Just a simple python reverse shell I developped to work some fundamentals. I'll keep improving it whenever I get some free time.
Do not hesitate to check the code as I tried to comment it as much as possible so that everyone can try and understand how it works.

---

## Usage

The attacker needs to setup a listener on a specific port (e.g., 4444, 8080). To do this, use the following command: `nc -lvnp <PORT>`
Replace <PORT> with a forwarded port. The target machine must then execute the `client.py` to establish a connection back to the attacker.
Once connected, the attacker will have shell access to the target machine.

---

## Technicalities

ATTACKER ➜ The attacker must forward a valid port if he's trying to attack a machine outside of his local network.
TARGET ➜ This script was built using Python 3.12. The target must have a valid Python version and the required packages installed.

---

## Ethical Considerations

This project is just a way for me and hopefully others to gain experience in cybersecurity.
Please do not use this script to perform any malicious activities!

---

### 📨 Contact me on Discord → sctwck
