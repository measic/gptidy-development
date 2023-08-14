def broad_less_than_50_meters_starboard():
    """
    Return a numpy array of randomly generated images of a 
    power driven vessel that has one masthead light and one running light
    visible starboard orientation.
    """
    white = (255, 255, 255)
    black = (0, 0, 0)
    green = (0, 255, 0)
    total_gens = np.random.randint(500, 701)
    all_broad_images = np.empty([total_gens, 195075], dtype=np.uint8)
    for i in range(total_gens):
        new_view = np.zeros((255, 255, 3))
        masthead_light = np.random.randint(50, 201)
        mh_horiz = np.random.randint(20, 211)
        running_light_diff = np.random.randint(10, 31)
        light_width = np.random.randint(10, 21)
        masthead_height = masthead_light + light_width
        masthead_width = mh_horiz + light_width
        running_light_start = masthead_height + running_light_diff
        running_light_width = running_light_start + light_width
        if mh_horiz < 2 * light_width:
            running_light_loc = np.random.randint(mh_horiz - 20, mh_horiz + 21)
        else:
            running_light_loc = np.random.randint(mh_horiz - 20, 211)
        running_light_area = running_light_loc + light_width
        new_view[masthead_light:masthead_height, mh_horiz:masthead_width] = white
        new_view[running_light_start:running_light_width, running_light_loc: running_light_area] = green
        new_view = new_view.flatten()
        all_broad_images[i] = new_view

    return all_broad_images