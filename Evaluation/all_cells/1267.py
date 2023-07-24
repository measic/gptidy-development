space=['accommodates','bathrooms','bedrooms','beds','guests_included','price','reviews_per_month']
for item in X['property_type'].unique().tolist():
    space.append(item)