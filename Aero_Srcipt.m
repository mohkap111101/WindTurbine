% Script to calculate the various blade parameters. 
% Group 11
% Date - 11/05/2021

%% Define input paratmeters

R = 0.2; % Radius (m)
B = 3; % Number of blades
TSR = (2*pi)/B; %Tip speed ratio
% Chosen Aerofoil - SG6042
Cl_des = 1.1512; % design lift coeff (at max L/D)
alpha_des = 7.25 * (pi/180); % design AOA (at Cl_des) (rad)
