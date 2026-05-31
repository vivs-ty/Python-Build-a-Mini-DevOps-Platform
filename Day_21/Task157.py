#  Task 157: Extend alerts to email, or simulate email delivery.

import psutil
import time
import smtplib
from email.mime.text import MIMEText

def simulate_email_alert(subject, body):
    print("--- EMAIL ALERT TRIGGERED ---")
    print(f"Subject: {subject}")
    print(f"Body: {body}")
    print("-----------------------------")

def real_email_alert(subject, body):
    # This is how you would send a real email using standard Python libraries
    sender = "your_email@example.com"
    receiver = "admin@example.com"
    password = "your_app_password"

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender, password)
            server.sendmail(sender, receiver, msg.as_string())
    except Exception as e:
        print(f"Failed to send email: {e}")

def monitor_cpu_usage(threshold=80.0):
    print(f"Monitoring CPU (Threshold: {threshold}%)...")
    try:
        while True:
            cpu_usage = psutil.cpu_percent(interval=1)
            if cpu_usage > threshold:
                alert_message = f"CPU usage exceeded threshold! Current usage: {cpu_usage}%"
                
                # Using the simulation for the demo
                simulate_email_alert("High CPU Alert", alert_message)
                
            time.sleep(5)
    except KeyboardInterrupt:
        print("Monitoring stopped.")

if __name__ == "__main__":
    # Using a low threshold to demonstrate the email simulation
    monitor_cpu_usage(threshold=5.0)

print(" \n Python 30 days Series - Day 21 : Task 157 \n"                                                 )
print(" \n Day 21 : Logging, Monitoring, and Alerts \n"                                                )
print(" \n Have a good one! \n "                          + "-"*40)
