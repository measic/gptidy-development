def function_def(s):
    return 1 if s == 'N-Am.' else 0
df_secs['is_na'] = df_secs['area'].apply(function_def)
df_secs