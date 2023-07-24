with open("../../auth.txt") as my_api:
    key = my_api.read()

quandl.ApiConfig.api_key = key