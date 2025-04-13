import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator

# X-axis time points
timestamps = [f"{(23 + i*2) % 24:02d}:00" for i in range(13)]
x = np.arange(len(timestamps))

# --- 5QI Flow 2 ---
constraint_2 = 1e-3
per_old_flow2 = [0.8e-3, 0.85e-3, 0.9e-3, 0.95e-3, 0.99e-3, 0.9e-3, 0.95e-3, 0.8e-3, 0.85e-3, 0.95e-3, 0.92e-3, 0.89e-3, 0.87e-3]  # Always below
per_now_flow2 = [1.2e-3, 1.3e-3, 1.1e-3, 1.4e-3, 0.95e-3, 1.5e-3, 1.6e-3, 1.7e-3, 1.2e-3, 1.05e-3, 1.3e-3, 1.6e-3, 1.4e-3]  # Mostly above (2 below)

# --- 5QI Flow 79 ---
constraint_79 = 1e-2
per_old_flow79 = [0.008, 0.009, 0.0095, 0.0098, 0.0085, 0.007, 0.0099, 0.0092, 0.008, 0.0091, 0.009, 0.0093, 0.0097]  # Always below
per_now_flow79 = [0.012, 0.013, 0.011, 0.014, 0.009, 0.015, 0.016, 0.0135, 0.0122, 0.0115, 0.0145, 0.0105, 0.0112]  # Mostly above (3 below)

# Modify values to follow the constraint conditions:

# Adjust per_now_flow2 to follow above and below constraint 1-2 times
per_now_flow2 = [1.9e-3, 1.7e-3, 1.8e-3, 2e-3, 1.8e-3, 0.9e-3, 1.95e-3, 1.65e-3, 0.8e-3, 1.8e-3, 1.3e-3, 1.95e-3, 1.85e-3]

# Adjust per_old_flow2 to remain below the constraint
per_old_flow2 = [0.6e-3, 0.3e-3, 0.8e-3, 0.2e-3, 0.3e-3, 0.6e-3, 0.71e-3, 0.5e-3, 0.3e-3, 0.73e-3, 0.6e-3, 0.7e-3, 0.5e-3]  # No change

# Adjust per_now_flow79 to follow above and below constraint 1-2 times
per_now_flow79 = [0.012, 0.013, 0.011, 0.012, 0.009, 0.013, 0.011, 0.0135, 0.0122, 0.0115, 0.0135, 0.0105, 0.0112]

# Adjust per_old_flow79 to remain below the constraint
per_old_flow79 = [0.008, 0.009, 0.0095, 0.0098, 0.0085, 0.007, 0.0099, 0.0092, 0.008, 0.0091, 0.009, 0.0093, 0.0097]  # No change

# Create plot
fig, ax = plt.subplots(figsize=(14, 8))

# Plot 5QI Flow 2
ax.plot(x, per_now_flow2, label='1. 5QI 2 - Current (Cyan)', color='cyan', marker='o')
ax.plot(x, per_old_flow2, label='2. 5QI 2 - Old (Red)', color='red', marker='o')
ax.plot(x, [constraint_2]*len(x), label='3. 5QI 2 - Constraint', color='blue', linestyle=':')

# Plot 5QI Flow 79
ax.plot(x, per_now_flow79, label='4. 5QI 79 - Current (Orange)', color='orange', marker='s')
ax.plot(x, per_old_flow79, label='5. 5QI 79 - Old (Purple)', color='purple', marker='s')
ax.plot(x, [constraint_79]*len(x), label='6. 5QI 79 - Constraint', color='green', linestyle=':')

# Axis formatting
ax.set_xticks(x)
ax.set_xticklabels(timestamps, rotation=45)
ax.set_xlabel('Timestamp', fontsize=12)
ax.set_ylabel('Packet Error Rate', fontsize=12)

# Y-axis: set limits between [0, 0.014] with a tick interval of 0.001
ax.set_ylim(0, 0.014)
ax.yaxis.set_major_locator(MultipleLocator(0.001))  # Set interval to 0.001
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda val, _: f'{val:.4f}'))  # Display 4 decimal places

# Limit X-axis range to match the number of timestamps
ax.set_xlim(left=0, right=len(timestamps) - 1)

# Custom legend
handles, labels = ax.get_legend_handles_labels()
custom_order = [0, 3, 1, 4, 2, 5]
handles = [handles[i] for i in custom_order]
labels = [labels[i] for i in custom_order]

legend = ax.legend(
    handles, labels,
    loc='upper center',
    bbox_to_anchor=(0.5, 1.15),
    ncol=3,
    fontsize=12,
    frameon=True,
    borderaxespad=0.5,
    handlelength=2,
    handleheight=1.2,
    handletextpad=0.5,
    borderpad=0.3,
    labelspacing=0,
    columnspacing=14.4
)

legend.get_frame().set_linewidth(0.8)
legend.get_frame().set_edgecolor('gray')
legend.get_frame().set_boxstyle('round', pad=0.2, rounding_size=0.2)

# Title placed below
plt.figtext(0.5, 0.01, '5QI Flow 2 and 79 - Packet Error Rate with Constraint', ha='center', fontsize=15)

# Layout adjustments
plt.tight_layout(rect=[0, 0.05, 1, 0.90])
plt.show()
