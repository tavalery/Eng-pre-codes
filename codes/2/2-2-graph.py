import matplotlib.pyplot as plt
 
data = [255, 127, 64, 32, 5, 0, 256]
values = [3.246, 1.671, 0.867, 0.460, 0.1145, 0.0533, 0.0533]
 
plt.figure(figsize=(8, 6), dpi=100)
plt.axis([0, 256, 0, 3.3])
plt.plot(data[:-1], values[:-1], "ob")
plt.plot(data[:-1], values[:-1])
plt.show()