import matplotlib.pyplot as plt
import json

# === load data ===
with open('data/iperf3_tcp_h1_h4.json') as fwd_file, open('data/iperf3_tcp_h4_h1_reverse.json') as rev_file:
    fwd_data = json.load(fwd_file)
    rev_data = json.load(rev_file)

# Extract throughput
fwd_throughput = [interval['sum']['bits_per_second'] / 1e6 for interval in fwd_data['intervals']]
rev_throughput = [interval['sum']['bits_per_second'] / 1e6 for interval in rev_data['intervals']]


# === Plotting ===
time = list(range(1, len(fwd_throughput) + 1))

plt.figure(figsize=(10,6))
plt.plot(time, fwd_throughput, label='Forward TCP (h1 → h4)', marker='o')
plt.plot(time, rev_throughput, label='Reverse TCP (h4 → h1)', marker='x')

plt.title('TCP Throughput Over Time')
plt.xlabel('Time (seconds)')
plt.ylabel('Throughput (Mbps)')
plt.legend()
plt.grid(True)
plt.tight_layout()

# Save or show
plt.savefig('plots/tcp_throughput.png')
plt.show()