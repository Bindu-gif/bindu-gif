# 🏥 Public Health Emergency Architecture  
## Use Case: Communicable Disease Surveillance

This project showcases the design of a standards-based architecture for **communicable disease surveillance**, enabling real-time data collection and integration from multiple healthcare facilities across Michigan’s Upper Peninsula. The architecture leverages **FHIR interoperability**, **HAPI FHIR servers**, **OpenEMR**, and **Google Cloud Looker** dashboards to empower local public health units with timely and geotagged outbreak information.

---

## 🎯 Project Objectives

- Integrate Electronic Health Records (EHRs) from different hospitals using HL7 message standards.
- Convert HL7 messages to **FHIR** (Fast Healthcare Interoperability Resources) using HAPI-FHIR servers.
- Enable centralized **Health Information Exchange (HIE)** with secure access for state repositories and MiHIN (Michigan Health Information Network).
- Create a **customizable dashboard** for real-time communicable disease tracking using Google Looker.
- Empower **Western Upper Peninsula Health Department (WUPHD)** and public users with actionable insights.

---

## 📁 Components

- **Hospitals' Raw HL7 Messages** → Simulated using OpenEMR
- **FHIR Transformation Layer** → HAPI-FHIR server
- **HIE Intercept Point** → Aggregates data from all participating hospitals
- **State and MiHIN Integration** → Transmits structured FHIR data to regulatory systems
- **Visualization Layer** → Real-time dashboards powered by Looker, displaying geotagged public health data

---

## ⚙️ Technologies & Standards

| Component | Description |
|----------|-------------|
| **HL7 v2 Messages** | Health Level 7 standard used for transmitting hospital data |
| **FHIR** | Fast Healthcare Interoperability Resources – Modern standard for healthcare data exchange |
| **OpenEMR** | Open-source EHR software used to simulate data from each hospital |
| **HAPI FHIR Server** | Java-based FHIR implementation used to intercept and standardize incoming data |
| **Google Looker** | Business intelligence platform used to build outbreak dashboards |
| **MiHIN** | Michigan's official health information network for sharing FHIR data across the state |

---

## 💡 Outcomes

- Real-time surveillance of outbreaks through FHIR-converted hospital data  
- Integration of four simulated hospitals to a centralized intercept point  
- Secure transfer of public health data to MiHIN and the State of Michigan Repository  
- Custom dashboards for WUPHD and public access via Google Cloud  
- Demonstrated end-to-end interoperability in a real-world public health context  

---

## 🙋‍♀️ Personal Contribution

As part of my **Master’s in Health Informatics**, I was involved in:

- Mapping HL7 messages to FHIR standards using HAPI server tools  
- Planning cloud integration and dashboard development using Looker  
- Documenting public health data flows and system interactions  
- Conducting research on legal and technical aspects of health data interoperability  
- Aligning system design with CDC recommendations for outbreak reporting

---

## 📚 References

- HL7 International. (2023). *Health Level Seven Standards.* Retrieved from https://www.hl7.org/  
- HL7 FHIR. (2024). *Fast Healthcare Interoperability Resources.* https://www.hl7.org/fhir/  
- OpenEMR Project. (2023). *Open-source electronic health record platform.* https://www.open-emr.org/  
- HAPI FHIR. (2023). *FHIR server for Java developers.* https://hapifhir.io/  
- Google Looker. (2024). *Modern data analytics & visualization platform.* https://cloud.google.com/looker  
- MiHIN. (2024). *Michigan Health Information Network Shared Services.* https://mihin.org/  
- Centers for Disease Control and Prevention (CDC). (2023). *Public Health Surveillance Systems.* https://www.cdc.gov/surveillance/

---

👩‍⚕️ **Developed by Bindu Mamillapalli**  
🎓 *Master’s in Health Informatics – Michigan Technological University*

