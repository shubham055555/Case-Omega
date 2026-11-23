from pathlib import Path
import hashlib

output = Path("evidence/images/case_omega_simulated.dd")
size = 8 * 1024 * 1024

image = bytearray(size)

artifacts = [
    b"CASE OMEGA - SYNTHETIC FORENSIC DISK IMAGE",
    b"Hospital: Fictional City Hospital",
    b"Incident: Simulated ransomware attack",
    b"Date: 2026-11-18",
    b"User: SYSTEM",
    b"Event: Suspicious scheduled task created",
    b"Event: Simulated file encryption activity",
    b"Ransom note: YOUR FILES HAVE BEEN ENCRYPTED (SIMULATION ONLY)",
    b"IOC: 198.51.100.24",
    b"WARNING: This is synthetic training evidence, not a real hospital disk."
]

offset = 1024
for artifact in artifacts:
    data = artifact + b"\n"
    image[offset:offset + len(data)] = data
    offset += 4096

output.write_bytes(image)

digest = hashlib.sha256(output.read_bytes()).hexdigest()

print("Synthetic image created successfully")
print("File:", output)
print("Size:", output.stat().st_size, "bytes")
print("SHA-256:", digest)
print("Type: Synthetic raw training image - not an actual disk acquisition")
