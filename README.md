# 🌐 Network Traffic Monitoring & Classification

Real-time packet capture and categorization (General, OTT, News, Games, Education, Explicit) using Python.  
Includes a short demo video.

---

## 📂 Repository Contents
- `code/` → `file_mon.py`, `intercept.py`
- `scripts/` → Windows helper scripts (`run.bat`, `start.bat`)
- `requirements.txt` → Python dependencies
- `docs/` → Final report, literature survey, presentation slides
- `video/` → Demo (`PACKET_CLASSIFICATION_2.mp4`)

---

## 🛠️ Setup
Create and activate a virtual environment, then install dependencies:

python -m venv .venv  
Windows: .venv\Scripts\activate  
macOS/Linux: source .venv/bin/activate  
pip install -r requirements.txt  

---

## ▶️ Run
Windows (Admin cmd/PowerShell):  
scripts\start.bat  
or  
python code\intercept.py  

macOS/Linux (may need sudo for sniffing):  
sudo python code/intercept.py  

---

## 📺 Demo
A demo of real-time packet classification is available:  
👉 video/PACKET_CLASSIFICATION_2.mp4  

---

## ⚠️ Notes
- Packet capture may require **admin/root privileges**.  
- If you see missing-module errors, add them to requirements.txt and re-install.  

---

## 📚 Citation
If you reference this project, please cite:

Jaiswal, S. *An Efficient Traffic Monitoring and Identification Based on Categorization in Internet Access*.  
B.Tech Final Project, TKR College of Engineering & Technology, 2022.  

BibTeX:

@report{Jaiswal_TrafficClassification_2022,  
  title   = {An Efficient Traffic Monitoring and Identification Based on Categorization in Internet Access},  
  author  = {Saachi Jaiswal},  
  year    = {2022},  
  institution = {TKR College of Engineering & Technology},  
  note    = {B.Tech Final Project}  
}
