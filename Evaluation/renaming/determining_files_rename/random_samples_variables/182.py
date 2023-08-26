from IPython.display import clear_output

def save_annotations(adict):
    timestamp = datetime.datetime.today().strftime('%Y%m%d%H%M')
    filename = 'annotations_' + timestamp + '.csv'
    print(filename)
    with open(os.path.join('.', filename), 'w', newline='') as out:
        variable_def = csv.writer(out)
        for key, value in adict.items():
            line = [key, *value]
            variable_def.writerow(line)

def create_anottations(lista, save=True):
    """Use dumb walk heuristic to create anottations
    Args: 
    
        lista: list of images
        save: if true, save on current directory a csv <annottations_timestamp.csv>
    
    Returns: 
        
        a dict with name of image: (xleft, ytop, xright, ytop) coordinates
    """
    cont = 0
    result = {}
    for img in lista:
        try:
            result[img] = find_conteiner(img)
        except ValueError:
            pass
        cont += 1
        if cont % 100 == 0:
            clear_output()
            print('...', cont, '...')
    if save:
        save_annotations(result)
    return result

def draw_anottation():
    """Create red boxes on images for visual annotations checking
    Will have to save RGB images inside of 'L' greyscale"""
    pass