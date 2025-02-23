import matplotlib.pyplot as plt

# Define the Alliance payoffs (UK (player 1), China (Player 2))
payoffs = {
    'a': {'a': (1, 1), 'n': (-1, 0)}, 
    'n': {'a': (0, -2), 'n': (0, 0)} 
}

# Compute best response for Player 1
a_probabilities = [i / 100 for i in range(101)]
best_response_1 = [
    'a' if p2_a * payoffs['a']['a'][0] + (1 - p2_a) * payoffs['a']['n'][0] >
           p2_a * payoffs['n']['a'][0] + (1 - p2_a) * payoffs['n']['n'][0]
    else 'n'
    for p2_a in a_probabilities
]

# Convert strategy choices into numeric values for plotting
best_response_1_numeric = [1 if br == 'a' else 0 for br in best_response_1]

print(round(sum(best_response_1_numeric)/ len(best_response_1_numeric), 3))

plt.plot(a_probabilities, best_response_1_numeric, label="Best response of the UK")
plt.xlabel("Probability of China tightening alliance")
plt.ylabel("Best response (1 = a, 0 = n)")
plt.title("Best Response Function for the UK")
plt.legend()
plt.show()

# Compute best response for Player 2
best_response_2 = [
    'a' if p1_a * payoffs['a']['a'][1] + (1 - p1_a) * payoffs['n']['a'][1] >
           p1_a * payoffs['a']['n'][1] + (1 - p1_a) * payoffs['n']['n'][1]
    else 'n'
    for p1_a in a_probabilities
]

# Convert strategy choices into numeric values for plotting
best_response_2_numeric = [1 if br == 'a' else 0 for br in best_response_2]

print(round(sum(best_response_2_numeric)/ len(best_response_2_numeric), 3))

plt.plot(a_probabilities, best_response_2_numeric, label="Best response of China")
plt.xlabel("Probability of the UK tightening alliance")
plt.ylabel("Best response (1 = a, 0 = n)")
plt.title("Best Response Function for China")
plt.legend()
plt.show()
