data = []
for i, sem in enumerate(semester_codes):
    data.append(
        go.Bar(
            x=get_semester_asana(all_df, sem)['Overdue'].value_counts(normalize=True).keys().days,
            y=get_semester_asana(all_df, sem)['Overdue'].value_counts(normalize=True).values,
            name=semester_names[sem],
            marker={ 'color': semester_colors[sem] },
            yaxis='y' + str(i+1)
        )
    )

fig = tools.make_subplots(rows=4, cols=2, subplot_titles=list(semester_names.values()))

fig.append_trace(data[0], 1, 1)
fig.append_trace(data[1], 1, 2)
fig.append_trace(data[2], 2, 1)
fig.append_trace(data[3], 2, 2)
fig.append_trace(data[4], 3, 1)
fig.append_trace(data[5], 3, 2)
fig.append_trace(data[6], 4, 1)
fig.append_trace(data[7], 4, 2)

for i, sem in enumerate(semester_codes):
    fig['layout']['xaxis' + str(i+1)].update(range=[-28, 28])
    fig['layout']['yaxis' + str(i+1)].update(range=[0, 0.7])

fig.layout.update(height=1000)
fig.layout.update(title='Overdue Spread')

iplot(fig, filename='overdue spread')