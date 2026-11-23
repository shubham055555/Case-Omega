import re
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOG_DIR = ROOT / "evidence" / "logs"
OUTPUT = ROOT / "reports" / "ioc_results.csv"

indicators = {
    "Suspicious Account": r"unknown-admin",
    "Suspicious Process": r"remote_tool\.exe",
    "Persistence Service": r"UpdaterSvc",
    "Ransom Note": r"README_RECOVER\.txt",
    "Encrypted Extension": r"\.locked",
    "Suspicious IP": r"198\.51\.100\.24",
    "USB Device": r"USB-TRAIN-004"
}

results = []

for log_file in LOG_DIR.glob("*.log"):
    with log_file.open(encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            for name, pattern in indicators.items():
                if re.search(pattern, line, re.IGNORECASE):
                    results.append([
                        name,
                        line.strip(),
                        log_file.name,
                        line_number
                    ])

with OUTPUT.open("w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["IOC Type", "Matched Log Entry", "Source Log", "Line Number"])
    writer.writerows(results)

print("=" * 55)
print("       CASE OMEGA - AUTOMATIC IOC DETECTOR")
print("=" * 55)

for name, entry, source, line in results:
    print(f"\n[DETECTED] {name}")
    print(f"Source: {source}, Line: {line}")
    print(f"Evidence: {entry}")

print("\nTotal IOC matches:", len(results))
print("Report saved:", OUTPUT)
