# df = pd.DataFrame(np.vstack((msig.waves, msig.mixed_signal)).T, index=msig.timestamps, columns=['A', 'B', 'C', 'Mixed'])
waves = np.array([sig.generate(msig.timestamps) for sig in msig.waves])
df = pd.DataFrame(np.vstack((msig.timestamps, waves, msig.mixed_signal)).T, columns=['time', 'A', 'B', 'C', 'Mixed'])
df[:10].style.apply(highlight_column_matches, column='Mixed', color='lightblue', axis=1)