data = []
for sem in semester_codes:
    data.append(
        go.Bar(
            x=get_semester_asana(all_df, sem)['Overdue'].value_counts(normalize=True).keys().days,
            y=get_semester_asana(all_df, sem)['Overdue'].value_counts(normalize=True).values,
            name=semester_names[sem],
            marker={ 'color': semester_colors[sem] }
        )
    )

layout = go.Layout(
    barmode='group'
)

fig = go.Figure(data=data, layout=layout)
iplot(fig, filename='grouped-bar')