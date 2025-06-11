import json
import matplotlib.pyplot as plt

# === Load data ===
with open("data/iperf3_tcp_h1_h4.json") as f_tcp_fwd, \
     open("data/iperf3_tcp_h4_h1_reverse.json") as f_tcp_rev, \
     open("data/iperf3_udp_h1_h4.json") as f_udp_single, \
     open("data/udp_test_qos_changed.json") as f_udp_qos, \
     open("data/iperf3_udp_parallel.json") as f_udp_parallel:

    tcp_fwd = json.load(f_tcp_fwd)
    tcp_rev = json.load(f_tcp_rev)
    udp_single = json.load(f_udp_single)
    udp_qos = json.load(f_udp_qos)
    udp_parallel = json.load(f_udp_parallel)

# === Average Throughput ===
def get_tcp_throughput_mbps(data):
    return data['end']['sum_received']['bits_per_second'] / 1e6

def get_udp_throughput_mbps(data):
    return data['end']['sum']['bits_per_second'] / 1e6

throughput_data = {
    "TCP Forward": get_tcp_throughput_mbps(tcp_fwd),
    "TCP Reverse": get_tcp_throughput_mbps(tcp_rev),
    "UDP Single": get_udp_throughput_mbps(udp_single),
    "UDP QoS": get_udp_throughput_mbps(udp_qos),
    "UDP Parallel": get_udp_throughput_mbps(udp_parallel),
}

# === Plot ===
labels = list(throughput_data.keys())
values = list(throughput_data.values())

plt.figure(figsize=(10, 6))
bars = plt.bar(labels, values, color=['steelblue', 'royalblue', 'skyblue', 'salmon', 'mediumpurple'])

# === label ===
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval + 1, f'{yval:.1f} Mbps', ha='center', va='bottom')

plt.title("Average Throughput Comparison (TCP vs UDP)")
plt.ylabel("Throughput (Mbps)")
plt.ylim(0, max(values) + 20)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("plots/throughput_statistics.png")
plt.show()
