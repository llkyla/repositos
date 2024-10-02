
% Problem 1
t = 1950:5:2005;
C = [34.616, 40.208, 45.087, 54.017, 67.844, 71.999, 78.122, 76.491, 84.652, 91.173, 98.975, 100.506];

    % 1(a)
    degree = 1; 
    coefficients_optimal = polyfit(t, C, degree);

    C_optimal = polyval(coefficients_optimal, t);

    % 1(b)
    figure(1);
    plot(t, C, 'o', t, C_optimal, '-', t, 91 + 1.25 * (t - 1995), '--');
    legend('Data', 'Optimal Model', 'Given Model', 'Location', 'Best');
    xlabel('Year (t)');
    ylabel('C');
    title('Optimal Model vs Given Model');

    % 1(c)
    residuals_optimal = C - C_optimal;
    mse_optimal = mean(residuals_optimal.^2);
    disp(['Mean Squared Error (Optimal Model): ', num2str(mse_optimal)]);

% Problem 2
t = 1790:10:2050;
P = [0.0039, 0.0053, 0.0072, 0.0096, 0.0129, 0.0171, 0.0232, 0.0314, 0.0398, 0.0502, 0.063, 0.0762, 0.0922, 0.106, 0.1232, 0.1321, 0.1513, 0.1793, 0.2033, 0.2265, 0.2487, 0.2814, 0.3102, 0.3414, 0.3735, 0.4057, 0.439];

% 2(a)
y = log(P);
x = (t - 1790) / 35;

% 2(b)
coefficients_optimal = polyfit(x, y, 1);

% 2(c)
figure(2);
plot(t, P, 'o', t, exp(polyval(coefficients_optimal, x)), '-', t, 0.0039 * exp((t - 1790) / 35), '--');
legend('Data', 'Optimal Model', 'Given Model', 'Location', 'Best');
xlabel('Year (t)');
ylabel('Population (P)');
title('Optimal Model vs Given Model');

% 2(d)
residuals_optimal = P - exp(polyval(coefficients_optimal, x));
mse_optimal = mean(residuals_optimal.^2);
disp(['Mean Squared Error (Optimal Model): ', num2str(mse_optimal)]);