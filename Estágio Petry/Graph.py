
import matplotlib.pyplot as plt
import numpy as np

archive = open("Tabela.txt","r")
voltage = []
time = []

text = archive.read()
text = text.split("\n")

for element in text:
    v = element.split(" ")
    voltage.append(float(v[0]))
    time.append(float(v[1]))
    
plt.style.use("ggplot")
plt.plot(time,voltage)
plt.xlabel("Time")
plt.ylabel("Voltage")
plt.title("Voltage vs Time")    
plt.savefig("Tabela.png")
plt.show()