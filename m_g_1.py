import numpy as np
import matplotlib.pyplot as plt

MU = 1.0
NUM_CUSTOMERS = 1_000_000
REPEATS = 3
LAMBDA_VALUES = np.arange(0.1, 1.0, 0.1)

def simulate_mg1(lmbda, mu, n):
    inter_arrival_times = np.random.exponential(1 / lmbda, n)
    arrival_times = np.cumsum(inter_arrival_times)
    
    # Loi générale : Gamma avec même moyenne que Exp(1/μ)
    service_times = np.random.gamma(shape=2, scale=1 / (2 * mu), size=n)

    start_times = np.zeros(n)
    end_times = np.zeros(n)

    for i in range(1, n):
        start_times[i] = max(arrival_times[i], end_times[i - 1])
        end_times[i] = start_times[i] + service_times[i]

    wait_times = start_times - arrival_times
    response_times = end_times - arrival_times

    return response_times.mean(), wait_times.mean()

# Résultats
mg1_results = {
    "lambda": [],
    "response_time": [],
    "wait_time": [],
    "rho": []
}

for lmbda in LAMBDA_VALUES:
    responses, waits = [], []
    for _ in range(REPEATS):
        r, w = simulate_mg1(lmbda, MU, NUM_CUSTOMERS)
        responses.append(r)
        waits.append(w)
    
    mg1_results["lambda"].append(lmbda)
    mg1_results["response_time"].append(np.mean(responses))
    mg1_results["wait_time"].append(np.mean(waits))
    mg1_results["rho"].append(lmbda / MU)

# Tracé
plt.figure(figsize=(10, 6))
plt.plot(mg1_results["lambda"], mg1_results["response_time"], label="M/G/1 - Temps de réponse")
plt.plot(mg1_results["lambda"], mg1_results["wait_time"], label="M/G/1 - Temps d'attente")
plt.plot(mg1_results["lambda"], mg1_results["rho"], label="Taux d'occupation (ρ = λ/μ)")
plt.title("Résultats de la simulation M/G/1")
plt.xlabel("Taux d'arrivée (λ)")
plt.ylabel("Valeur moyenne")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
