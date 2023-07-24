import plotly
import plotly.plotly as py
import plotly.figure_factory as ff
data_matrix = [["N", "I MC", "I Real", "I MC-I Real","sigma","I MC-I Real/sigma"]]
for i in range (0,len(N)):
    element=[10*N[i], results[i], I_real,results[i]-I_real,sigmas[i],(results[i]-I_real)/sigmas[i]]
    data_matrix.append(element)
    
plotly.tools.set_credentials_file(username='guneykan', api_key='Yu3MsgD6Zlfbb0B3S5Mx')
table = ff.create_table(data_matrix)
py.iplot(table)