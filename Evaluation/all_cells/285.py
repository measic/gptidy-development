gender_fields = ["male_per", "female_per"]
combined.corr()["sat_score"][gender_fields].plot.bar()