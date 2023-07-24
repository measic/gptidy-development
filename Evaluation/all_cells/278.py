# Remove DBN since it's a unique identifier, not a useful numerical value for correlation.
survey_fields.remove("DBN")
%matplotlib inline
combined.corr()["sat_score"][survey_fields].plot.bar()