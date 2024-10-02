function obs_birds(x_h, dt, obstacle_pos, obstacle_radius)
    figure
    fig = gcf;
    
    for i = 1:round(size(x_h, 3) / 100)
        clf(fig)
        
        plot(x_h(:, 1, i * 100), x_h(:, 2, i * 100), ".", 'MarkerSize', 30);
        hold on

        % Plot obstacle
        th = 0:pi/50:2*pi;
        x_circle = obstacle_radius * cos(th) + obstacle_pos(1);
        y_circle = obstacle_radius * sin(th) + obstacle_pos(2);
        plot(x_circle, y_circle, 'r', 'LineWidth', 2);

        xlim([min(min(x_h(:, 1, :))) max(max(x_h(:, 1, :)))]); % Set x-axis limits
        ylim([min(min(x_h(:, 2, :))) max(max(x_h(:, 2, :)))]); % Set y-axis limits
        
        xlabel('X')
        ylabel('Y')
        title(['t = ' num2str((i - 1) * dt * 100)]);
        
        pause(0.0001);

        hold off
    end
end
