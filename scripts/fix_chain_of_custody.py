import csv
from pathlib import Path

path = Path("reports/chain_of_custody.csv")

with path.open(newline="", encoding="utf-8") as f:
    rows = list(csv.reader(f))

header = rows[0]

for i, row in enumerate(rows[1:], start=1):
    if row and row[0] == "E-04":
        rows[i] = [
            "E-04",
            "Synthetic Disk Image",
            "Shubham",
            row[3],
            "Python-generated training artifact",
            "Synthetic raw image generation and SHA-256 verification",
            "2E49B4F51B8682DCC2A870EAFCA3A71250B3B8921BE27C9171E092FFA1A1551",
            "Not transferred",
            "",
            "Synthetic evidence; no physical hospital disk acquired"
        ]

with path.open("w", newline="", encoding="utf-8") as f:
    csv.writer(f).writerows(rows)

print("CSV corrected successfully")
print("Header columns:", len(header))
print("Evidence records:", len(rows) - 1)
print("Column counts:", [len(r) for r in rows])
