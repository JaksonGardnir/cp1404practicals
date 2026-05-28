"""
Program to simulate gopher population over a number of years.
"""
import random

TIME_PERIOD = 10  # Years.
STARTING_POPULATION = 1000
GOPHER_BIRTH_RATE_RANGE = 10, 20  # Percentages.
GOPHER_DEATH_RATE_RANGE = 5, 25  # Percentages.


def main():
    """Simulate a population of gophers over TIME_PERIOD years."""
    print_gopher_simulation_welcome()
    gopher_population = STARTING_POPULATION
    for i in range(TIME_PERIOD):
        # The * unpacks the tuple into individual integers for use as arguments.
        gopher_birth_rate = random.randint(*GOPHER_BIRTH_RATE_RANGE)
        gopher_births = calculate_change_in_population(gopher_birth_rate, gopher_population)
        gopher_death_rate = random.randint(*GOPHER_DEATH_RATE_RANGE)
        gopher_deaths = calculate_change_in_population(gopher_death_rate, gopher_population)
        gopher_population = update_population(gopher_births, gopher_deaths, gopher_population)
        print_population_summary(gopher_births, gopher_deaths, gopher_population, i + 1)


def print_gopher_simulation_welcome():
    """Print the welcome message for the gopher population simulator."""
    print("Welcome to the Gopher Population Simulator!")
    print(f"Starting population: {STARTING_POPULATION}")


def update_population(births: int, deaths: int, current_population: int) -> int:
    """Update population based on births, deaths, and current population."""
    new_population = current_population + births - deaths
    return new_population


def calculate_change_in_population(percentage_rate: int, current_population: int) -> int:
    """Calculate the change in population based off a percentage rate."""
    change_in_population = int(current_population * percentage_rate / 100)
    return change_in_population


def print_population_summary(births: int, deaths: int, new_population: int, year: int):
    """Print a message detailing the year, number of births and deaths, and the new population."""
    print(f"End of year {year}: ")
    print(f"{births} were born. {deaths} died.")
    print(f"Population: {new_population}\n")


main()
