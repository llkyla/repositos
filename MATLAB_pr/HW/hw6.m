% Oscillatory Enzyme Reactions - Part (c)
clear; close all;

% Define parameter range
p_range = 1:9;

% Initialize array to store equilibrium solutions
S1_equilibria = zeros(size(p_range));

% Define function for fsolve
equilibrium_func = @(S, p) [
    c/(1 + alpha*S(4)^p) - k1*S(1);
    k1*S(1) - k2*S(2);
    k2*S(2) - k3*S(3);
    k3*S(3) - k4*S(4)
];

% Initial guess for fsolve
initial_guess = [1; 1; 1; 1];

% Iteratively compute equilibrium solutions for different p values
for i = 1:length(p_range)
    p = p_range(i);
    % Solve for equilibrium using fsolve
    S_eq = fsolve(@(S) equilibrium_func(S, p), initial_guess);
    S1_equilibria(i) = S_eq(1);
    % Update initial guess for next iteration
    initial_guess = S_eq;
end

% Plot S1 versus p
figure;
plot(p_range, S1_equilibria, 'o-', 'LineWidth', 2);
xlabel('$p$', 'Interpreter', 'latex', 'FontSize', 18);
ylabel('$S_1$', 'Interpreter', 'latex', 'FontSize', 18);
title('Equilibrium Solutions for $S_1$ versus $p$', 'Interpreter', 'latex', 'FontSize', 18);
grid on;

