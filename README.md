# 🔵🔴 2D Momentum & Kinematics Simulator

A custom-built, Python-based physics engine designed to simulate 2D oblique collisions, momentum conservation, and kinetic energy transfer.

## Project Overview:
This simulator operates in two distinct modes to explore classical mechanics and statistical probability:
1. **Deterministic Mode (Pygame):** A real-time visualizer for 2D collisions. It features dynamic velocity vectors, surface friction deceleration, and live kinetic energy tracking.

2. **Stochastic Mode (Monte Carlo / Matplotlib):** An analytical engine that injects real-world uncertainty (standard deviation and measurement errors) into the mass and velocity variables. It bypasses the visual frame rate to calculate 5,000 alternate realities in a split second, generating a statistical "Blast Zone" scatter plot of the final velocities.

## Installation & Requirements
Ensure you have Python 3.x installed, then install the required dependencies:
```bash
pip install pygame matplotlib

Simulator Controls:
    - SPACE - Start the visual Pygame simulation
    - R - Reset balls to their starting positions
    - 1 / 2 - Select the Blue Ball (1) or Red Ball (2) to edit its properties
    - E / Q - Increase / Decrease Mass of the selected ball
    - D / A - Increase / Decrease Velocity of the selected ball
    - , / . - Rotate the impact angle vector of the selected ball
    - W / S - Adjust the Coefficient of Restitution (e)
    - Up / Down - Adjust the starting displacement between the balls
    - Right / Left - Adjust the surface friction ($\mu$)
    - M - Trigger the Monte Carlo Statistical Analysis (Runs 5,000 randomized impacts and plots the data)

Core Physics Concepts Are Handled Well:
    - Conservation of Momentum: Analyzes normal and tangential vectors during oblique impacts.
    - Coefficient of Restitution (e): Simulates perfectly elastic (e=1) to perfectly inelastic (e=0) collisions.
    - Work-Energy Principle: Calculates the exact frame-by-frame deceleration of the masses as kinetic energy is lost to surface friction.