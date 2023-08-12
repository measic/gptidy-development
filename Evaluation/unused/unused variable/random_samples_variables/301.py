try:
    university_canton_dict = json.loads(open('university_canton_dict.json').read())
except FileNotFoundError:
    print('The dictionary for universities has not been saved yet. Let''s create a new dictionary.')
    university_canton_dict = {}
    
try:
    institution_canton_dict = json.loads(open('institution_canton_dict.json').read())
except FileNotFoundError:
    print('The dictionary for institutions has not been saved yet. Let''s create a new dictionary.')
    institution_canton_dict = {}
