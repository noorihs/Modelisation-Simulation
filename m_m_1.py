import numpy as np
import matplotlib.pyplot as plt

# Paramètres constants
MU = 1.0  # Taux de service (fixe à 1)
NUM_CUSTOMERS = 1_000_000  # Nombre de clients simulés
REPEATS = 3  # Nombre de répétitions pour la stabilité statistique

LAMBDA_VALUES = np.arange(0.1, 1.0, 0.1)  # Valeurs de λ testées (de 0.1 à 0.9)

# Fonction de simulation M/M/1
def simulate_mm1(lmbda, mu, n):
    arrival_times = np.cumsum(np.random.exponential(1 / lmbda, n))
    service_times = np.random.exponential(1 / mu, n)

    start_times = np.zeros(n)
    end_times = np.zeros(n)

    for i in range(1, n):
        start_times[i] = max(arrival_times[i], end_times[i - 1])
        end_times[i] = start_times[i] + service_times[i]

    wait_times = start_times - arrival_times
    response_times = end_times - arrival_times

    return response_times.mean(), wait_times.mean()

# Résultats
results = {
    "lambda": [],
    "response_time": [],
    "wait_time": [],
    "rho": []
}

for lmbda in LAMBDA_VALUES:
    responses, waits = [], []
    for _ in range(REPEATS):
        r, w = simulate_mm1(lmbda, MU, NUM_CUSTOMERS)
        responses.append(r)
        waits.append(w)
    
    results["lambda"].append(lmbda)
    results["response_time"].append(np.mean(responses))
    results["wait_time"].append(np.mean(waits))
    results["rho"].append(lmbda / MU)

# Tracé des résultats
plt.figure(figsize=(10, 6))
plt.plot(results["lambda"], results["response_time"], label="Temps de réponse moyen")
plt.plot(results["lambda"], results["wait_time"], label="Temps d'attente moyen")
plt.plot(results["lambda"], results["rho"], label="Taux d'occupation (ρ = λ/μ)")
plt.title("Résultats de la simulation M/M/1")
plt.xlabel("Taux d'arrivée (λ)")
plt.ylabel("Valeur moyenne")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
