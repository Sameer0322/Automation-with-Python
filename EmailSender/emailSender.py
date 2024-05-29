import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import tkinter as tk
from tkinter import messagebox
import schedule
import time

# Function to send email
def send_email():
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    username = username_entry.get()
    password = password_entry.get()
    to_address = to_entry.get()
    subject = subject_entry.get()
    body = body_entry.get("1.0", tk.END)
    
    if not (username and password and to_address and subject and body):
        messagebox.showwarning("Warning", "Please fill in all fields.")
        return

    try:
        msg = MIMEMultipart()
        msg['From'] = username
        msg['To'] = to_address
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(username, password)
        text = msg.as_string()
        server.sendmail(username, to_address, text)
        server.quit()

        messagebox.showinfo("Success", "Email sent successfully.")
        to_entry.delete(0, tk.END)
        subject_entry.delete(0, tk.END)
        body_entry.delete("1.0", tk.END)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to send email. Error: {str(e)}")

# Function to schedule email
def schedule_email():
    scheduled_time = time_entry.get()
    schedule.every().day.at(scheduled_time).do(send_email)

# Create GUI window
root = tk.Tk()
root.title("Automated Email Sender")

# Create GUI components
username_label = tk.Label(root, text="Gmail Username:")
username_entry = tk.Entry(root, width=50)
password_label = tk.Label(root, text="Gmail Password:")
password_entry = tk.Entry(root, width=50, show="*")
to_label = tk.Label(root, text="To:")
to_entry = tk.Entry(root, width=50)
subject_label = tk.Label(root, text="Subject:")
subject_entry = tk.Entry(root, width=50)
body_label = tk.Label(root, text="Body:")
body_entry = tk.Text(root, width=50, height=10)
time_label = tk.Label(root, text="Scheduled Time (HH:MM):")
time_entry = tk.Entry(root, width=50)
send_button = tk.Button(root, text="Send Email", command=send_email)
schedule_button = tk.Button(root, text="Schedule Email", command=schedule_email)

# Place GUI components
username_label.grid(row=0, column=0, sticky="e")
username_entry.grid(row=0, column=1, padx=5, pady=5, columnspan=2)
password_label.grid(row=1, column=0, sticky="e")
password_entry.grid(row=1, column=1, padx=5, pady=5, columnspan=2)
to_label.grid(row=2, column=0, sticky="e")
to_entry.grid(row=2, column=1, padx=5, pady=5, columnspan=2)
subject_label.grid(row=3, column=0, sticky="e")
subject_entry.grid(row=3, column=1, padx=5, pady=5, columnspan=2)
body_label.grid(row=4, column=0, sticky="ne")
body_entry.grid(row=4, column=1, padx=5, pady=5, columnspan=2)
time_label.grid(row=5, column=0, sticky="e")
time_entry.grid(row=5, column=1, padx=5, pady=5, columnspan=2)
send_button.grid(row=6, column=1, padx=5, pady=5)
schedule_button.grid(row=6, column=2, padx=5, pady=5)

# Start GUI event loop
root.mainloop()
