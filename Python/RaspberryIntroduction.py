'''
DAY 17: Raspberry introduction
Guess what? I got a Raspberry Pi! I am so excited to start learning about it and all the cool projects I can do with it. I already set it up (trying not to use tutorials to strengthen my problem-solving skills), it took some time (so it's not exactly the 17th day) but it's worth it
Before getting into projects, I want to learn the basics, especially I need to know the temperature of the cpu in real-time, it's just a fan-less 4 model b with 2 GB of RAM at the moment so it's absolutely necessary to keep an eye on the temperature
To get the temperature just use psutil library:
'''

import psutil # This is the library that allows us to get system information, including CPU temperature
import time
import os
import random

def monitor_system():
    print("--- Raspberry Pi System Monitor ---")
    print("Type Ctrl+C to stop\n")
    
    with open("system_stats.csv", "a") as f:
        f.write("Timestamp,CPU_Usage,RAM_Usage,Temp\n")

    try:
        while True:
            cpu_usage = psutil.cpu_percent(interval=1)
            ram_usage = psutil.virtual_memory().percent
            
            temp = "N/A"

            '''try:
                with open("/sys/class/thermal/thermal_zone0/temp", "r") as t:
                    temp = int(t.read()) / 1000 
            except: ''' # This just for Linux and Raspberry Pi OS

            temp = int(random.randint(40, 70)) # Simulating temperature for testing on other OS like Windows or MacOS
            
            timestamp = time.strftime("%H:%M:%S")
            
            print(f"[{timestamp}] CPU: {cpu_usage}% | RAM: {ram_usage}% | Temp: {temp}°C")
            
            with open("system_stats.csv", "a") as f:
                f.write(f"{timestamp},{cpu_usage},{ram_usage},{temp}\n")
            
            if temp != "N/A" and temp > 75:
                print("WARNING: high temperature!")

    except KeyboardInterrupt:
        print("\nmonitoring ended. Stats saved in system_stats.csv")

if __name__ == "__main__":
    monitor_system()

'''
Can't wait to do some projects on it, I'm making another directory for my Raspberry Pi projects and updates!
'''