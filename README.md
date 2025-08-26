# Network Traffic Monitoring and Classification

**Project Title:** An Efficient Traffic Monitoring and Identification Based on Categorization in Internet Access  
**Authors:** Saachi Jaiswal & Team  
**Guide:** Dr. S.A. Kalaiselvan  
**Institute:** TKR College of Engineering & Technology  

---

## 📖 Overview
This project presents a **Python-based network traffic classifier** that monitors packets in real time and categorizes them into groups like:
- General
- OTT (YouTube, Netflix, Prime, etc.)
- News
- Games
- Educational
- Explicit

Traffic is captured using **scapy**, processed with **pandas/SciPy**, and visualized via **matplotlib**. UDP/TCP packets are inspected, logged, and analyzed. Results show real-time classification and frequency bar charts.  [oai_citation:7‡Saachi Final Document .pdf](file-service://file-A7EVcTgvwR6L9fbR4MxLFv)

---

## 📂 Repository Contents
- `code/` → `file_mon.py`, `intercept.py`
- `scripts/` → Windows helpers `run.bat`, `start.bat`
- `requirements.txt` → Python deps
- `docs/` → Final report, literature survey, slides
- `video/` → Demo (`PACKET_CLASSIFICATION_2.mp4`)

## Setup
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
pip install -r requirements.txt


⸻

📺 Demo

A demo of real-time packet classification is available:
👉 video/PACKET_CLASSIFICATION_2.mp4

⸻

⚠️ Notes
	•	Packet capture may require admin/root privileges.
	•	If you see missing-module errors, add them to requirements.txt and re-install.

⸻

📚 Citation

If you reference this project, please cite:

Jaiswal, S. An Efficient Traffic Monitoring and Identification Based on Categorization in Internet Access.
B.Tech Final Project, TKR College of Engineering & Technology, 2022.
