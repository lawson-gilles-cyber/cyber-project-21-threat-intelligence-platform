# Analysis using threat intelligence

def analyze_logs(logs, iocs):

    alerts = []

    for log in logs:
        log = log.strip()

        for ioc in iocs:
            if ioc in log:
                alerts.append(f"[TIP ALERT] IOC match detected: {ioc}")

    return alerts
