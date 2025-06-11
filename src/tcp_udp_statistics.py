import json
import matplotlib.pyplot as plt

# === Load UDP Data ===
with open('data/iperf3_udp_h1_h4.json') as f_udp:
    udp_data = json.load(f_udp)

udp_times, udp_throughputs, udp_loss_percent = [], [], []

for interval in udp_data['intervals']:
    stream = interval['streams'][0]
    start = stream['start']
    end = stream['end']
    udp_times.append((start + end) / 2)

    throughput_mbps = stream['bits_per_second'] / 1e6
    udp_throughputs.append(throughput_mbps)

    lost = stream.get('lost_packets', 0)
    total = stream.get('packets', 1)
    loss = (lost / total) * 100 if total > 0 else 0
    udp_loss_percent.append(loss)

# === Load TCP Data ===
with open('data/iperf3_tcp_h1_h4.json') as f_tcp:
    tcp_data = json.load(f_tcp)

tcp_times, tcp_throughputs = [], []

for interval in tcp_data['intervals']:
    start = interval['sum']['start']
    end = interval['sum']['end']
    tcp_times.append((start + end) / 2)

    throughput_mbps = interval['sum']['bits_per_second'] / 1e6
    tcp_throughputs.append(throughput_mbps)

# === Plotting ===
fig, ax1 = plt.subplots(figsize=(10, 6))

# TCP Throughput
ax1.set_xlabel('Time (seconds)')
ax1.set_ylabel('Throughput (Mbps)', color='tab:blue')
ax1.plot(tcp_times, tcp_throughputs, label='TCP Throughput (h1→h4)', color='tab:blue', marker='o')
ax1.plot(udp_times, udp_throughputs, label='UDP Throughput (h1→h4)', color='tab:green', marker='s')
ax1.tick_params(axis='y', labelcolor='tab:blue')

# UDP Packet Loss
ax2 = ax1.twinx()
ax2.set_ylabel('UDP Packet Loss (%)', color='tab:red')
ax2.plot(udp_times, udp_loss_percent, label='UDP Loss %', color='tab:red', marker='x', linestyle='--')
ax2.tick_params(axis='y', labelcolor='tab:red')

plt.title('TCP & UDP Performance: Throughput and Packet Loss Over Time (h1 → h4)')
fig.legend(loc='upper right', bbox_to_anchor=(0.9, 0.85))
plt.grid(True)
plt.tight_layout()
plt.savefig('plots/tcp_udp_statistics.png')
plt.show()