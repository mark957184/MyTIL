'''
DAY 18: Data handling on graphs
Today I learned how I can transform data in .csv's to graphs with a Python library, matplotlib:
'''

import matplotlib.pyplot as plt
import csv
import os

def create_graph():
    time = []
    temps = []
    cpu = []

    if not os.path.exists("system_stats.csv"): # The csv created by yesterday's file
        print("File not found. Check and try again")
        return
    
    with open("system_stats.csv", "r") as f:
        reader = csv.DictReader(f)
        for riga in reader:
            time.append(riga["Timestamp"])
            temps.append(float(riga["Temp"]) if riga["Temp"] != "N/A" else 0)
            cpu.append(float(riga["CPU_Usage"]))
    
    plt.figure(figsize=(10, 5))

    plt.plot(time, temps, label="Temperature (°C)", color="red", marker="o")
    plt.plot(time, cpu, label="CPU usage (%)", color="blue", linestyle="--")
    plt.title("Raspberry Pi 4 model B's Performance")
    plt.xlabel("Time")
    plt.ylabel("Values")
    plt.legend() # Show legend
    plt.xticks(rotation=45)
    plt.tight_layout() # Make it clean

    plt.savefig("report_performance.png") # Save as image
    print("Graph saved as report_performance.png")
    plt.show()

if __name__ == "__main__":
    create_graph()

'''
This could be useful to get a (more graphical) overall "aftermath" after an heavy usage of my Raspberry!
'''