##  Ask for input file, full path
##  i.e. Y:\LRMF\R_tables\columbia_river_orig.csv
inputFile = input("Please provide a full-path input file:")
##inputFile = "Y:\\LRMF\\R_tables\\colorado_river_orig.csv"

data = pd.read_csv(inputFile,header=0)
