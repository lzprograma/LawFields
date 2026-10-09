OARA-3: Adaptive Relational Amplification Operator (Concept of Chirality)
From chiral symmetry breaking to the inertia of complex networks. A mathematical formalization in pure code to simulate phase transition dynamics, self-reinforcement, and topological locking in concurrent adaptive systems.
🔬 Overview
OARA-3 (Adaptive Relational Amplification Operator, Version 3) is a mathematical and computational framework designed to investigate how small asymmetries in nonlinear systems are amplified by feedback mechanisms until they dominate the global state of the system.
Inspired by phenomena of asymmetric autocatalysis (such as the Soai Reaction and the origin of homochirality in chemistry) and the dynamics of adaptive networks, OARA-3 generalizes the concept of “structural stubbornness”: the ability of a group of interconnected elements to resist contrary external evidence due to the mutual reinforcement of their internal relationships.
🌟 Implementation Highlights
Zero External Dependencies: Implemented in 100% pure Python (math and native types), with no need for numpy or scipy.
Native Spectral Analysis: Calculates the spectral gap ($\Delta \lambda$) of the connection matrix using the Power Iteration Method with Hotelling Deflation.
High-Precision Numerical Integration: Native 4th-order Runge-Kutta (RK4) differential solver.
Universal Phase Laws: Real-time monitoring of the fluid, critical (critical slowing down), and topological locking regimes.
📐 Mathematical Foundations
OARA-3 models the coupled evolution of a state vector in the probability simplex $\mathbf{p}(t) \in \Delta^{N-1}$ (where $\sum p_i = 1$) and a relational memory matrix $W(t) \in \mathbb{R}^{N \times N}$.
1. State Dynamics ($\mathbf{p}$)
The state vector evolves according to an amplified replicator equation:
$$\frac{dp_i}{dt} = \eta \, p_i \left( S_i(\mathbf{p}) - \bar{S}(\mathbf{p}) \right)$$
Where $S_i(\mathbf{p}) = \sum_j W_{ij} p_j$ is the relational strength of element $i$, and $\bar{S}(\mathbf{p}) = \mathbf{p}^T W \mathbf{p}$ is the average relational strength of the system.
2. Dynamics of Relational Memory ($W$)
The connection matrix evolves with gradual memory loss and internal Hebbian reinforcement:
$$\frac{dW_{ij}}{dt} = \rho \left( -W_{ij} + U_{ij} + \kappa \, p_i p_j \right)$$
Where $U_{ij}$ is the external perturbation matrix, $\kappa$ represents the self-reinforcing force of dominance, and $\rho$ is the relaxation rate.
3. The Law of Relational Inertia
The reversal delay time ($\tau$) required for the system to change state after the reversal of external evidence $A$ is dictated by the spectral gap $\Delta \lambda = \lambda_1 - \lambda_2$ of the symmetrized matrix $W_{sym}$:
$$\tau(\Delta \lambda, \kappa, A) = \frac{C}{\eta \, \rho} \cdot \frac{A}{\Delta \lambda \cdot A - \kappa}$$
RegimeConditionDynamic BehaviorFluid$\Delta \lambda \cdot A > \kappa$Smooth transition; the system adapts quickly to the new evidence. Critical Point$\Delta \lambda \cdot A \to \kappa^+$Divergence $\tau \to \infty$; decision paralysis (critical slowing down).Topological Lock-in$\Delta \lambda \cdot A \le \kappa$Irreversible hysteresis; the network structure locks in the current state.
🛠️ Repository Structure
Plaintext
.
├── simulator.py        # Complete source code (OARA-3 Engine, Linear Algebra, and CLI)
└── README.md           # Technical and scientific documentation for the project
🚀 How to Run
Since it uses only standard Python libraries, it runs immediately in any environment.
1. Clone the repository
Bash
git clone https://github.com/usuario/oara3-simulator.git
cd oara3-simulator
2. Run the simulator
Bash
python simulator.py
💻 Usage Example (CLI Interface)
When you start the program, you’ll have access to the interactive menu:
Plaintext
------------------------------------
OARA-3 Simulator
------------------------------------

1 - Simulate
2 - Law
3 - Authors

> 1
Simulation Output (Option 1)
The simulation runs 200 numerical steps, forcing a reversal of the external evidence at step 100:
Plaintext
--- Starting OARA-3 Simulation ---
Phase 1: External force favors Element 0 (Steps 0 to 100)
Step   0 | p[0]: 0.5000 | p[1]: 0.5000 | Spectral Gap (Δλ): 0.0000
Step  20 | p[0]: 0.7412 | p[1]: 0.2588 | Spectral Gap (Δλ): 0.1245
Step  40 | p[0]: 0.9120 | p[1]: 0.0880 | Spectral Gap (Δλ): 0.3512
Step  80 | p[0]: 0.9854 | p[1]: 0.0146 | Spectral Gap (Δλ): 0.4820
Phase 2: External force shifts to Element 1 (Steps 100 to 200)
Step 120 | p[0]: 0.8210 | p[1]: 0.1790 | Spectral Gap (Δλ): 0.1980
Step 140 | p[0]: 0.3102 | p[1]: 0.6898 | Spectral Gap (Δλ): 0.2104
Step 180 | p[0]: 0.0210 | p[1]: 0.9790 | Spectral Gap (Δλ): 0.4912
--- Simulation Complete ---
👥 Authors
Mr. Lunz — Principal Investigator & Operator Formulator
Tony / ChatGPT / Gemini — Contributor in Theoretical and Computational Physics
📄 License
This project is licensed under the Apache License 2.0—see the LICENSE file for more details.

Translated with DeepL.com (free version)
