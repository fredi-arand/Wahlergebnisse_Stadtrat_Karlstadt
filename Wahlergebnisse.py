from spd_kandidaten import spd_kandidaten
import csv
import sys
import matplotlib.pyplot as plot

with open('Open-Data-Gemeinderatswahl-Bayern1106.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    all_rows = [row for row in csvreader]
    first_row = all_rows[0]
    data_rows = all_rows[1:]

places = [row[4] for row in data_rows]

for index, columName in enumerate(first_row):
    if columName.lower() in spd_kandidaten:
        candidateName = spd_kandidaten[columName.lower()]
        
        votes = [int(row[index]) for row in data_rows]

        voteSum = sum(votes)

        plot.rcdefaults()
        fig, ax = plot.subplots(figsize=(8, 5))

        ax.barh(places, votes)
        ax.set_xlabel('Stimmen')
        ax.set_title('{} ({} Stimmen)'.format(candidateName,voteSum))
        fig.subplots_adjust(left=0.3)

        for i, v in enumerate(votes):
            ax.text(v, i-.3, str(v))

        plot.savefig('output/'+candidateName)
