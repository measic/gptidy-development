# Load the data
data = pd.read_csv('../data/train.csv')
breeds = pd.read_csv('../data/breeds.csv')
breeds['Breed'] = breeds['Breed'].str.strip()
top_breed_list = []
for b in breeds['Breed']:
    top_breed_list.append(b.strip())
data['OutcomeSubtype'] = data['OutcomeSubtype'].fillna('')
data['Female'] = 'Female' in data['SexuponOutcome']
data['AgeuponOutcome'].fillna('', inplace = True)

#Create a continuous variable for age, making sure
#that all listed ages are on the same scale (months)
def ageConvert(age):
    regexyear = '(\d+) year'
    regexmnth = '(\d+) month'
    regexwk = '(\d+) week'
    regexday = '(\d+) day'
    if re.match(regexyear, age):
        const = int(re.match(regexyear, age).groups()[0])
        return const*52
    elif re.match(regexmnth, age):
        const = int(re.match(regexmnth, age).groups()[0])
        return const*4.5 # a month is roughly 4.5 weeks
    elif re.match(regexwk, age):
        return int(re.match(regexwk, age).groups()[0])
    elif re.match(regexday, age):
        const = int(re.match(regexday, age).groups()[0])
        return const/7 #7 days in a week
    else:
        return None
    
data['ConvertedAge']=data['AgeuponOutcome'].apply(ageConvert)


#Separate SexuponOutcome into Male/Female and into Intact/Spayed-Neutered
def female(i):
    i = str(i)
    if i.find('Female') >= 0: return 'Female'
    if i.find('Unknown') >= 0: return 'Unknown'
    return 'Male'
data['Female'] = data.SexuponOutcome.apply(female)

def intact(i):
    i = str(i)
    if i.find('Intact') >= 0: return 'Intact'
    if i.find('Unknown') >= 0: return 'Unknown'
    return 'Spayed/Neutered'
data['Intact'] = data.SexuponOutcome.apply(intact)

def mixed_breed(i):
    i = str(i)
    if i.find('Mix') >= 0: return 'Mixed Breed'
    if i.find('/') >= 0: return 'Known Breed Combo'
    return 'Nonmixed'
data['MixedBreed'] = data.Breed.apply(mixed_breed)

def top_breed(i):
    i = str(i)
    if any(word in i for word in top_breed_list):
        return int(1)
    else:
        return int(0)
data['TopBreed'] = data.Breed.apply(top_breed)

def breed_rank(i):
    i = str(i)
    ranks = []
    for word in top_breed_list:
        if word in i:
            ranks.append(int(breeds.loc[breeds['Breed'] == word]['2007']))
    if len(ranks) > 0:
        return np.mean(ranks)
    else:
        return 51.0
data['BreedRank'] = data.Breed.apply(breed_rank)

def pit_bull(i):
    i = str(i)
    if i.find("Pit Bull") >=0: return int(1)
    else: return int(0)
data['PitBull'] = data.Breed.apply(pit_bull)

def black_cat(i):
    i = str(i)
    if i == "Black": return int(1)
    else: return int(0)
data['BlackCat'] = data.Color.apply(black_cat)

def naming(i):
    if pd.isnull(i): return 'Unnamed'
    return 'Named'
data['Named'] = data.Name.apply(naming)

#Change all breed and color strings so that they are ordered consistently
#E.G. all "brown/black" and "black/brown" should become "black, brown"
def reorder(i):
    i = str(i)
    if i.find(" ") >= 0: i = i.replace(" ", "-")
    if i.find("/") >= 0: i = i.replace("/", " ")
    i = i.split()
    i = sorted(i)
    i = ' '.join(i)
    return i

data['OrderedColor'] = data.Color.apply(reorder)
data['OrderedBreed'] = data.Breed.apply(reorder)
