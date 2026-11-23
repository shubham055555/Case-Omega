# CASE OMEGA
# DIGITAL FORENSIC INVESTIGATION REPORT

## Assignment 3 - Unit 3
### Investigation of Cyber Crimes

**Case:** Ransomware Attack on Healthcare Network

**Case ID:** OMEGA-001

**Investigator:** Student Investigator

**Date:** 23 November 2026

**Environment:** Fictional Hospital Network

**IMPORTANT:** This report describes a simulated academic investigation. All evidence, hosts, accounts and events are fictional.

---

# 1. EXECUTIVE SUMMARY

A simulated ransomware incident was investigated
in a fictional hospital network.

The investigation identified suspicious account
activity, unauthorized privilege changes,
suspicious process execution and persistence
through a service named UpdaterSvc.

The simulated logs also showed mass file
modification involving 1842 files and creation
of a ransom note named README_RECOVER.txt.

The incident is classified as high severity because
healthcare information systems may affect patient
care and hospital operations.

# 2. FIRST RESPONDER PROCEDURES

The following steps were documented:

1. Ensure patient and staff safety.
2. Inform the hospital IT security team.
3. Record incident details.
4. Secure the investigation scene.
5. Photograph relevant equipment.
6. Identify digital evidence.
7. Preserve volatile information where authorized.
8. Isolate affected systems safely.
9. Acquire forensic copies.
10. Calculate SHA-256 hashes.
11. Maintain Chain of Custody.
12. Prepare the investigation report.

Supporting file: reports/first_responder_sop.md

# 3. SCENE DOCUMENTATION

The fictional hospital network includes:

- WS-07: Suspected infected workstation
- HIS-SRV01: Hospital information server
- USB-TRAIN-004: Removable media
- Firewall: Network security component

The logical scene sketch is available at:

reports/scene_sketch.txt

# 4. EVIDENCE COLLECTION

The following simulated evidence was collected
for the classroom exercise:

| ID | Evidence | Source |
| E-01 | Authentication Log | HIS-SRV01 |
| E-02 | Endpoint Log | WS-07 |
| E-03 | Network Log | Firewall |

Evidence files:

- evidence/logs/authentication.log
- evidence/logs/endpoint.log
- evidence/logs/network.log

# 5. SHA-256 HASH VERIFICATION

SHA-256 was used to generate cryptographic
hashes of the three simulated evidence log files.

The hash manifest is stored at:

reports/hash_manifest.csv

Hash verification is used to detect changes
in evidence files.

No real server disk image was acquired.

# 6. CHAIN OF CUSTODY

A Chain of Custody record was prepared containing:

- Evidence identification
- Description
- Collection information
- Acquisition method
- SHA-256 hash
- Transfer information
- Remarks

Supporting file:

reports/chain_of_custody.csv

The recorded investigators and transfers
are simulated training entries.

# 7. MALWARE ANALYSIS

The simulated malware behavior was classified
as file-encrypting ransomware-like activity.

Observed indicators:

- Suspicious account: unknown-admin
- Suspicious process: remote_tool.exe
- Persistence service: UpdaterSvc
- Ransom note: README_RECOVER.txt
- File extension: .locked
- Mass file modification: 1842 files

Threat classification: HIGH

The exact malware family and encryption algorithm
cannot be confirmed without an actual sample.

# 8. INDICATORS OF COMPROMISE

The Python IOC detection program identified:

1. Suspicious Account
2. Persistence Service
3. Ransom Note
4. USB Device
5. Suspicious Process
6. Encrypted Extension
7. Suspicious IP
8. Associated malicious activity

The detector generated a CSV report:

reports/ioc_results.csv

198.51.100.24 is a reserved documentation IP
and must not be treated as a real attacker address.

# 9. ATTACK TIMELINE

The timeline was generated using Python by
correlating authentication, network and endpoint logs.

Important events:

08:40 - USB insertion
08:41 - Suspicious account login
08:42 - Suspicious process execution
08:43 - Privilege change
09:03 - Suspicious service creation
09:06 - Outbound connection blocked
09:22 - Mass file modification
09:24 - Ransom note creation

Complete timeline:

reports/attack_timeline.csv

# 10. APPLICABLE LEGAL PROVISIONS

Potentially applicable provisions in India include:

1. Information Technology Act, 2000,
   Section 43: Unauthorized access and damage
   to computer systems.

2. Information Technology Act, 2000,
   Section 66: Computer-related offences
   when statutory requirements are met.

3. Information Technology Act, 2000,
   Section 66C: Identity theft.

4. Information Technology Act, 2000,
   Section 66D: Cheating by personation
   using computer resources.

5. Bharatiya Nyaya Sanhita, 2023:
   Depending on established facts, provisions
   relating to cheating, extortion, forgery
   or criminal conspiracy may be examined.

The exact legal provisions depend on verified
facts and legal advice. For offences committed
in 2026, BNS rather than IPC is the current
general criminal code.

# 11. CYBERSECURITY RECOMMENDATIONS

1. Implement multi-factor authentication.
2. Use strong password policies.
3. Maintain regular offline backups.
4. Implement network segmentation.
5. Restrict unauthorized USB devices.
6. Monitor suspicious login activities.
7. Install endpoint detection solutions.
8. Regularly patch operating systems.
9. Restrict unnecessary RDP and SMB access.
10. Conduct employee cybersecurity training.
11. Monitor newly created services.
12. Test disaster recovery procedures.

# 12. TOOLS USED

- Visual Studio Code
- Python 3.11.9
- PowerShell
- SHA-256
- CSV
- Git and GitHub (planned repository workflow)

FTK Imager/dd acquisition was not performed.
No live ransomware was executed.

# 13. CONCLUSION

The simulated investigation demonstrates
how digital forensic techniques can be used
to investigate ransomware-like incidents.

The project covers evidence identification,
hash generation, integrity verification,
Chain of Custody, malware behavior analysis,
IOC detection and attack timeline generation.

It demonstrates the importance of preserving
digital evidence and maintaining proper
investigation documentation.

# 14. AUTHorship DECLARATION

This project is an academic simulation using
fictional evidence and training data.

Student Name: __________________

Roll Number: ___________________

Course: ________________________

Submission Date: _______________

The student should disclose assistance and
tools used according to institutional policy.
