import matplotlib.pyplot as plt

# Constants
R = 10000  # Link capacity
SSTH = 0.04 * R  # Threshold
TIME_STEPS = 20000  # Number of time steps for the simulation
CONSTANT = 1  # The constant by which flow rate increases when there's no congestion


def simulate_tcp_fairness(RTT_ratio):
    flow1_rate = 0.7 * R
    flow2_rate = 0.01 * R
    flow1_rates = [flow1_rate]
    flow2_rates = [flow2_rate]

    for _ in range(TIME_STEPS):
        if flow1_rate + flow2_rate > R:
            flow1_rate /= 2
            flow2_rate /= 2
        else:
            flow1_rate += CONSTANT
            flow2_rate += CONSTANT / RTT_ratio
        flow1_rates.append(flow1_rate)
        flow2_rates.append(flow2_rate)

    return flow1_rates, flow2_rates


# Simulate for both cases
flow1_rates_same_RTT, flow2_rates_same_RTT = simulate_tcp_fairness(1)
flow1_rates_diff_RTT, flow2_rates_diff_RTT = simulate_tcp_fairness(10)

# Plotting
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(flow1_rates_same_RTT, flow2_rates_same_RTT, label="Same RTT")
plt.plot([R, 0], [0, R], "k--", label="Fairness Line")  # Fairness line
plt.plot([0, R / 1.5], [0, R / 1.5], "--", label="Convergence line")  # Convergence line
plt.scatter(
    [flow1_rates_same_RTT[0], flow1_rates_same_RTT[-1]],
    [flow2_rates_same_RTT[0], flow2_rates_same_RTT[-1]],
    c="red",
    label="Start/End Points",
)  # Start and End points
plt.title("RTTs with same flow")
plt.xlabel("Time Steps")
plt.ylabel("Flow Rate")
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(flow1_rates_diff_RTT, flow2_rates_diff_RTT, label="Different RTT")
plt.plot([R, 0], [0, R], "k--", label="Fairness Line")  # Fairness line
plt.plot([0, R], [0, R / 10], "--", label="Convergence line")  # Convergence line
plt.scatter(
    [flow1_rates_diff_RTT[0], flow1_rates_diff_RTT[-1]],
    [flow2_rates_diff_RTT[0], flow2_rates_diff_RTT[-1]],
    c="red",
    label="Start/End Points",
)  # Start and End points
plt.title("Flow$_2$ = 10 x Flow$_1$")
plt.xlabel("Time Steps")
plt.ylabel("Flow Rate")
plt.legend()

plt.tight_layout()
plt.savefig("flow.png")
