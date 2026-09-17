# =====================
# black-hole-calculator
# =====================

# Physical constants
G = 6.67430e-11  # Gravitational constant (m³ kg⁻¹ s⁻²)
C = 299792458  # Speed of light in vacuum (m/s)
SOLAR_MASS = 1.989e30  # Solar mass (kg)


def get_user_input():
    """Get and validate the black hole mass from the user."""

    while True:
        mass = (
            input("\nBlack Hole Mass (in solar masses) or 'exit' to quit: ")
            .lower()
            .strip()
        )

        # Allow the user to exit the program.
        if mass == "exit":
            return None

        try:
            mass = float(mass)

            # Black hole mass must be greater than zero.
            if mass <= 0:
                print("\nPlease enter a positive value for mass.")
                continue

            return mass

        except ValueError:
            print("\nInvalid input. Please enter a numeric value for mass.")


def calculate_schwarzschild_radius(mass):
    """
    Calculate the Schwarzschild radius of a black hole.

    The Schwarzschild radius is the radius of the event horizon
    for a non-rotating, uncharged black hole.

    Formula:
        r = 2GM / c²

    The input mass is given in solar masses and is converted to kg.
    The result is returned in kilometres.
    """

    # Convert mass from solar masses to kilograms.
    mass_kg = mass * SOLAR_MASS

    # Calculate Schwarzschild radius in metres.
    radius = 2 * G * mass_kg / C**2

    # Convert metres to kilometres.
    radius_km = radius / 1000

    return radius_km


def classify_black_hole(mass):
    """Classify a black hole by mass using simplified theoretical ranges."""

    if mass < 3:
        return "Below typical stellar black-hole mass range."
    elif mass <= 100:
        return "Stellar-mass black hole."
    elif mass <= 100000:
        return "Intermediate-mass black hole."
    else:
        return "Supermassive black hole."


def display_result(mass):
    """Calculate and display the black hole's properties."""

    radius_km = calculate_schwarzschild_radius(mass)

    # The event horizon diameter is twice the Schwarzschild radius.
    diameter_km = 2 * radius_km

    classification = classify_black_hole(mass)

    print(f"\nSchwarzschild Radius: {radius_km:.2f} km")
    print(f"Event Horizon Diameter: {diameter_km:.2f} km")
    print(f"Classification: {classification}")


def main():
    """Run the black hole calculator."""

    while True:
        mass = get_user_input()

        # None indicates that the user chose to exit.
        if mass is None:
            print("\nExiting the program.")
            break

        display_result(mass)


# Run the calculator only when this file is executed directly.
# This allows the functions to be imported safely by test files.
if __name__ == "__main__":
    main()
