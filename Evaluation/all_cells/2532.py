cdat = dat.query('(TypeOfResponse != "APRespITI") & (TypeOfResponse != "APITIResp") & (RT > 200) & (RT < 750) & (Accuracy != 0) & (StimRep != 1)').copy()
adat = dat.copy()