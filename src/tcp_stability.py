import json
import matplotlib.pyplot as plt

# == data ===
with open("data/iperf3_tcp_stability.json") as f:
    data = json.load(f)

# === extract data ===
retransmissions, throughput = [], []

for interval in data["intervals"]:
    sum_stats = interval["sum"]
    throughput.append(sum_stats["bits_per_second"] / 1e6)  
    retransmissions.append(sum_stats.get("retransmits", 0)) 

# === Plotting ===
time = list(range(1, len(throughput) + 1))

fig, ax1 = plt.subplots(figsize=(10, 6))

# throughput
ax1.plot(time, throughput, label="Throughput", color="blue", marker="o")
ax1.set_xlabel("Time (s)")
ax1.set_ylabel("Throughput (Mbps)", color="blue")
ax1.tick_params(axis="y", labelcolor="blue")
ax1.grid(True)

# Retransmissions
ax2 = ax1.twinx()
ax2.plot(time, retransmissions, label="Retransmissions", color="red", marker="x")
ax2.set_ylabel("Retransmissions", color="red")
ax2.tick_params(axis="y", labelcolor="red")

# Legends
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper right")

plt.title("TCP Throughput and Retransmissions Over Time (Stability Test)")
plt.tight_layout()
plt.legend()
plt.savefig("plots/tcp_stability.png")
plt.show()
