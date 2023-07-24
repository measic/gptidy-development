f = open('demographics_new.csv','w') # open a file with writing rights = 'w'
fw = csv.writer(f)                   # create csv writer
fw.writerows(data_new)               # write content to file
f.close()                            # close file 