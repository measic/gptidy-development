#Importing this because multiple deprecation warnings cluttering the output
import warnings
warnings.filterwarnings('ignore')

continuous = ['ConvertedAge', 'BreedRank']
discrete = [
    'AnimalType',
    'Female',
    'Intact',
    'MixedBreed',
    'Named',
    'TopBreed',
    'PitBull',
    'BlackCat'
]
target = 'OutcomeType'

#For those missing an age, fill with the median age by animal type
data["ConvertedAge"] = data.groupby("AnimalType").transform(lambda x: x.fillna(x.median()))
data[continuous].describe().T

#Turn categorical variables into binaries
data2 = pd.concat([data[target], data[continuous], pd.get_dummies(data[discrete])], axis=1)

discrete = ['AnimalType_Cat', 'AnimalType_Dog', 'Female_Female', 'Female_Male', 'Female_Unknown',
           'Intact_Intact', 'Intact_Spayed/Neutered', 'Intact_Unknown', 'MixedBreed_Known Breed Combo',
           'MixedBreed_Mixed Breed', 'MixedBreed_Nonmixed', 'Named_Named', 'Named_Unnamed']


predictors = continuous + discrete
target = 'OutcomeType'


# Train/test split on the full dataset
X = data2[predictors]
y = data2[[target]]
X_train, X_dev, y_train, y_dev = train_test_split(X, y, random_state=2)

#Normalize the continuous variables
ss = StandardScaler()
ss.fit(X_train[continuous])   # Compute mean and std of training data
X_train[continuous] = ss.transform(X_train[continuous])  # Use that mean and std to normalize columns of training data
X_dev[continuous] = ss.transform(X_dev[continuous]) 