import psutil
from datetime import datetime
from email_alert import send_email_alert


print("================================")
print("      SERVER HEALTH CHECK")
print("================================")

cpu_usage = psutil.cpu_percent(interval=1)
memory_usage = psutil.virtual_memory().percent
disk_usage = psutil.disk_usage("C:\\").percent

print(f"CPU Usage    : {cpu_usage}%")
print(f"Memory Usage : {memory_usage}%")
print(f"Disk Usage   : {disk_usage}%")

print("\n================================")
print("          ALERT STATUS")
print("================================")

alerts = []

# CPU check
if cpu_usage > 80:
    alert = f"CPU usage is above 80%: {cpu_usage}%"
    print("ALERT:", alert)
    alerts.append(alert)
else:
    print("CPU: NORMAL")


# Memory check
if memory_usage > 80:
    alert = f"Memory usage is above 80%: {memory_usage}%"
    print("ALERT:", alert)
    alerts.append(alert)
else:
    print("Memory: NORMAL")


# Disk check
if disk_usage > 85:
    alert = f"Disk usage is above 85%: {disk_usage}%"
    print("ALERT:", alert)
    alerts.append(alert)
else:
    print("Disk: NORMAL")


# Save alerts and send email
if alerts:

    with open("../logs/alert.log", "a") as log_file:

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        for alert in alerts:

            log_file.write(
                f"{timestamp} - ALERT - {alert}\n"
            )

            # Send email
            send_email_alert(alert)

    print("\nAlert saved to logs/alert.log")
    print("Email alert process completed.")

else:

    print("\nNo alerts detected.")