learn = Learner(data, simple_cnn((3,16,16,2)), metrics=accuracy)
fit_odd_shedule(learn, 1e-3)