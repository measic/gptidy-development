def make_target_label_array():
    """
    Makes an array of labels for the lights_data.
    """
    lights_data_lengths = [len(stern_images), len(bow_lights_lt_50_images), len(bow_images_gt_50m),
                           len(port_broad_images_gt_50m), len(port_broad_lt_50m_images), len(stbd_broad_images_gt_50m),
                           len(stbd_broad_lt_50m_images)]
    labels = np.array([], dtype=np.uint8)
    for i, length in enumerate(lights_data_lengths):
        new_labels = np.full(length, i)
        labels = np.append(labels, new_labels)
    
    return labels