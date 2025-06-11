import json
import matplotlib.pyplot as plt

# === load data ===
with open("data/iperf3_udp_h1_h4.json") as f1, \
     open("data/udp_test_qos_changed.json") as f2, \
     open("data/iperf3_udp_parallel.json") as f3:
    data_single = json.load(f1)
    data_qos = json.load(f2)
    data_parallel = json.load(f3)

# === extract jitter ===
def extract_jitter_single(data):
    jitter = data["end"]["sum"]["jitter_ms"]
    return [jitter] * len(data["intervals"])

def extract_jitter_parallel(data):
    stream_jitters = [s["udp"]["jitter_ms"] for s in data["end"]["streams"]]
    avg_jitter = sum(stream_jitters) / len(stream_jitters)
    return [avg_jitter] * len(data["intervals"])

jitter_single = extract_jitter_single(data_single)
jitter_qos = extract_jitter_single(data_qos)
jitter_parallel = extract_jitter_parallel(data_parallel)

time = list(range(1, len(jitter_single) + 1))

# === Plot ===
plt.figure(figsize=(10, 6))
plt.plot(time, jitter_single, label=f'Single Stream ({jitter_single[0]:.2f} ms)', marker='o', color='blue')
plt.plot(time, jitter_qos, label=f'QoS Changed ({jitter_qos[0]:.2f} ms)', marker='s', color='red')
plt.plot(time, jitter_parallel, label=f'Parallel Avg. ({jitter_parallel[0]:.2f} ms)', marker='x', color='purple')

plt.title('UDP Jitter Over Time')
plt.xlabel('Time (seconds)')
plt.ylabel('Jitter (ms)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("plots/udp_jitter_over_time.png")
plt.show()
