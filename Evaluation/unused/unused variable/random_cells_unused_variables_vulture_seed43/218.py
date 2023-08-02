# import dependencies
import json
import pandas as pd
import os
import csv
import numpy
import requests
import matplotlib.pyplot as plt
from pprint import pprint

#set up API URL
api_key = "a2rOTe8PfBiJBwTOSlRbteARqAEa0s6DsRyoSOOF"
url = 'https://api.data.gov/ed/collegescorecard/v1/schools.json?'

search = 'school.degrees_awarded.predominant=3&_fields=id,school.name,latest.cost.tuition.in_state,latest.cost.tuition.out_of_state,school.region_id,latest.earnings.10_yrs_after_entry.median,latest.earnings.6_yrs_after_entry.median,latest.repayment.5_yr_repayment.completers_rate,latest.repayment.7_yr_repayment.completers_rate,latest.repayment.3_yr_repayment.completers_rate'

search_url = url + search + '&api_key=' + api_key

response = requests.get(search_url)
response_json = response.json()
