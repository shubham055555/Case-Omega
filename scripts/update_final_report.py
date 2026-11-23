# -*- coding: utf-8 -*-
from pathlib import Path

p = Path("reports/final_forensic_report.md")
s = p.read_text(encoding="utf-8")

section = """
# 13. DISK IMAGE ACQUISITION AND INTEGRITY VERIFICATION

## 13.1 Evidence Details

Evidence ID: E-04
File: case_omega_simulated.dd
Type: Synthetic raw training image
Size: 8,388,608 bytes (8 MB)
Location: evidence/images/case_omega_simulated.dd

## 13.2 Image Generation Method

A synthetic raw image was generated using Python 3.11.
Script: scripts/create_simulated_image.py

This was a training simulation, NOT a bit-for-bit acquisition
from an actual hospital computer, server or physical disk.

## 13.3 SHA-256 Integrity Verification

Algorithm: SHA-256

Hash:
2E49B4F51B8682DCC2A870EAFCAE3A71250B3B8921BE27C9171E092FFA1A1551

Result: PASS

The independently calculated SHA-256 hash matched the recorded hash.

## 13.4 Chain of Custody

Evidence E-04 was added to reports/chain_of_custody.csv.
Its synthetic origin, generation method and hash are documented.

## 13.5 Limitations

This image is synthetic training evidence, not a real hospital disk.
No physical hospital disk acquisition or real patient data access
was performed.

"""

if "# 13. DISK IMAGE ACQUISITION AND INTEGRITY VERIFICATION" not in s:
    marker = "# 13. CONCLUSION"
    if marker not in s:
        raise SystemExit("Conclusion heading not found. Report unchanged.")
    s = s.replace(marker, section + "# 14. CONCLUSION", 1)
    s = s.replace("# 14. AUTHorship DECLARATION",
                  "# 15. AUTHORSHIP DECLARATION", 1)

s = s.replace(
    "Git and GitHub (planned repository workflow)",
    "Git and GitHub (version control and repository hosting)"
)
s = s.replace("Student Name: __________________", "Student Name: Shubham")
s = s.replace("Roll Number: ___________________", "Roll Number: 2301730100")
s = s.replace(
    "Course: ________________________",
    "Course: B.Tech CSE (AI and ML), Assignment 3, Unit 3"
)
s = s.replace(
    "Submission Date: _______________",
    "Submission Date: 23 November 2026"
)

p.write_text(s, encoding="utf-8")
print("Report update complete.")
print("Disk image section:", "13. DISK IMAGE ACQUISITION" in s)
print("Conclusion section:", "# 14. CONCLUSION" in s)
print("Authorship section:", "# 15. AUTHORSHIP DECLARATION" in s)
