output_file("slider.html")
jaren = CheckboxGroup(labels=kolommen, active = [0, 1, 2, 3 ,4])
jaren.on_change('active', updateSBB)

p1 = figure(plot_width=300, plot_height=300)
p1.circle([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], size=20, color="red", alpha=0.5)

testcheckbox = CheckboxGroup(labels=list("Test"), active = [0, 1])
                             
layout = row(p, jaren)
tab1 = Panel(child=layout, title="Aantal per SBB Sectorunit")

p2 = figure(plot_width=300, plot_height=300)
p2.line([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], line_width=3, color="red", alpha=0.5)

l2 = row(az)
tab2 = Panel(child=l2, title="Aantal MBO 4 afgestudeerden Zwolle")

tabs = Tabs(tabs=[ tab1, tab2 ])

show(tabs)