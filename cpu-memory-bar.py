import matplotlib.pyplot as plt
import numpy as np

# Data from the original line plot
cpu_percent_current = [42, 48, 45, 50, 46, 49, 51, 47, 44, 45, 47, 46, 44]
cpu_percent_old = [55, 62, 57, 65, 60, 67, 67, 66, 63, 64, 56, 60, 55]
mem_current = [470, 400, 475, 385, 478, 382, 388, 475, 472, 374, 380, 478, 473]
mem_old = [500, 523, 490, 530, 400, 535, 445, 505, 522, 528, 535, 440, 333]

# Convert to milliCPU (1% = 10m) and calculate totals
total_cpu_current = sum(val * 10 for val in cpu_percent_current)
total_cpu_old = sum(val * 10 for val in cpu_percent_old)
total_mem_current = sum(mem_current)
total_mem_old = sum(mem_old)

# --- Plotting
fig, ax1 = plt.subplots(figsize=(10, 8))

# X-axis positions
x = np.arange(2)  # Two groups: Method-1 (Old) and Method-2 (Current)
width = 0.35  # Width of the bars

# Left Y-axis: CPU bars
cpu_bars_old = ax1.bar(x[0] - width/2, total_cpu_old, width, label='1. CPU - Old', color='red')
cpu_bars_current = ax1.bar(x[1] - width/2, total_cpu_current, width, label='2. CPU - Current', color='cyan')

ax1.set_xlabel('Method', fontsize=12)
ax1.set_ylabel('Total CPU Usage (m)', fontsize=12)
ax1.set_xticks(x)
ax1.set_xticklabels(['Method-1 (Old)', 'Method-2 (Current)'])
ax1.set_ylim(0, max(total_cpu_old, total_cpu_current) * 1.25)

# Right Y-axis: Memory bars
ax2 = ax1.twinx()
mem_bars_old = ax2.bar(x[0] + width/2, total_mem_old, width, label='3. Memory - Old', color='purple')
mem_bars_current = ax2.bar(x[1] + width/2, total_mem_current, width, label='4. Memory - Current', color='orange')

ax2.set_ylabel('Total Memory Usage (MiB)', fontsize=12)
ax2.set_ylim(0, max(total_mem_old, total_mem_current) * 1.3)

# Combine all bars for legend
bars = [cpu_bars_old, cpu_bars_current, mem_bars_old, mem_bars_current]
labels = ['1. CPU - Old', '2. CPU - Current', '3. Memory - Old', '4. Memory - Current']

legend = ax1.legend(
    bars, labels,
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
    columnspacing=26
)

legend.get_frame().set_linewidth(0.8)
legend.get_frame().set_edgecolor('gray')
legend.get_frame().set_boxstyle('round', pad=0.2, rounding_size=0.2)

# Title below
plt.figtext(0.5, 0.01, '5QI 2 - Total CPU (m) and Memory (MiB) Usage Comparison', ha='center', fontsize=15)

plt.tight_layout(rect=[0, 0.05, 1, 0.90])
plt.show()
