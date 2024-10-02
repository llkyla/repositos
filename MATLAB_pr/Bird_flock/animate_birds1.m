function animate_birds1(x_h,dt)
    figure
    fig = gcf;
    
    for i = 1:round(size(x_h,3)/100)
        clf(fig)
        
        plot(x_h(:,1,i*100), x_h(:,2,i*100), ".", 'MarkerSize', 15);
        hold on

        xlim([min(min(x_h(:,1,:))) max(max(x_h(:,1,:)))]);
        ylim([min(min(x_h(:,2,:))) max(max(x_h(:,2,:)))]);
        
        xlabel('X')
        ylabel('Y')
        title(['t = ' num2str((i-1)*dt*100)]);
        
        pause(0.0001);

        hold off
    end
end
