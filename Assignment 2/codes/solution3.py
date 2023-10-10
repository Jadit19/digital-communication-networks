import numpy as np
import matplotlib.pyplot as plt

R = 5  # Transmission capacity in bits per second
TIME_INSTANTS = 10_000  # Number of time instants for simulation

# Packet sizes
a, b, c, d = 2, 4, 6, 8

# Probabilities for different cases
cases = [[0.25, 0.25, 0.25, 0.25], [0, 0.5, 0.5, 0], [0.5, 0, 0, 0.5], [0, 0, 0, 1]]


def gen_packet_size(prob):
    rand = np.random.rand()
    if rand < prob[0]:
        return a
    elif rand < sum(prob[:2]):
        return b
    elif rand < sum(prob[:3]):
        return c
    else:
        return d


def simulate_queue(p, prob):
    queue_length = 0
    total_delay = 0
    total_packets = 0

    for _ in range(TIME_INSTANTS):
        if np.random.rand() < p:
            packet_size = gen_packet_size(prob)
            queue_length += packet_size
            if queue_length > R:
                delay = (queue_length - R) / R
                total_delay += delay
            total_packets += 1
        queue_length -= R
        if queue_length < 0:
            queue_length = 0

    avg_queue_length = queue_length
    avg_delay = total_delay / total_packets if total_packets > 0 else 0
    return avg_queue_length, avg_delay


p_values = [i / 100 for i in range(99)]
for _case in cases:
    avg_queue_lengths = []
    avg_delays = []
    for p in p_values:
        avg_ql, avg_d = simulate_queue(p, _case)
        avg_queue_lengths.append(avg_ql)
        avg_delays.append(avg_d)

    plt.figure(figsize=(16, 9))
    plt.plot(
        p_values, avg_queue_lengths, label=f"Case {cases.index(_case)+1} Queue Length"
    )
    plt.plot(
        p_values, avg_delays, label=f"Case {cases.index(_case)+1} Delay", linestyle="--"
    )
    plt.legend()
    plt.xlabel("p")
    plt.ylabel("Value")
    plt.grid()
    plt.title("Network Queuing Simulation")
    plt.tight_layout()
    plt.savefig(f"plot{cases.index(_case)+1}.png")
