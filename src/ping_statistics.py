import matplotlib.pyplot as plt

# === manually enter data since its not json ===
data = [
    {"delay": 10, "avg_rtt": 16.250, "loss": 0.0},
    {"delay": 30, "avg_rtt": 15.827, "loss": 0.0},
    {"delay": 50, "avg_rtt": 15.749, "loss": 0.0},
    {"delay": 70, "avg_rtt": 15.684, "loss": 0.0},
]

# === extract data ===
delays = [d["delay"] for d in data]
avg_rtts = [d["avg_rtt"] for d in data]
losses = [d["loss"] for d in data]

# === Plot ===
fig, ax1 = plt.subplots(figsize=(10, 6))

ax1.plot(delays, avg_rtts, marker='o', color='blue', label='Avg RTT (ms)')
ax1.set_xlabel("Configured Delay (ms)")
ax1.set_ylabel("Avg RTT (ms)", color='blue')
ax1.tick_params(axis='y', labelcolor='blue')
ax1.grid(True)

# === packet loss ===
ax2 = ax1.twinx()
ax2.plot(delays, losses, marker='x', color='red', label='Packet Loss (%)')
ax2.set_ylabel("Packet Loss (%)", color='red')
ax2.tick_params(axis='y', labelcolor='red')

# === Combine legends ===
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper right')

plt.title("Ping Latency and Packet Loss vs Configured Delay")
plt.tight_layout()
plt.legend()
plt.savefig("plots/ping_statistics.png")
plt.show()
