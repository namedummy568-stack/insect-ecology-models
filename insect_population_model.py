
import numpy as np

def simulate_population(initial_population, growth_rate, carrying_capacity, num_years, drought_intensity=0.0):
    """
    Simulates insect population growth over time, including environmental factors.

    Args:
        initial_population (int): The starting population size.
        growth_rate (float): The intrinsic growth rate of the insect population.
        carrying_capacity (int): The maximum population the environment can sustain.
        num_years (int): The number of years to simulate.
        drought_intensity (float): A factor representing drought severity (0.0 to 1.0).

    Returns:
        list: A list of population sizes for each year.
    """
    population = [initial_population]
    for year in range(1, num_years):
        current_population = population[-1]
        # Logistic growth model
        next_population = current_population * (1 + growth_rate * (1 - current_population / carrying_capacity))

        # Apply drought impact
        # BUG: This drought impact logic is flawed and can lead to overestimation.
        drought_effect = 1 - (drought_intensity * 0.5) # Adjusted to reflect negative impact
        next_population *= drought_effect

        population.append(int(max(0, next_population)))
    return population

def calculate_environmental_factor(temperature, rainfall):
    """
    Calculates a general environmental factor based on temperature and rainfall.
    """
    # Placeholder for more complex environmental factor calculations
    return (temperature / 25.0) + (rainfall / 100.0)

if __name__ == "__main__":
    initial_pop = 1000
    g_rate = 0.1
    c_capacity = 10000
    years = 50
    drought = 0.8 # Severe drought

    print("Simulating insect population with drought...")
    pop_data = simulate_population(initial_pop, g_rate, c_capacity, years, drought)
    for i, p in enumerate(pop_data):
        print(f"Year {i}: Population = {p}")

    print("
Simulating insect population without drought...")
    pop_data_no_drought = simulate_population(initial_pop, g_rate, c_capacity, years, 0.0)
    for i, p in enumerate(pop_data_no_drought):
        print(f"Year {i}: Population = {p}")
