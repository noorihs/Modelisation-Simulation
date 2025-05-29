import numpy as np
import matplotlib.pyplot as plt

# Paramètres généraux
MU = 1.0  # Taux de service
NUM_CUSTOMERS = 1_000_000
REPEATS = 3
LAMBDA_VALUES = np.arange(0.1, 1.0, 0.1)

# Fonction de simulation générique pour les files mono-serveur
def simulate_queue(arrival_gen, service_gen, n):
    arrival_times = np.cumsum(arrival_gen(n))
    service_times = service_gen(n)
    start_times = np.zeros(n)
    end_times = np.zeros(n)

    for i in range(1, n):
        start_times[i] = max(arrival_times[i], end_times[i-1])
        end_times[i] = start_times[i] + service_times[i]

    wait_times = start_times - arrival_times
    response_times = end_times - arrival_times

    return response_times.mean(), wait_times.mean()

# Simulation de M/M/1
results_mm1 = {"lambda": [], "response_time": [], "wait_time": [], "rho": []}

for lmbda in LAMBDA_VALUES:
    responses = []
    waits = []
    for _ in range(REPEATS):
        resp, wait = simulate_queue(
            arrival_gen=lambda n: np.random.exponential(1/lmbda, n),
            service_gen=lambda n: np.random.exponential(1/MU, n),
            n=NUM_CUSTOMERS
        )
        responses.append(resp)
        waits.append(wait)
    results_mm1["lambda"].append(lmbda)
    results_mm1["response_time"].append(np.mean(responses))
    results_mm1["wait_time"].append(np.mean(waits))
    results_mm1["rho"].append(lmbda / MU)

# Simulation de G/M/1 (arrivées gamma)
results_gm1 = {"lambda": [], "response_time": [], "wait_time": [], "rho": []}

for lmbda in LAMBDA_VALUES:
    responses = []
    waits = []
    for _ in range(REPEATS):
        resp, wait = simulate_queue(
            arrival_gen=lambda n: np.random.gamma(shape=2, scale=1/(2*lmbda), size=n),
            service_gen=lambda n: np.random.exponential(1/MU, n),
            n=NUM_CUSTOMERS
        )
        responses.append(resp)
        waits.append(wait)
    results_gm1["lambda"].append(lmbda)
    results_gm1["response_time"].append(np.mean(responses))
    results_gm1["wait_time"].append(np.mean(waits))
    results_gm1["rho"].append(lmbda / MU)

# Simulation de M/G/1 (services gamma)
results_mg1 = {"lambda": [], "response_time": [], "wait_time": [], "rho": []}

for lmbda in LAMBDA_VALUES:
    responses = []
    waits = []
    for _ in range(REPEATS):
        resp, wait = simulate_queue(
            arrival_gen=lambda n: np.random.exponential(1/lmbda, n),
            service_gen=lambda n: np.random.gamma(shape=2, scale=1/(2*MU), size=n),
            n=NUM_CUSTOMERS
        )
        responses.append(resp)
        waits.append(wait)
    results_mg1["lambda"].append(lmbda)
    results_mg1["response_time"].append(np.mean(responses))
    results_mg1["wait_time"].append(np.mean(waits))
    results_mg1["rho"].append(lmbda / MU)

# Fonction de tracé des résultats
def plot_results(results, title_prefix):
    plt.plot(results["lambda"], results["response_time"], label=f"{title_prefix} - Temps de réponse")
    plt.plot(results["lambda"], results["wait_time"], label=f"{title_prefix} - Temps d'attente")
    plt.plot(results["lambda"], results["rho"], label=f"{title_prefix} - Taux d'occupation")

plt.figure(figsize=(12, 8))
plot_results(results_mm1, "M/M/1")
plot_results(results_gm1, "G/M/1 ")
plot_results(results_mg1, "M/G/1 ")
plt.title("Comparaison des modèles M/M/1, G/M/1 et M/G/1")
plt.xlabel("Taux d'arrivée (lambda)")
plt.legend()
plt.grid(True)
plt.ylabel("Valeurs moyennes")
plt.tight_layout()
plt.show()
