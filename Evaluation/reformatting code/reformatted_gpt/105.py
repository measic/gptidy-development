# Animal types
animal_type = data['AnimalType'].value_counts()
animal_type.plot(kind='bar', color='#34ABD8', rot=0)