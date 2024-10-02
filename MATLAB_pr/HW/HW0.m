
% Problem A.6
x = 0:.1:1;
A = [x; exp(x); log(x+1)];

fileID = fopen('mytable.txt','w');
fprintf(fileID,'%6s %12s\n','x','exp(x)');
fprintf(fileID,'%6.2f %12.8f\n',A);
fclose(fileID);

% Problem A.7
figure(1)
x = -2:2;c
y1 = exp(x);
plot(x, y1, 'r');

hold on

y2 = 1 + x + x.^2/2 + x.^3/6;
plot(x, y2, 'b--');

hold off

% Problem 9
m = 5; n = 5; A = zeros(m,n);

for i=1:m
    for j=1:n
        A(i,j) = i * j;
    end
end

A

% Problem 11
bal = [0, 1000, 5000, 200000, 600000];

for i = 1:length(bal)
    if bal(i) < 5000
        bal(i) = bal(i) * 1.01;
    elseif (bal(i) >= 5000) && (bal(i) < 20000) 
        bal(i) = bal(i) * 1.02;
    elseif bal(i) > 20000
        bal(i) = bal(i) * 1.05;
    end
end

bal

% Problem 14
unit = input('Temperature Unit in F or C: ', 's');
temp = str2double(input('Temperature: ', 's'));

if (unit == 'F') || (unit == 'f') % if inputted unit is F or f
    FtoC = (temp - 32) * (5/9);
    
    figure(2)
    plot(temp, FtoC, 'ro-');
    xlabel('Temperature F');
    ylabel('Temperature C');
    grid on;

elseif (unit == 'C') || (unit == 'c') % if inputted unit is C or c
    CtoF = temp * (9/5) + 32;

    figure(3)
    plot(temp, CtoF, 'bo-');
    xlabel('Temperature C');
    ylabel('Temperature F');
    grid on;
end

% Problem 15
f = @(x) x.^3;
g = @(x) cos(x);

x = -10:10;

% Initialize fg and gf before calling compositefun
fg = zeros(size(x));
gf = zeros(size(x));

[fg, gf] = compositefun(f, g, x);

figure(4)
plot(x, fg, 'r-', 'DisplayName', 'f(g(x))');
hold on
plot(x, gf, 'b--', 'DisplayName', 'g(f(x))');
xlabel('x');
ylabel('y');
title('Composite Function');
legend('show');
grid on;
hold off;

function [fg, gf] = compositefun(f, g, x)
    fg = f(g(x));
    gf = g(f(x));
end

