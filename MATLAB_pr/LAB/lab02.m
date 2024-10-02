% lab 02

% 1
tspan = [0 5];
y0 = 0;
[t, y] = ode45(@(t,y) 2*t, tspan, y0);
figure(1);
plot(t, y, '-o') 

% 2
[t , y ] = ode45 (@ vdp1 ,[0 20] ,[2; 0]) ;
figure(2);
plot (t , y (: ,1) , ' -o ' ,t , y (: ,2) , ' -o ')

% 3

% Solve the ODEs using ode45
tspan = [0, 20];
initial_conditions = [initial_H_value; initial_M_value]; % Set your initial conditions
[t, y] = ode45(@(t, y) mammoth(t, y), tspan, initial_conditions);

% Plot the solutions for H and M against t
figure(3);
plot(t, y(:, 1), '-o', t, y(:, 2), '-o');
xlabel('Time');
ylabel('Population');
legend('H', 'M');
title('Mammoth Population Dynamics');