import matplotlib.pyplot as plt

# Generate time labels from 12AM to 9PM hourly
time_labels = [f"{(h % 12 or 12)}{'AM' if h < 12 else 'PM'}" for h in range(0, 22)]

# Session data every 3 hours (main points)
main_times = ['12AM', '3AM', '6AM', '9AM', '12PM', '3PM', '6PM', '9PM']
sessions = [100000, 250000, 500000, 750000, 1250000, 1000000, 500000, 200000]
flavours = ['m8g.large', 'm8g.12xlarge', 'm8g.24xlarge', 'm8g.48xlarge',
            'm8g.metal-48xl', 'm8g.48xlarge', 'm8g.24xlarge', 'm8g.12xlarge']

# Map unique flavours to numeric levels
unique_flavours = list(dict.fromkeys(flavours))
flavour_to_y = {f: i for i, f in enumerate(unique_flavours)}
flavour_y_values = [flavour_to_y[f] for f in flavours]

# Get x positions for session bars (every 3 hours)
main_indices = [time_labels.index(t) for t in main_times]

# Shift flavour change earlier (simulate at 1 hour before change)
flavour_x = [i - 1 for i in main_indices]

# Plot setup
fig, ax1 = plt.subplots(figsize=(14, 6))

# Bar plot for sessions
ax1.bar(main_indices, sessions, width=1.5, color='orange', label='No of Sessions')
ax1.set_ylabel('No of Sessions', color='orange')
ax1.set_ylim(0, 1300000)
ax1.set_yticks([0, 250000, 500000, 750000, 1000000, 1250000])
ax1.tick_params(axis='y', labelcolor='orange')

# X-axis ticks for every hour
ax1.set_xticks(range(len(time_labels)))
ax1.set_xticklabels(time_labels, rotation=45)

# Twin axis for flavours
ax2 = ax1.twinx()
ax2.plot(flavour_x, flavour_y_values, color='green', marker='o',
         linestyle='-', linewidth=2, drawstyle='steps-post', label='Flavours')
ax2.set_ylabel('Flavours', color='green')
ax2.set_ylim(-0.5, len(unique_flavours) - 0.5)
ax2.set_yticks(range(len(unique_flavours)))
ax2.set_yticklabels(unique_flavours)
ax2.tick_params(axis='y', labelcolor='green')

# Add red line at max flavour level
max_flavour_y = max(flavour_y_values)
max_flavour_label = [k for k, v in flavour_to_y.items() if v == max_flavour_y][0]
ax2.axhline(y=max_flavour_y, color='red', linestyle='--', linewidth=2,
            label=f'Max Flavour: {max_flavour_label}')

# Grid and title
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.title('Session Counts and Instance Flavours Over 24 Hours')
fig.tight_layout()

# Combined legend from both axes
handles1, labels1 = ax1.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()
plt.legend(handles1 + handles2, labels1 + labels2, loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=3)

plt.show()
