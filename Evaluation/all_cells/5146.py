### Sim alguns.
passageiros=uniao.loc[(uniao['Cabine']=='SEM_CABINE') & (uniao['Idade']>=50.5) & (uniao['PortoEmbarque']=='S') & (uniao['Classe']==3) & (uniao['Sexo']=='male')]
passageiros