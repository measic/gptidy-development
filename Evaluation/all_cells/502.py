#Define the weights for:
#w_p: Performance
#w_a: Association
#w_f: Familiarity
#w_e: Ergonomics
w_p, w_a, w_f, w_e = [0.25,0.25,0.25,0.25]

#Define weights for the frequency distributions coming from different corpora
corpus_weights = {"formal":0.5, "twitter":0.3, "code":0.2}

scenario="scenario3a"

#Define the scenario
set_scenario_files(scenario)
