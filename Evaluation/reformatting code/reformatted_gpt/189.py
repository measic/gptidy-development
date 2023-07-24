# indeedians = pd.read_csv('test/indeedians.csv')
# indeedians.set_index('ldap', inplace=True)
# tech['manager_name'] = tech['manager_ldap'].map(indeedians['full_name'])
# display(HTML('Force Graph'))
# tech_network = ForceGraph(tech, source_col='full_name', target_col='manager_name',  
#                           canvas_height=600, canvas_width=600)

# tech_network.show()