import matplotlib.pyplot as plt

# Full day data (every 3 hours)
time_labels = ['12AM', '3AM', '6AM', '9AM', '12PM', '3PM', '6PM', '9PM']
sessions = [100000, 250000, 500000, 750000, 1250000, 1000000, 500000, 200000]
flavours = ['m8g.large', 'm8g.12xlarge', 'm8g.24xlarge', 'm8g.48xlarge',
            'm8g.metal-48xl', 'm8g.48xlarge', 'm8g.24xlarge', 'm8g.12xlarge']

# Map unique flavours to numeric levels for plotting
unique_flavours = list(dict.fromkeys(flavours))  # Remove duplicates but preserve order
flavour_to_y = {flavour: i for i, flavour in enumerate(unique_flavours)}
flavour_y_values = [flavour_to_y[f] for f in flavours]

# Create plot
fig, ax1 = plt.subplots(figsize=(12, 6))

# Left y-axis: Bar plot for session counts
bars = ax1.bar(time_labels, sessions, color='orange', label='No of Sessions')
ax1.set_ylabel('No of Sessions', color='orange')
ax1.set_ylim(0, 1300000)
ax1.set_yticks([0, 250000, 500000, 750000, 1000000, 1250000])
ax1.tick_params(axis='y', labelcolor='orange')
ax1.axhline(y=1250000, color='red', linestyle='--', linewidth=2, label='Max Session: 1,250,000')

# Right y-axis: Step curve for flavour trend
ax2 = ax1.twinx()
ax2.plot(time_labels, flavour_y_values, color='green', marker='o', linewidth=2,
         linestyle='-', drawstyle='steps-post', label='Flavours')
ax2.set_ylabel('Flavours', color='green')
ax2.set_ylim(-0.5, len(unique_flavours) - 0.5)
ax2.set_yticks(range(len(unique_flavours)))
ax2.set_yticklabels(unique_flavours)
ax2.tick_params(axis='y', labelcolor='green')

# Title and layout
plt.title('Session Counts and Instance Flavours Over 24 Hours')
fig.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Combined legend from both axes
lines_labels = [ax.get_legend_handles_labels() for ax in [ax1, ax2]]
lines, labels = [sum(lol, []) for lol in zip(*lines_labels)]
plt.legend(lines, labels, loc='upper center', bbox_to_anchor=(0.5, 1.1), ncol=3)

plt.show()
