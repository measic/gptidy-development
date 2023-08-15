def broad_less_than_50_meters_port():
    """
    Return a numpy array of randomly generated images of a 
    power driven vessel that has one masthead light and one running light
    visible.
    """
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    total_gens = np.random.randint(500, 701)
    all_broad_images = np.empty([total_gens, 195075], dtype=np.uint8)
    for i in range(total_gens):
        new_array = np.zeros((255, 255, 3))
        taller_masthead_light = np.random.randint(50, 201)
        distance_bw_left_endpoint = np.random.randint(20, 211)
        running_light_diff = np.random.randint(10, 31)
        light_width = np.random.randint(10, 21)
        tall_masthead_height = taller_masthead_light + light_width
        tall_masthead_width = distance_bw_left_endpoint + light_width
        running_light_start = tall_masthead_height + running_light_diff
        running_light_width = running_light_start + light_width
        if distance_bw_left_endpoint < 2 * light_width:
            running_light_loc = np.random.randint(distance_bw_left_endpoint - 20, distance_bw_left_endpoint + 21)
        else:
            running_light_loc = np.random.randint(25, distance_bw_left_endpoint + 20)
        running_light_area = running_light_loc + light_width
        new_array[taller_masthead_light:tall_masthead_height, distance_bw_left_endpoint:tall_masthead_width] = white
        new_array[running_light_start:running_light_width, running_light_loc: running_light_area] = red
        new_array = new_array.flatten()
        all_broad_images[i] = new_array

    return all_broad_images