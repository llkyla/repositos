clear;
close all;

load("CO2.mat");
load("t.mat");

% Vars
X = t(2: end) ;
Y = CO2(2: end) ;
S = (Y - CO2 (1) ) ./( X - t (1) ) ;

tspan = 1959:2010;
SM1 = 0.7*(1+(tspan-1959)./47);
CO2M1 = 316 + SM1.*(tspan-1959);

% Fig 1
figure(1)
plot(X, S, 'LineStyle', 'none', 'Marker', 'o', 'MarkerEdgeColor', 'k', 'MarkerFaceColor', 'k');
hold on;
plot(tspan, SM1, 'k', 'LineWidth', 1);

xlim ([1950 2010]);
ylim ([0 2]);
xticks (1950:10:2010); 
yticks (0:0.5:2); 

xlabel ( '$t$ ' , 'Interpreter' , 'latex') ;
ylabel ( '$S$ ' , 'Interpreter' , 'latex') ;

ax = gca ;
ax . FontSize = 16;

hold off;

% Fig 2
figure(2)
plot(t, CO2, 'LineStyle', 'none', 'Marker', 'o', 'MarkerEdgeColor', 'k', 'MarkerFaceColor', 'k');
hold on;
plot(tspan, CO2M1, 'k', 'LineWidth', 1);

xlim ([1950 2010]);
ylim ([300 400]);
xticks (1950:10:2010); 
yticks (310:20:390);

xlabel ( '$t$ ' , 'Interpreter' , 'latex') ;
ylabel ( '$CO_2$ ' , 'Interpreter' , 'latex') ;

ax = gca ;
ax . FontSize = 16;

hold off;

% Part 2
mean_X = mean(X);
eX = X - mean_X;
eS = S - mean(S);
optimal_S = mean(S) + sum(eX .* eS) / sum(eX.^2 .* (X - mean_X));

fun = @(x) 316 + (x(1) * (t - 1959) + x(2)) .* (t - 1959) - CO2;

x0 = [1, 1];

parfits = lsqnonlin(fun, x0);

CO2M2 = 316 + (parfits(1) * (t - 1959) + parfits(2)) .* (t - 1959);

% Fig 3
figure(3);
plot(t, CO2, 'o', 'DisplayName', 'CO2 Data');
hold on;
plot(t, CO2M2, '-', 'DisplayName', 'Quadratic Model');
xlabel('Year');
ylabel('CO2 Concentration');
legend('Location', 'best');
title('Optimized Quadratic Model for CO2 Concentration');

% Summary
% The first strategy computes the optimal model for S using the given formula.
% The second strategy uses lsqnonlin to directly optimize the quadratic function CO2(t)
% using the least-squares criterion. This involves defining an anonymous function that
% represents the difference between the model and data, setting an initial condition for
% parameters, and using lsqnonlin to find the optimal parameter values numerically.


