classdef Boid
    
    properties
        position
        velocity
        acceleration
        r
        max_speed
        max_force
    end
    
    methods
        function obj = Boid(position_x,  position_y)
            obj.acceleration = [0 0];
            
            angle = (2*pi).*rand;
            obj.velocity = [cos(angle), sin(angle)];
            
            obj.position = [position_x, position_y];
            obj.r = 0;
            obj.max_speed = 3.0;
            obj.max_force = 0.3;
        end
        
        
        function obj = apply_force(obj, sep_force, coh_force,  ali_force)
            obj.acceleration = obj.acceleration+sep_force+coh_force+ali_force;
        end
        
        
        function obj = flock(obj,boids)
            
            ali = obj.align(boids);
            coh = obj.cohesion(boids);
            sep = obj.seperate(boids);
                
            sep = sep.*3.0;  % Csep
            ali = ali.*1.0;  % Cali
            coh = coh.*7.0; % Ccoh
            
            obj=obj.apply_force(sep,coh,ali);
        end
        
        function obj = borders(obj, lattice_size)
            if obj.position(1) < -obj.r
                obj.position(1)=lattice_size(1)+obj.r;
            end
            
            if obj.position(2) < -obj.r
                obj.position(2)=lattice_size(2)+obj.r;
            end
            
            if obj.position(1) > lattice_size(1) + obj.r
                obj.position(1)=-obj.r;
            end
            
            if obj.position(2) > lattice_size(2) + obj.r
                obj.position(2)=-obj.r;
            end
        end
        
        function obj = update(obj)
            obj.velocity = obj.velocity + obj.acceleration;
            obj.velocity = obj.velocity./norm(obj.velocity).*obj.max_speed;
            obj.position = obj.position + obj.velocity;
            obj.acceleration = [0 0];
        end
        
        function [steer] = seek(obj, target)
            desired = target - obj.position;
            desired = norm(desired);
            desired = desired*obj.max_speed;
            
            steer = desired-obj.velocity;
            steer = steer./norm(steer).*obj.max_force;
        end
        
        function [steer] = seperate(obj, boids)
            neighbor_dist = 100.0;
            steer = [0,0];
            count = 0;
            sum = [0,0];
            positions = zeros(2,length(boids));
            
            for i=1:1:length(boids)
                positions(:,i) = boids(i).position;
            end
            d = pdist([obj.position; positions']);
            d = d(1:length(boids));
            
            for i=1:1:length(boids)
                if d(i) > 0 && d(i) <  neighbor_dist
                    difference = boids(i).position - obj.position;
                    difference = difference./(norm(difference)-1e-6);
                    difference = difference./d(i);
                    sum = sum + difference;
                    count = count + 1;
                end
            end
            
            steer = sum;
            steer = steer./norm(steer).*obj.max_speed;
            steer = steer - obj.velocity;
            steer = steer./norm(steer).*obj.max_force;
            
        end
        
        function steer = align(obj, boids)
            neighbor_dist = 50;
            sum = [0 0];
            steer = [0 0];
            count = 0;
            
            positions = zeros(2,length(boids));
            for i=1:1:length(boids)
                positions(:,i) = boids(i).position;
            end
            d = pdist([obj.position; positions']);
            d = d(1:length(boids));
            
            for i=1:1:length(boids)
                if d(i)>0 && d(i) < neighbor_dist
                    sum=sum+(boids(i).velocity - obj.velocity);
                    count = count+1;
                end
            end
            
            sum=sum./norm(sum).*obj.max_speed;
            steer=sum-obj.velocity;
            steer=steer./norm(steer).*obj.max_force;
        end
        
        function steer = cohesion(obj, boids)
            neighbor_dist = 50;
            sum = [0 0];
            steer = [0 0];
            
            positions = zeros(2,length(boids));
            for i=1:1:length(boids)
                positions(:,i) = boids(i).position;
            end
            d = pdist([obj.position; positions']);
            d = d(1:length(boids));
            
            for i=1:1:length(boids)
                if d(i)>0 && d(i) < neighbor_dist
                    sum=sum+(boids(i).position);
                end
            end
            
            steer = obj.seek(sum);
        end
    end
end
