import matplotlib.pyplot as plt

# Data
time_labels = ['12AM', '3AM', '6AM', '9AM', '12PM']
sessions = [250000, 500000, 750000, 1000000, 1250000]
flavours = ['m8g.12xlarge', 'm8g.24xlarge', 'm8g.48xlarge', 'm8g.48xlarge', 'm8g.metal-48xl']

fig, ax1 = plt.subplots(figsize=(10, 6))

# Orange bar plot for sessions
bars = ax1.bar(time_labels, sessions, color='orange', label='No of Sessions')
ax1.set_ylabel('No of Sessions', color='orange')
ax1.set_ylim(0, 1300000)
ax1.set_yticks([0, 250000, 500000, 750000, 1000000, 1250000])
ax1.tick_params(axis='y', labelcolor='orange')

# Red dashed line for max session
ax1.axhline(y=1250000, color='red', linestyle='--', linewidth=2, label='Max Session: 1,250,000')

# Green line for flavours (on secondary axis)
ax2 = ax1.twinx()
ax2.plot(time_labels, sessions, color='green', marker='o', linewidth=2, label='Flavours')
ax2.set_ylabel('Flavours', color='green')
ax2.tick_params(axis='y', labelcolor='green')
ax2.set_yticks(sessions)
ax2.set_yticklabels(flavours)

# Title and layout
plt.title('Session Counts and Instance Flavours Over Time')
fig.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Combine legends from both axes
lines_labels = [ax.get_legend_handles_labels() for ax in [ax1, ax2]]
lines, labels = [sum(lol, []) for lol in zip(*lines_labels)]
plt.legend(lines, labels, loc='upper center', bbox_to_anchor=(0.5, 1.1), ncol=3)

plt.show()
