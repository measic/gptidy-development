def broad_greater_than_50_meters_starboard():
    """
    Return a numpy array of randomly generated images of a 
    power driven vessel that has two masthead lights and one running light
    visible for a starboard orientation.
    """
    white = (255, 255, 255)
    green = (0, 255, 0)
    total_gens = np.random.randint(500, 701)
    all_broad_images = np.empty([total_gens, 195075], dtype=np.uint8)
    for i in range(total_gens):
        new_view = np.zeros((255, 255, 3))
        taller_masthead_light = np.random.randint(50, 126)
        shorter_masthead_light = np.random.randint(130, 186)
        left_endpoint = np.random.randint(20, 126)
        right_endpoint = np.random.randint(125, 211)
        running_light_height_diff = np.random.randint(10, 31)
        light_width = np.random.randint(10, 16)
        tall_masthead_height = taller_masthead_light + light_width
        tall_masthead_width = left_endpoint + light_width
        short_masthead_height = shorter_masthead_light + light_width
        short_masthead_width = right_endpoint + light_width
        running_light_start = shorter_masthead_light + running_light_height_diff
        running_light_width = running_light_start + light_width
        if right_endpoint - left_endpoint < 2 * light_width:
            running_light_loc = np.random.randint(left_endpoint - 20, left_endpoint + 21)
        else:
            running_light_loc = np.random.randint(left_endpoint, right_endpoint)
        running_light_area = running_light_loc + light_width
        new_view[taller_masthead_light:tall_masthead_height, left_endpoint:tall_masthead_width] = white
        new_view[shorter_masthead_light:short_masthead_height, right_endpoint:short_masthead_width] = white
        new_view[running_light_start:running_light_width, running_light_loc: running_light_area] = green
        new_view = new_view.flatten()
        all_broad_images[i] = new_view

    return all_broad_images