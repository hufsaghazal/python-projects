# 🕳️ Black Hole Calculator

A Python-based web calculator for exploring basic black-hole properties from mass. The application uses Gradio to provide a simple interactive interface.

## Features

* Schwarzschild radius calculation
* Event-horizon diameter calculation
* Mass-based classification
* Input validation and error handling
* Interactive Gradio web interface

## Physics

The Schwarzschild radius is calculated using:

$$
r_s = \frac{2GM}{c^2}
$$

The event-horizon diameter is calculated using:

$$
d = 2r_s
$$

The calculation assumes an idealized non-rotating, uncharged black hole.

## Example

```text
Black Hole Mass: 10

Schwarzschild Radius: 29.54 km
Event Horizon Diameter: 59.08 km
Classification: Stellar-mass black hole.
```

## Requirements

* Python 3
* Gradio

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the application:

```bash
python app.py
```

A Gradio interface will open where you can enter the black hole mass in solar masses.

## Project Structure

```text
black-hole-calculator/
├── app.py
├── requirements.txt
└── README.md
```

## Note

The mass classifications are simplified theoretical ranges intended for educational purposes.
