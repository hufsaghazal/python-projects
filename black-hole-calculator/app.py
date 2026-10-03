# =====================
# black-hole-calculator
# =====================

import gradio as gr

css = """
.gradio-container {
    max-width: 800px;
    margin: auto;
    text-align: center;
}
"""

# Physical constants
G = 6.67430e-11  # Gravitational constant (m³ kg⁻¹ s⁻²)
C = 299792458  # Speed of light in vacuum (m/s)
SOLAR_MASS = 1.989e30  # Solar mass (kg)


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

    if mass is None:
        return "Please enter a mass."

    if mass <= 0:
        return "Please enter a positive value for mass."

    radius_km = calculate_schwarzschild_radius(mass)

    # The event horizon diameter is twice the Schwarzschild radius.
    diameter_km = 2 * radius_km

    classification = classify_black_hole(mass)

    return (
        f"### 🕳️ Schwarzschild Radius\n"
        f"**{radius_km:.2f} km**\n\n"
        f"### ⭕ Event Horizon Diameter\n"
        f"**{diameter_km:.2f} km**\n\n"
        f"### 🌌 Classification\n"
        f"**{classification}**"
    )


# =====================
# Gradio Interface
# =====================

demo = gr.Blocks()

with demo:
    gr.Markdown("# 🕳️ Black Hole Calculator")
    gr.Markdown("Calculate a black hole's size from its mass.")

    mass = gr.Number(
        label="BLACK HOLE MASS",
        info="Enter mass in solar masses",
    )

    button = gr.Button("🔭 Calculate")

    output = gr.Markdown("### Enter a mass to begin.")

    button.click(
        fn=display_result,
        inputs=mass,
        outputs=output,
    )


if __name__ == "__main__":
    demo.launch(css=css)
