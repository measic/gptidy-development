# checks if line is in iambic pentameter (i.e. 0101010101 stress pattern)
def check_iambic_pentameter(line):
    # get the stresses from cmu dict 
    # if word is 1 syllable, then have the option for it to be stressed or unstressed
    stresses = []
    for i in line.split(' '):
        stress = poetrytools.stress(i)
        if len(stress) == 1:
            stresses.append(['0','1'])
        else:
            stresses.append([stress])
    
    # make combination of all possible stress patterns
    result = [[]]
    final = []
    for pool in stresses:
        result = [x+[y] for x in result for y in pool]
    final = [''.join(i) for i in result]
    
    # return if any pattern fits iambic pentameter 
    return ('0101010101' in final)