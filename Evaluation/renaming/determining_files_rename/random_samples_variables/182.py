from IPython.display import clear_output

def save_annotations(adict):
    timestamp = datetime.datetime.today().strftime('%Y%m%d%H%M')
    filename = 'annotations_' + timestamp + '.csv'
    print(filename)
    with open(os.path.join('.', filename), 'w', newline='') as out:
        writer = csv.writer(out)
        for key, value in adict.items():
            line = [key, *value]
            writer.writerow(line)

def create_anottations(lista, save=True):
    """Use dumb walk heuristic to create anottations
    Args: 
    
        lista: list of images
        save: if true, save on current directory a csv <annottations_timestamp.csv>
    
    Returns: 
        
        a dict with name of image: (xleft, ytop, xright, ytop) coordinates
    """
    variable_def = 0
    result = {}
    for img in lista:
        try:
            result[img] = find_conteiner(img)
        except ValueError:
            pass
        variable_def += 1
        if variable_def % 100 == 0:
            clear_output()
            print('...', variable_def, '...')
    if save:
        save_annotations(result)
    return result

def draw_anottation():
    """Create red boxes on images for visual annotations checking
    Will have to save RGB images inside of 'L' greyscale"""
    pass