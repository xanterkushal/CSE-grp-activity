def calculate_volume(V1, P1, P2):
    V2 = (V1 * P1) / P2
    return V2

# Example usage
initial_volume = 10.0  # Initial volume (V1)
initial_pressure = 2.0  # Initial pressure (P1)
new_pressure = 4.0  # New pressure (P2)

resulting_volume = calculate_volume(initial_volume, initial_pressure, new_pressure)
print("The resulting volume is:", resulting_volume)
