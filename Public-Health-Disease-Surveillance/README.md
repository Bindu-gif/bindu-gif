
Sure! Here's the **full single-block version** of your `README.md` content. Just copy and paste it directly into your GitHub repository:

---

```markdown
# 🏥 Public Health Disease Surveillance Architecture Development Project

This project demonstrates a simulated public health emergency architecture for real-time disease surveillance using HL7 FHIR, OpenEMR, and HAPI-FHIR in a multi-hospital virtualized environment.

---

## 📌 Project Overview

The system was designed to enable seamless and secure interoperability among four hospitals and a Health Information Exchange (UPHIE). It focuses on detecting and monitoring communicable diseases in the Upper Peninsula of Michigan.

---

## 🖼️ Architecture Diagram

> ![Architecture Overview](./screenshots/architecture-diagram.png)

The architecture includes:
- **4 Hospital VMs** (Aspirus, Portage, BCMH, MGH)
- Each hospital uses **OpenEMR** with synthetic FHIR data
- A central **UPHIE intercept point (HAPI-FHIR Server)** receives FHIR bundles
- Data forwarded to:
  - State of Michigan HIE Proxy
  - MiHIN Shared Services
  - Google Looker Dashboard
  - WUPHD (Public Health Dashboard)

---

## ⚙️ Technology Stack

| Component                  | Details                                |
|---------------------------|----------------------------------------|
| OS                        | Ubuntu Server (20.04)                  |
| EHR System                | OpenEMR                                |
| Interoperability          | HL7 FHIR                               |
| API Testing               | Postman                                |
| Visualization             | Google Looker                          |
| HIE Server                | HAPI FHIR (Port 8090)                  |
| Security Tools            | UFW Firewall, Apache Config Headers    |

---

## 🛠️ Setup & Configuration

### ✅ Ubuntu Server Setup
```bash
sudo apt-get update && sudo apt-get upgrade
sudo apt-get install unattended-upgrades
sudo dpkg-reconfigure --priority=low unattended-upgrades
```

### 🔥 Firewall Configuration (UFW)
```bash
sudo apt-get install ufw
sudo ufw allow http
sudo ufw allow https
sudo ufw allow ssh
sudo ufw enable
```

### 🧱 Apache Security Hardening
```bash
sudo nano /etc/apache2/conf-available/security.conf
```

Add headers:
```
ServerTokens Prod
ServerSignature Off
TraceEnable Off
Header set X-Content-Type-Options: "nosniff"
Header set X-Frame-Options: "sameorigin"
Header set X-XSS-Protection: "1; mode=block"
```

Enable config:
```bash
sudo a2enconf security
sudo systemctl restart apache2
```

---

## 🧪 API Interactions via Postman

FHIR resource tested:
```http
POST http://localhost:8090/fhir/Practitioner
```

Sample JSON body:
```json
{
  "resourceType": "Practitioner",
  "id": "1",
  "meta": {
    "versionId": "1",
    "lastUpdated": "2025-03-25T19:42:11.552+00:00"
  },
  "identifier": [{
    "type": {"text": "NPI"},
    "value": "CWI234563"
  }]
}
```

Response:
```
201 Created ✅
```

---

## 🔐 Security Concerns Identified

Despite hardening, OpenEMR is still susceptible to:
- **SQL Injection (SQLi)**
- **Cross-Site Scripting (XSS)**
- **Cross-Site Request Forgery (CSRF)**
- **Privilege Escalation**
- **Insider Threats**

---

## 🙋‍♀️ Personal Contributions

- Installed OpenEMR on 4 VMs
- Enabled FHIR data generation
- Configured security settings (firewall & Apache)
- Deployed Postman APIs to test HAPI-FHIR server
- Managed data flow simulation to UPHIE and Looker

---

## 📂 Files Included

- `/screenshots/` – VM and Postman output
- `architecture-diagram.png`
- `openemr_install_guide.md`
- `postman_test_result.json`
- `README.md` (this file)

---

## 📅 Timeline

- Configuration & Testing: Feb–Mar 2025  
- Final Submission: April 18, 2025

---

## 📬 Contact

**Bindu Mamillapalli**  
Master's in Health Informatics  
Michigan Technological University
``
