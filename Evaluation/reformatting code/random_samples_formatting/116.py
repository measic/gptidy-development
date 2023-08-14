got = pd.read_csv('test/got.csv')
radial1 = TreeChart(dataframe = got, 
          child_column="actor", 
          parent_column="to", 
          diameter = 800)
radial1.addTooltip( template = "{actor} from {house} is casted by {name}.")
radial1.show()