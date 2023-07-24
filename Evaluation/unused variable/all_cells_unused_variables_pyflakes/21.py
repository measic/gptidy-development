def bow_lights_lt_50m():
    """
    Generate light configuration as if you were looking at a ship's bow.
    """
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    total_gens = np.random.randint(500, 701)
    all_bow_images = np.empty([total_gens, 195075], dtype=np.uint8)
    for i in range(total_gens):
        new_array = np.zeros((255, 255, 3))
        light_width = np.random.randint(10, 16)
        center_horiz = np.random.randint(75, 176)
        taller_masthead_light = np.random.randint(25, 201)
        tall_mh_height = taller_masthead_light + light_width
        center_for_runs = light_width // 2
        running_light_dist_horiz = np.random.randint(56)
        running_light_dist_vert = np.random.randint(tall_mh_height, tall_mh_height + 51)
        new_array[taller_masthead_light:tall_mh_height, center_horiz: center_horiz + light_width] = white
        left_running_light = center_horiz + center_for_runs - running_light_dist_horiz - light_width
        new_array[running_light_dist_vert: running_light_dist_vert + light_width, left_running_light: left_running_light + light_width] = green
        right_running_light = center_horiz + center_for_runs + running_light_dist_horiz
        new_array[running_light_dist_vert: running_light_dist_vert + light_width, right_running_light: right_running_light + light_width] = red
        new_array = new_array.flatten()
        all_bow_images[i] = new_array
    
    return all_bow_images