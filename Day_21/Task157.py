#  Task 157: Extend alerts to email, or simulate email delivery.

import smtplib
from email.mime.text import MIMEText
import psutil
import time

def send_email_alert(subject, body):
    # Simulate email delivery (replace with actual email configuration)
    print(f"Sending email: {subject}")
    print(f"Message: {body}")
def monitor_cpu_usage(threshold=80):
    while True:
        cpu_usage = psutil.cpu_percent(interval=1)
        if cpu_usage > threshold:
            alert_message = f"ALERT: CPU usage is at {cpu_usage}%!"
            print(alert_message)
            send_email_alert("CPU Usage Alert", alert_message)
        time.sleep(5)
if __name__ == "__main__":
    monitor_cpu_usage(threshold=80)
