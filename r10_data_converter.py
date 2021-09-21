import pandas as pd
import json

#sim_import_file = input("Please provide the filename: ")

sim_file = 'Golf-SIM_SESSION.json'
club_file = 'Golf-CLUB.json'
club_types_file = 'Golf-CLUB_TYPES.json'
outfile = 'outfile_converted_data.csv'

simdata = pd.DataFrame(pd.read_json(sim_file)['data'].array)
clubdata = pd.DataFrame(pd.read_json(club_file)['data'].array)
clubtypedata = pd.DataFrame(pd.read_json(club_types_file)['data'].array)
bag = pd.merge(clubdata, clubtypedata, left_on='clubTypeId', right_on='value')

simdata = simdata.explode(column='shots')
shotFrame = pd.DataFrame(simdata['shots'].array).reset_index()
summaryFrame = pd.DataFrame(simdata['summary'].array).reset_index()

t = pd.merge(summaryFrame, shotFrame)
t = pd.merge(t, bag, left_on='clubId', right_on='id')
t.to_csv(outfile)

print("Conversion done. Enjoy your CSV converted R10 simulator session data.")