
# 🏥 Public Health Disease Surveillance Architecture Development Project

This project simulates a real-world public health emergency surveillance system using **OpenEMR**, **FHIR standards**, **HAPI-FHIR server**, and virtualized Ubuntu environments. It demonstrates how health data can be captured at multiple hospitals, routed through a regional Health Information Exchange (UPHIE), and used by state and public health entities for **real-time outbreak detection and monitoring**.

> 📌 Final Project for SAT 5424 – Population and Public Health Informatics  
> 🎓 Michigan Technological University | April 2025

---

## 🧭 Project Goals

- Implement a **multi-hospital health data flow system** using open-source EHRs (OpenEMR)
- Enable secure data interoperability using **HL7 FHIR standards**
- Route synthetic health data to a regional **HAPI-FHIR intercept point**
- Visualize data via **dashboards (e.g., Google Looker)**
- Simulate real-world public health architecture for early disease surveillance

---

## 🖼️ System Architecture Diagram

> 📌 This diagram visualizes the simulated public health ecosystem connecting hospitals, UPHIE, and analytics/reporting tools.

![Architecture Diagram](./screenshots/architecture-diagram.png)

---

## 🏗️ System Components

| Layer                          | Component                            | Purpose                                                                 |
|-------------------------------|--------------------------------------|-------------------------------------------------------------------------|
| 🏥 Hospitals (x4)              | OpenEMR on Ubuntu                    | Generates patient-level synthetic health records in FHIR format        |
| 🔁 Middleware (UPHIE)         | HAPI-FHIR Server (port 8090)         | Receives FHIR bundles, acts as data exchange hub                       |
| 📊 Visualization               | Google Looker Dashboard              | Displays anonymized health trends to WUPHD and public stakeholders     |
| 🛡️ State Connectivity         | MiHIN & Michigan State HIE Proxy     | Simulates health data submission to statewide authorities              |

---

## ⚙️ Technical Stack

| Area                 | Technology Used                      |
|----------------------|--------------------------------------|
| Operating System     | Ubuntu 20.04 Server (VirtualBox VMs) |
| EHR Platform         | OpenEMR                              |
| Interoperability     | HL7 FHIR v4.0.1                      |
| API Server           | HAPI-FHIR (localhost:8090/fhir)      |
| Network Security     | UFW Firewall, Apache Hardening       |
| API Testing          | Postman                              |
| Data Source          | Synthetic FHIR data from Synthea     |

---

## 🛠️ System Configuration Details

### 🔧 Ubuntu Update & Security Setup

```bash
sudo apt-get update && sudo apt-get upgrade
sudo apt-get install unattended-upgrades
sudo dpkg-reconfigure --priority=low unattended-upgrades
```

### 🔥 UFW Firewall Rules

```bash
sudo ufw allow http
sudo ufw allow https
sudo ufw allow ssh
sudo ufw enable
```

### 🧱 Apache Security Headers

```bash
sudo nano /etc/apache2/conf-available/security.conf
```

Set headers:
```
ServerTokens Prod
Header set X-Content-Type-Options: "nosniff"
Header set X-Frame-Options: "sameorigin"
Header set X-XSS-Protection: "1; mode=block"
```

Restart Apache:
```bash
sudo a2enconf security
sudo systemctl restart apache2
```

---

## 🧪 API Example via Postman

### ➕ Creating a Practitioner Resource

```http
POST http://localhost:8090/fhir/Practitioner
```

**Payload**:
```json
{
  "resourceType": "Practitioner",
  "id": "1",
  "identifier": [{
    "type": {"text": "NPI"},
    "value": "CWI234563"
  }]
}
```

**Response**:
```
201 Created ✅
```

---

## 🔐 Cybersecurity Considerations

Even with hardened Apache and firewalls, OpenEMR remains exposed to:

- **SQL Injection (SQLi)**
- **Cross-Site Scripting (XSS)**
- **Cross-Site Request Forgery (CSRF)**
- **API vulnerabilities**
- **Insider threats** without strict role-based access controls

---

## 🖥️ VM Configuration & Screenshots

The following screenshots demonstrate real-time configuration and testing from the four virtual machines:

### 🏥 Hospital VM 1 – Ubuntu Server Installation
![VM 1](./screenshots/vm-diagram-1.png)

### 🏥 Hospital VM 2 – OpenEMR Login and Access
![VM 2](./screenshots/vm-diagram-2.png)

### 🔐 Firewall and Apache Security Configuration
![Firewall](./screenshots/vm-diagram-3.png)

### 🧪 FHIR API Testing using Postman
![Postman](./screenshots/vm-diagram-4.png)

---

## 📊 Project Outcome

- Simulated a **regional EHR data ecosystem**
- Successfully routed data from **4 hospital VMs → UPHIE → dashboards**
- Demonstrated use of **FHIR APIs for public health data sharing**
- Applied **network and application-level security measures**

---

## 🙋‍♀️ Personal Contribution – Bindu Mamillapalli

- Installed and configured OpenEMR on 4 virtual machines
- Secured Ubuntu servers with firewall & Apache headers
- Enabled FHIR output and tested endpoints via Postman
- Managed architecture setup, testing, and documentation
- Ensured alignment with public health surveillance goals

---

## 📁 Files Included in Repo

| File/Folder                     | Description                                        |
|--------------------------------|----------------------------------------------------|
| `/screenshots/architecture-diagram.png` | High-resolution architecture diagram       |
| `/screenshots/vm-diagram-1.png` to `vm-diagram-4.png` | Configuration & testing screenshots |
| `README.md`                    | Full documentation of this project                |

---

## 🎓 Course Info

**Course**: SAT 5424 – Population and Public Health Informatics  
**Institution**: Michigan Technological University  
**Final Submission**: April 18, 2025

---

## ✅ Final Takeaway

> This project demonstrates how low-cost, open-source solutions can simulate powerful **public health informatics infrastructure** for real-time disease surveillance. It integrates modern data standards (FHIR), robust APIs (HAPI-FHIR), and strong cybersecurity configurations — making it a valuable prototype for local health departments and global health systems alike.
