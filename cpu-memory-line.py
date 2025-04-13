import matplotlib.pyplot as plt
import numpy as np

# Timestamps start from 23:00, every 2 hours
timestamps = [f"{(23 + i * 2) % 24:02d}:00" for i in range(13)]
x = np.arange(len(timestamps))

# --- Swapped CPU usage in percentage (current usage now lower)
cpu_percent_current = [42, 48, 45, 50, 46, 49, 51, 47, 44, 45, 47, 46, 44]  # Swapped values
cpu_percent_old = [55, 62, 57, 65, 60, 67, 67, 66, 63, 64, 56, 60, 55]  # Swapped values

# Convert to milliCPU (1% = 10m)
cpu_current = [val * 10 for val in cpu_percent_current]
cpu_old = [val * 10 for val in cpu_percent_old]

# --- Swapped Memory Usage (MiB, current usage now lower)
mem_current = [470, 480, 475, 485, 478, 482, 488, 475, 472, 474, 480, 478, 473]  # Swapped values
mem_old = [510, 523, 515, 530, 518, 535, 545, 525, 522, 528, 535, 540, 533]  # Swapped values

# --- Plotting
fig, ax1 = plt.subplots(figsize=(14, 8))

# Left Y-axis: CPU
lns1 = ax1.plot(x, cpu_current, label='1. CPU - Current', color='cyan', marker='o')
lns2 = ax1.plot(x, cpu_old, label='2. CPU - Old', color='red', marker='o')

ax1.set_xlabel('Timestamp', fontsize=12)
ax1.set_ylabel('CPU Usage (m)', fontsize=12)
ax1.set_ylim(0, 1000)
ax1.set_xticks(x)
ax1.set_xticklabels(timestamps, rotation=45)
ax1.set_xlim(x[0], x[-1])

# Right Y-axis: Memory (Adjusted to 1000 for clarity)
ax2 = ax1.twinx()
lns3 = ax2.plot(x, mem_current, label='3. Memory - Current', color='orange', marker='s')
lns4 = ax2.plot(x, mem_old, label='4. Memory - Old', color='purple', marker='s')

ax2.set_ylabel('Memory Usage (MiB)', fontsize=12)
ax2.set_ylim(0, 600)

# Combine all lines for legend
lines = lns1 + lns2 + lns3 + lns4
labels = [line.get_label() for line in lines]

legend = ax1.legend(
    lines, labels,
    loc='upper center',
    bbox_to_anchor=(0.5, 1.15),
    ncol=2,
    fontsize=12,
    frameon=True,
    borderaxespad=0.5,
    handlelength=2,
    handleheight=1.2,
    handletextpad=0.5,
    borderpad=0.3,
    labelspacing=0,
    columnspacing=50
)

legend.get_frame().set_linewidth(0.8)
legend.get_frame().set_edgecolor('gray')
legend.get_frame().set_boxstyle('round', pad=0.2, rounding_size=0.2)

# Title below
plt.figtext(0.5, 0.01, '5QI 2 - CPU (m) and Memory (MiB) Usage', ha='center', fontsize=15)

plt.tight_layout(rect=[0, 0.05, 1, 0.90])
plt.show()
