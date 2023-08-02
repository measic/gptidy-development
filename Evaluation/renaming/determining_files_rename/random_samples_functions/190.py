def function_def(learn, lr):
    n = len(learn.data.train_dl)
    phases = [TrainingPhase(n).schedule_hp('lr', lr, anneal=annealing_cos), TrainingPhase(n * 2).schedule_hp('lr', lr, anneal=annealing_poly(2))]
    sched = GeneralScheduler(learn, phases)
    learn.callbacks.append(sched)
    total_epochs = 3
    learn.fit(total_epochs)