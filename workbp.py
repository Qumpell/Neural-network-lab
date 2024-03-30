import numpy as np

# Funkcja aktywacji sigmoidalna
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Pochodna funkcji aktywacji sigmoidalnej
def sigmoid_derivative(x):
    return x * (1 - x)

# Pseudokod algorytmu
def backpropagation(input_data, expected_output, w_hidden, w_output, eta, epochs):
    for epoch in range(epochs):
        # Przekazywanie sygnału w przód
        hidden_input = np.dot(input_data, w_hidden)
        hidden_output = sigmoid(hidden_input)
        output_input = np.dot(hidden_output, w_output)
        output_output = sigmoid(output_input)

        # Obliczanie błędu propagacji wstecznej dla warstwy wyjściowej
        delta_output = (expected_output - output_output) * sigmoid_derivative(output_output)

        # Obliczanie błędu propagacji wstecznej dla warstwy ukrytej
        delta_hidden = np.dot(delta_output, w_output.T) * sigmoid_derivative(hidden_output)

        # Aktualizacja wag
        w_output += np.dot(hidden_output.T, delta_output) * eta
        w_hidden += np.dot(input_data.T, delta_hidden) * eta

        # Wypisz postęp co każde 100 epok
        if epoch % 100 == 0:
            print(f'Epoka {epoch}, Błąd: {np.mean(np.abs(delta_output))}')

    return w_hidden, w_output, output_output

# Przykładowe dane wejściowe
input_data = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
# Przykładowe oczekiwane wyniki (musi mieć kształt (4, 1))
expected_output = np.array([[0], [1], [1], [0]])
# Losowe inicjalizowanie wag

w_hidden = np.array([[0.0, 1.0, 2.0], [0.0, 1.0, 2.0]])
w_output = np.array([[0.0],[1.0], [2.0]])
# Parametry uczenia
eta = 0.5
epochs = 1

# Uruchom algorytm propagacji wstecznej
trained_w_hidden, trained_w_output, output_output = backpropagation(input_data, expected_output, w_hidden, w_output, eta, epochs)

print("Wagi warstwy ukrytej po treningu:")
print(trained_w_hidden)
print("Wagi warstwy wyjściowej po treningu:")
print(trained_w_output)
print("Końcowy wynik:")
print(output_output)
