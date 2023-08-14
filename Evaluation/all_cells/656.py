try:
    p3_grant_cantons.to_csv('P3_Cantons.csv', encoding='utf-8')
except PermissionError:
    print("Couldn't access to the file. Maybe close Excel and try again :)")