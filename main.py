# Threat Intelligence Platform

from core.ioc_manager import load_iocs
from core.analyzer import analyze_logs

# Load IOC feed
iocs = load_iocs()

# Load logs
with open("data/logs.txt", "r") as file:
    logs = file.readlines()

print("=== Threat Intelligence Analysis ===\n")

# Analyze logs with intelligence
alerts = analyze_logs(logs, iocs)

for alert in alerts:
    print(alert)
