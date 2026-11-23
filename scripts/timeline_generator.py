import csv
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
LOG_DIR = ROOT / "evidence" / "logs"
OUTPUT = ROOT / "reports" / "attack_timeline.csv"

events = []

for log_file in LOG_DIR.glob("*.log"):
    with log_file.open(encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line or line.startswith("#") or line.startswith("SIMULATED"):
                continue

            parts = line.split(maxsplit=1)

            if len(parts) != 2:
                continue

            timestamp, description = parts

            try:
                event_time = datetime.fromisoformat(
                    timestamp.replace("Z", "+00:00")
                )
            except ValueError:
                continue

            events.append({
                "timestamp": event_time,
                "source": log_file.name,
                "event": description
            })

events.sort(key=lambda item: item["timestamp"])

with OUTPUT.open("w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp UTC", "Source Log", "Event Description"])

    for event in events:
        writer.writerow([
            event["timestamp"].astimezone(timezone.utc).isoformat(),
            event["source"],
            event["event"]
        ])

print("=" * 65)
print("           CASE OMEGA - ATTACK TIMELINE")
print("=" * 65)

for event in events:
    print(
        event["timestamp"].strftime("%H:%M:%S UTC"),
        "|",
        event["source"],
        "|",
        event["event"]
    )

print("\nTotal events:", len(events))
print("Timeline saved:", OUTPUT)
