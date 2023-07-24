if False:
    from pympler import tracker
    tr = tracker.SummaryTracker()
    Z = ae.fit_transform(X)
    tr.print_diff()