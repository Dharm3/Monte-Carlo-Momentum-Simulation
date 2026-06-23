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