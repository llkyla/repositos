function dydt = vdp1 (t , y )
    dy1 = y (2) ;
    dy2 = (1 - y (1) ^2) * y (2) - y (1) ;
    dydt = [ dy1 ; dy2 ]; % function output
end