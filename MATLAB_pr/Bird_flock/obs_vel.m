function dvdt = obs_vel(f, l, x, x_h, v_h, t, t_del, dt, C_ali, C_att, C_rep, ep, M, obstacle_pos, obstacle_radius)
    if t >= t_del
        x_del = x_h(:,:,round((t-t_del)/dt)+1);
        v_del = v_h(:,:,round((t-t_del)/dt)+1);
    
        %% Find each bird's M nearest neighbors
        dist = zeros(length(f)); % dist(i,j) = distance between birds i & j
        for i = 1:length(f)
            dist(i,:) = sqrt(sum((x_del-x_del(i,:)).^2,2));
        end
        dist(dist==0) = Inf;
        [~,dist_index] = sort(dist,2);
        n_n = dist_index(:,1:M); % Each bird's M nearest neighbors

        % Obstacle avoidance
        avoid_force = zeros(size(x));
        for i = 1:length(f)
            if norm(x(i,:) - obstacle_pos) < obstacle_radius
                % Calculate avoidance force away from the obstacle
                avoid_force(i,:) = (x(i,:) - obstacle_pos) / norm(x(i,:) - obstacle_pos);
            end
        end

        dvdt = alignment(f,l,x_del,v_del,C_ali,C_att,C_rep,ep,n_n,M) ...
            +attraction(f,l,x_del,v_del,C_ali,C_att,C_rep,ep,n_n,M) ...
            +repulsion(f,l,x_del,v_del,C_ali,C_att,C_rep,ep,n_n,M) ...
            + avoid_force;  % Add obstacle avoidance force
    else
        dvdt = zeros(length(f),2); % Change to 2D
    end
end
