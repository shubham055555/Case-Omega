import csv
import hashlib
from pathlib import Path

image = Path("evidence/images/case_omega_simulated.dd")
manifest = Path("reports/hash_manifest.csv")

digest = hashlib.sha256(image.read_bytes()).hexdigest().upper()

with manifest.open("r", newline="", encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))

if not any(Path(row["Path"]).name == image.name for row in rows):
    rows.append({
        "Algorithm": "SHA256",
        "Hash": digest,
        "Path": str(image.resolve())
    })

with manifest.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["Algorithm", "Hash", "Path"])
    writer.writeheader()
    writer.writerows(rows)

print("Disk image hash added successfully!")
print("SHA-256:", digest)
print("Total evidence files:", len(rows))
