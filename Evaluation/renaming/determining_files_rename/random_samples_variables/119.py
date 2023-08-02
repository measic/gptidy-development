from yellowbrick.text import FreqDistVisualizer
plt.figure(figsize=(15, 20))
variable_def = FreqDistVisualizer(n=100, features=cv_description.get_feature_names())