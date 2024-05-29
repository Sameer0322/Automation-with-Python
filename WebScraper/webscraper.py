import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk, messagebox

def scrape_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        headlines = soup.find_all('h1')
        headlines_text = [headline.text for headline in headlines]
        return headlines_text
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Failed to retrieve data: {e}")
        return []

def display_headlines():
    url = url_entry.get()
    scrape_button.config(state=tk.DISABLED)
    status_label.config(text="Loading...")
    root.update_idletasks()
    headlines = scrape_website(url)
    scrape_button.config(state=tk.NORMAL)
    if headlines:
        result_text.delete('1.0', tk.END)
        for headline in headlines:
            result_text.insert(tk.END, headline + "\n")
        status_label.config(text="Scraping completed successfully.")
    else:
        status_label.config(text="Scraping failed.")

root = tk.Tk()
root.title("Web Scraping Tool")

url_label = ttk.Label(root, text="Enter Website URL:")
url_label.pack(pady=5)
url_entry = ttk.Entry(root, width=50)
url_entry.pack(pady=5)

scrape_button = ttk.Button(root, text="Scrape", command=display_headlines)
scrape_button.pack(pady=5)

status_label = ttk.Label(root, text="")
status_label.pack(pady=5)

result_text = tk.Text(root, height=20, width=60)
result_text.pack(pady=5)

root.mainloop()
