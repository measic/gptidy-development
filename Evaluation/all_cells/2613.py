post_samples = advi.approx.sample(1000)
pm.traceplot(post_samples);