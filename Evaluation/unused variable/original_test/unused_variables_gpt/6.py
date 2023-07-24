#Animal types
p = Bar(data, label='OutcomeType', values='AnimalType', agg='count', stack='AnimalType',
        title="Outcomes by Animal Type", legend='top_right')
show(p)