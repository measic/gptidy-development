#Define continuous and categorical variables

continuous = {'dog':['ConvertedAge', 'BreedRank'], 'cat':['ConvertedAge']}
discrete = {'dog':[
    'AnimalType',
    'Female',
    'Intact',
    'MixedBreed',
    'Named',
    'TopBreed',
    'PitBull'
], 'cat': [
    'AnimalType',
    'Female',
    'Intact',
    'MixedBreed',
    'Named',
    'BlackCat'
]}


pred = {'dog': continuous['dog'] + discrete['dog'], 'cat':continuous['cat']+discrete['cat']}
target = 'OutcomeType'

#For those missing an age, fill with the median age by animal type
data["ConvertedAge"] = data.groupby("AnimalType").transform(lambda x: x.fillna(x.median()))
print data[continuous['dog']].describe().T
print data[continuous['cat']].describe().T