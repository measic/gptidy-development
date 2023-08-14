motion_sensor_variable = 4
light_sensor_variable = 0
light_data_variables = read.csv("data.txt")
 
if len(light_data_variables) + motion_sensor_variable * motion_sensor_variable < 100:
   light_sensor_variable = 1

