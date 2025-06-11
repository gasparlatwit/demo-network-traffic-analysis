import matplotlib.pyplot as plt
import json

# === Load Data ===
with open("data/iperf3_udp_h1_h4.json") as f1, open("data/udp_test_qos_changed.json") as f2, open("data/iperf3_udp_parallel.json") as f3:
    data_single = json.load(f1)
    data_qos = json.load(f2)
    data_parallel = json.load(f3)

# === throughput ===
def extract_throughput(data):
    return [interval['sum']['bits_per_second'] / 1e6 for interval in data['intervals']]

# === loss ===
def extract_loss_percent(data):
    return data['end']['sum']['lost_percent']

# === data ===
t_single = extract_throughput(data_single)
t_qos = extract_throughput(data_qos)
t_parallel = extract_throughput(data_parallel)

loss_single = extract_loss_percent(data_single)
loss_qos = extract_loss_percent(data_qos)
loss_parallel = extract_loss_percent(data_parallel)


time = list(range(1, len(t_single) + 1))


# === throuoghput ===
fig, ax1 = plt.subplots(figsize=(10, 6))

# Primary Y-axis: Throughput
ax1.plot(time, t_single, label='Throughput: Single', color='blue', marker='o')
ax1.plot(time, t_qos, label='Throughput: QoS Changed', color='red', marker='s')
ax1.plot(time, t_parallel, label='Throughput: Parallel (4)', color='purple', marker='x')
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Throughput (Mbps)', color='black')
ax1.tick_params(axis='y', labelcolor='black')
ax1.grid(True)

# Secondary Y-axis: Packet Loss %
ax2 = ax1.twinx()
ax2.axhline(loss_single, color='blue', linestyle='dotted', label=f'Loss: Single ({loss_single:.1f}%)')
ax2.axhline(loss_qos, color='red', linestyle='dotted', label=f'Loss: QoS Changed ({loss_qos:.1f}%)')
ax2.axhline(loss_parallel, color='purple', linestyle='dotted', label=f'Loss: Parallel ({loss_parallel:.1f}%)')
ax2.set_ylabel('Packet Loss (%)', color='gray')
ax2.tick_params(axis='y', labelcolor='gray')

# Legend
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc='upper right')

# Save & Show
plt.title('UDP Throughput and Packet Loss')
plt.tight_layout()
plt.legend()
plt.savefig("plots/udp_throughput_and_loss.png")
plt.show()