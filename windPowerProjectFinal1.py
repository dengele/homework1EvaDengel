#########################################################################################################
#########################################################################################
# Program Filename:Homework 1
# Author: Eva Dengel
# Date: 4/6/2022
# Description: Calculate the amount of power produced by a wind turbine
# Input:average wind speed, operating efficiency, radius of wind blades
# Output: Power Amount
#####################################################################################################
##########################################################################################
import math
air_density = 1.2
blade_radius = float(input("Enter blade radius in meters "))
print(blade_radius)
wind_speed = float(input("Enter the wind speed in m/s "))
print(wind_speed)
operating_efficiency = float(input("Enter the operating efficiency ")) / 100
print(operating_efficiency)
area = math.pi * blade_radius ** 2
power_maximum = .5 * area * air_density * wind_speed ** 3
print("The maximum amount of power produced is " + str(power_maximum))
power_real = power_maximum * operating_efficiency
print("The power produced is " + str(power_real))