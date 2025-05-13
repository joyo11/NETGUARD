# 🛡️ NetGuard
**Monitor Packets. Debug Smarter.**

NetGuard is a lightweight, Dockerized network traffic monitoring tool built with Python and [Scapy](https://scapy.readthedocs.io/). It allows you to inspect live packets from your host machine for debugging, research, or security analysis. Designed for developers, security enthusiasts, and network engineers, NetGuard runs directly inside a container — no local Python setup required.

---

## ✨ Features

### ✅ Current Features
- **Live Packet Sniffing**: Uses Scapy to monitor real-time network traffic
- **Dockerized**: Clean environment — no host setup or pip installs
- **Minimal & Lightweight**: Just clone and run
- **Host-Level Access**: Use with `--net=host` and `--privileged` for full visibility

### 🚧 In Development
- Protocol filtering (HTTP, DNS, etc.)
- Packet logging to file (CSV/JSON)
- Real-time Flask web dashboard
- Alerts for suspicious activity

## 🔮 Future Acknowledgments

This section is reserved to recognize future contributors who help enhance NetGuard. We look forward to acknowledging:

- Developers who contribute new features, improvements, or fixes
- Security researchers who provide feedback from real-world use
- Collaborators who assist in building the planned web dashboard
- Community members who improve documentation or platform support

---

## 🐳 Installation

### 1. Clone the repository
```bash
git clone https://github.com/joyo11/NetGuard.git
cd NetGuard

2. Build the Docker image

docker build -t netguard .


3. Run the container
To allow full packet capture, run with --net=host and --privileged:

docker run --rm -it --net=host --privileged netguard
```


## Requirements
Docker installed on host machine

Linux recommended for --net=host mode compatibility

Root or sudo privileges to grant packet capture access

📜 License
This project is licensed under the MIT License. See the LICENSE file for details.

📬 Contact
Created by Mohammad Shafay Joyo
For questions or suggestions, feel free to open an issue or reach out!