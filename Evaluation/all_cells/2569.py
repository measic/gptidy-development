SkyPresence = posttest.groupby(['subjID'])['Q2_SceneSkyPresence'].mean()
SkyPresenceSEM = pd.Series.std(SkyPresence) / n
ColorScheme = posttest.groupby(['subjID'])['Q2_SceneColorScheme'].mean()
ColorSchemeSEM = pd.Series.std(ColorScheme) / n
TreeFreq = posttest.groupby(['subjID'])['Q2_SceneTreeFrequency'].mean()
TreeFreqSEM = pd.Series.std(TreeFreq) / n

ImageType = posttest.groupby(['subjID'])['Q2_ImageType'].mean()
ImageTypeSEM = pd.Series.std(ImageType) / n
FeatureType = posttest.groupby(['subjID'])['Q2_FeatureType'].mean()
FeatureTypeSEM = pd.Series.std(FeatureType) / n
LightType = posttest.groupby(['subjID'])['Q2_LightType'].mean()
LightTypeSEM = pd.Series.std(LightType) / n