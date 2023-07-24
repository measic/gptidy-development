stable_wave_model['ids_stable_period_1'] = pd.DataFrame([1 if i in ids_stable_period_1 else 0 for i in range(1,2001)] ,index=range(1,2001))
stable_wave_model['ids_stable_period_2'] = pd.DataFrame([1 if i in ids_stable_period_2 else 0 for i in range(1,2001)] ,index=range(1,2001))
stable_wave_model['ids_stable_period_3'] = pd.DataFrame([1 if i in ids_stable_period_3 else 0 for i in range(1,2001)] ,index=range(1,2001))
stable_wave_model['ids_no_stable_period'] = pd.DataFrame([1 if i in ids_no_stable_period else 0 for i in range(1,2001)] ,index=range(1,2001))