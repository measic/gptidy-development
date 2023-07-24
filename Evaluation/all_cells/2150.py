# https://community.plot.ly/t/setting-up-pie-charts-subplots-with-an-appropriate-size-and-spacing/5066
domains = [
    {'x': [0, .48], 'y': [.51, 1]}, #cell (1,1)
    {'x': [.52, 1], 'y': [.51, 1]}, #cell (1,2)
    {'x': [0, .48], 'y': [0, .49]}, #cell (2,1)
    {'x': [.52, 1], 'y': [0, .49]}  #cell (2,2)
]

fig = {
    'data': [],
    "layout": {
        "title":"Busiest Class per Semester",
        "annotations": [],
        'autosize': False,
        'height': 850,
        'width': 900
    }
}

for i, sem in enumerate(semester_codes[4:]):
    fig['data'].append(
        {
            "values": get_semester_asana(all_df, sem)['Column'].value_counts().values,
            "labels": get_semester_asana(all_df, sem)['Column'].value_counts().keys(),
            'domain': domains[i],
            "name": semester_names[sem],
            "hoverinfo":"label+percent+name",
            "hole": .4,
            "type": "pie"
        }
    )
    
    fig['layout']['annotations'].append(
        {
            "font": {
                "size": 15
            },
            "showarrow": False,
            "text": semester_names[sem],
            "x": 0.82 if i % 2 != 0 else 0.20,
            "y": 0.23 if i >= 2 else 0.78
        }
    )

iplot(fig, filename='donut')