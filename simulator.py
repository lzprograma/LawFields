import math

class OperadorOARA:
    def __init__(self, N, eta=0.05, rho=0.01, kappa=0.5):
        """Initializes system dimension, parameters, state probability vector p, and weight matrix W."""
        self.N = N
        self.eta = eta
        self.rho = rho
        self.kappa = kappa
        
        self.p = [1.0 / N for _ in range(N)]
        self.W = [[0.0 for _ in range(N)] for _ in range(N)]
        
    def _derivadas(self, p, W, U):
        """Computes rate of change dp/dt for state vector and dW/dt for weight matrix under external matrix U."""
        S = [0.0] * self.N
        for i in range(self.N):
            S[i] = sum(W[i][j] * p[j] for j in range(self.N))
            
        S_mean = sum(p[i] * S[i] for i in range(self.N))
        
        dp_dt = [self.eta * p[i] * (S[i] - S_mean) for i in range(self.N)]
        
        dW_dt = [[0.0] * self.N for _ in range(self.N)]
        for i in range(self.N):
            for j in range(self.N):
                Phi_ij = p[i] * p[j]
                dW_dt[i][j] = self.rho * (-W[i][j] + U[i][j] + self.kappa * Phi_ij)
                
        return dp_dt, dW_dt

    def step(self, U, dt=0.1):
        """Advances state vector p and matrix W by time increment dt using 4th-order Runge-Kutta integration."""
        def soma_vetor(v1, v2, mult=1.0):
            return [a + b * mult for a, b in zip(v1, v2)]
            
        def soma_matriz(m1, m2, mult=1.0):
            return [[m1[i][j] + m2[i][j] * mult for j in range(self.N)] for i in range(self.N)]

        p_k1, W_k1 = self._derivadas(self.p, self.W, U)
        
        p_temp = soma_vetor(self.p, p_k1, 0.5 * dt)
        W_temp = soma_matriz(self.W, W_k1, 0.5 * dt)
        p_k2, W_k2 = self._derivadas(p_temp, W_temp, U)
        
        p_temp = soma_vetor(self.p, p_k2, 0.5 * dt)
        W_temp = soma_matriz(self.W, W_k2, 0.5 * dt)
        p_k3, W_k3 = self._derivadas(p_temp, W_temp, U)
        
        p_temp = soma_vetor(self.p, p_k3, dt)
        W_temp = soma_matriz(self.W, W_k3, dt)
        p_k4, W_k4 = self._derivadas(p_temp, W_temp, U)
        
        soma_p = 0.0
        for i in range(self.N):
            delta_p = (dt / 6.0) * (p_k1[i] + 2*p_k2[i] + 2*p_k3[i] + p_k4[i])
            self.p[i] = max(1e-12, self.p[i] + delta_p) 
            soma_p += self.p[i]
            
            for j in range(self.N):
                delta_W = (dt / 6.0) * (W_k1[i][j] + 2*W_k2[i][j] + 2*W_k3[i][j] + W_k4[i][j])
                self.W[i][j] += delta_W
                
        self.p = [x / soma_p for x in self.p]

    def _iteracao_potencia(self, matriz, iteracoes=50):
        """Finds dominant eigenvalue and associated eigenvector using Power Iteration method."""
        v = [1.0] * self.N
        lambda_max = 0.0
        
        for _ in range(iteracoes):
            v_new = [sum(matriz[i][j] * v[j] for j in range(self.N)) for i in range(self.N)]
            norma = math.sqrt(sum(x * x for x in v_new))
            if norma == 0: break
            
            v = [x / norma for x in v_new]
            v_mat_v = sum(v[i] * sum(matriz[i][j] * v[j] for j in range(self.N)) for i in range(self.N))
            lambda_max = v_mat_v
            
        return lambda_max, v

    def gap_espectral(self):
        """Calculates spectral gap Delta_lambda = lambda_1 - lambda_2 of symmetrized matrix W via Hotelling deflation."""
        W_sym = [[0.5 * (self.W[i][j] + self.W[j][i]) for j in range(self.N)] for i in range(self.N)]
        
        lambda_1, v1 = self._iteracao_potencia(W_sym)
        
        W_def = [[W_sym[i][j] - lambda_1 * (v1[i] * v1[j]) for j in range(self.N)] for i in range(self.N)]
        lambda_2, _ = self._iteracao_potencia(W_def)
        
        return lambda_1 - lambda_2


def simular():
    """Executes time-series simulation under perturbation to measure state reversal delay and spectral gap."""
    N = 2
    op = OperadorOARA(N=N, eta=0.05, rho=0.01, kappa=0.5)
    
    # Perturbation matrix favoring element 0
    U_favor_0 = [[1.0, -1.0], [-1.0, -1.0]]
    # Perturbation matrix favoring element 1
    U_favor_1 = [[-1.0, -1.0], [-1.0, 1.0]]
    
    print("\n--- Starting OARA-3 Simulation ---")
    print("Phase 1: External force favors Element 0 (Steps 0 to 100)")
    
    for step in range(200):
        current_U = U_favor_0 if step < 100 else U_favor_1
        op.step(current_U, dt=0.2)
        
        if step % 20 == 0:
            gap = op.gap_espectral()
            print(f"Step {step:3d} | p[0]: {op.p[0]:.4f} | p[1]: {op.p[1]:.4f} | Spectral Gap (Δλ): {gap:.4f}")
            
    print("--- Simulation Complete ---\n")


def exibir_lei():
    """Displays analytical formulation and critical regimes of Relational Inertia Law (OARA-3)."""
    print("""
========================================================================
                      RELATIONAL INERTIA LAW (OARA-3)
========================================================================
Analytical equation for Reversal Delay Time (tau):

         tau(Δλ, κ, A) = (C / (η * ρ)) * (A / (Δλ * A - κ))

Where:
  - Δλ : Spectral Gap (λ1 - λ2) of Symmetrized Weight Matrix W
  - A  : Magnitude of Opposing External Evidence
  - κ  : Internal Self-Reinforcement Rate
  - η  : State Amplification Intensity
  - ρ  : Relational Memory Relaxation Rate

Regimes:
  1. Fluid Regime    (Δλ * A > κ) : Fast adaptation to external evidence.
  2. Critical Point  (Δλ * A -> κ): Critical slowing down; tau approaches infinity.
  3. Locked Regime   (Δλ * A <= κ): Structural hysteresis; topological state lockup.
========================================================================
""")


def exibir_autores():
    """Prints authors and project credits."""
    print("""
========================================================================
                             OARA-3 AUTHORS
========================================================================
  - Sr. Lunz (Principal Investigator)
  - Tony / ChatGPT / Gemini (Theoretical & Computational Physics Collaborator)
========================================================================
""")


def main():
    """Handles CLI menu display and option execution."""
    print('''
------------------------------------
Simulator OARA-3
------------------------------------

1 - Simulation
2 - Law
3 - Authors
''')
    options = input("> ").strip()
    
    if options == '1':
        simular()
    elif options == '2':
        exibir_lei()
    elif options == '3':
        exibir_autores()
    else:
        print("Opção inválida.")

if __name__ == "__main__":
    main()
