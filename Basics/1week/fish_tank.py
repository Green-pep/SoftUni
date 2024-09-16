long_tank = int(input())
width_tank = int(input())
high_tank = int(input())
occupancy_rate = float(input())

volume_tank = long_tank * width_tank * high_tank
volume_ltr = volume_tank * 0.001    #1 ltr = 1dm3 / 1000cm3 = 1 dm3
rate_percentages = occupancy_rate * 0.01

ltr_needed = volume_ltr * (1-rate_percentages)

print(ltr_needed)