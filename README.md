
# 📊 Queue Simulation Project: M/M/1 – G/M/1 – M/G/1

This project simulates and analyzes the behavior of three classic queueing models:

- **M/M/1**: Exponential inter-arrival and service times
- **G/M/1**: General (Gamma) inter-arrival times, exponential service times
- **M/G/1**: Exponential inter-arrival times, general (Gamma) service times

We study the performance of each system by varying the arrival rate (λ) while keeping the service rate (μ) constant.

---

## 🎯 Objective

To understand the impact of **arrival and service time variability** on key performance metrics in a single-server queue:

- Average waiting time
- Average response time
- Server utilization (ρ)

---

## 🧪 Simulation Parameters

| Parameter       | Description                        |
|----------------|------------------------------------|
| `λ` (lambda)    | Arrival rate (varied from 0.1 to 0.9) |
| `μ` (mu)        | Service rate (fixed to 1.0)        |
| `n`             | Number of clients (1,000,000)      |
| `repeats`       | Repetitions per λ (3 times)        |
| `shape`         | Shape parameter for Gamma law (2)  |

---

## 📁 Files

| File         | Description                                      |
|--------------|--------------------------------------------------|
| `m_m_1.py`   | Simulation for the M/M/1 queue                   |
| `g_m_1.py`   | Simulation for the G/M/1 queue                   |
| `m_g_1.py`   | Simulation for the M/G/1 queue                   |
| `compare.py` | (Optional) Compare results on a single graph     |

---

## 📊 Performance Metrics

The simulation computes, for each λ:

- **Average waiting time** = `start_time - arrival_time`
- **Average response time** = `end_time - arrival_time`
- **Utilization ρ** = `λ / μ`

---

## 🛠 How it works

1. Generate inter-arrival times using Exponential or Gamma distribution
2. Compute arrival timestamps via cumulative sum (`np.cumsum`)
3. Generate service times (Exponential or Gamma)
4. Simulate queue behavior: start, end, wait, and response times
5. Repeat for all λ values and average over 3 runs

---

## 📈 Output

Each script generates performance plots:

- **Response time** vs λ
- **Waiting time** vs λ
- **Utilization** vs λ

These help to visually compare how each model reacts to increased load.

---

## ✅ Key Takeaways

- **M/M/1** is sensitive to high λ values (very variable).
- **G/M/1** performs best: regular arrivals stabilize the system.
- **M/G/1** is a compromise: stable services help, but randomness in arrivals still causes queuing.

---

## 📌 Author & Notes

Developed for a university course project on **Modelisation** and **Simulation**.  
All models assume a single-server queue with infinite buffer and FIFO order.

