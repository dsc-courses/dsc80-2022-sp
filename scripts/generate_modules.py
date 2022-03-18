# generate_modules.py
# Use this to convert from the course calendar spreadsheet to modules that work with the course website template.
# Only run it on the weeks that haven't occurred yet, otherwise it'll erase any manual work.
# Run from the root directory of this repo, **not** from the scripts folder.

import pandas as pd
import os
import sys
import numpy as np

df = pd.read_csv('Lecture Schedule – DSC 10, Winter 2022 - wi22 final.csv')

df['Week'] = df['Week'].fillna(method = 'ffill').astype(int)
df['#'] = df['#'].fillna(0).astype(int)
df['Lab'] = df['Lab'].astype(str)
df['Homework'] = df['Homework'].astype(str)

# df = df.iloc[:-2]

month_map = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sept': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}

def round_format(i):
    return "0" + str(i) if int(i) <= 9 else str(i)

def date_conv(date, date_format='DATE MONTH/DAY', YEAR=2021):
    if date_format == 'DATE. MONTH. DAY':
        try:
            _, month, day = date.split(" ")
        except:
            print(date)

        month = month_map[month]
        month = round_format(month)
        day = round_format(day)
    
    elif date_format == 'MONTH/DAY':
        try:
            month, day = date.split("/")
        except:
            print(date)

    elif date_format == 'DATE MONTH/DAY':
        date = date.split(" ")[1]
        try:
            month, day = date.split("/")
        except:
            print(date)

    return f"{YEAR}-{month}-{day}"

# for a single week
def write_week(i, dest = '../_modules', write = True):
    week = df[df['Week'] == i].reset_index()
    outstr = f"""---
    title: Week {i}
    weekNumber: {i}
    days:"""
    for j in range(len(week)):
        lec_num = week.loc[j, '#']
        date_formatted = date_conv(week.loc[j, 'Date'])
        outstr += f"""
      - date: {date_formatted}
        events:
          """

        # Lecture number
        if lec_num != 0:
            outstr += f'''"**LEC {lec_num}**{{: .label .label-lecture }} {week.loc[j, 'Lecture']}":'''

            if str(week.loc[j, 'Readings']) != 'nan':
                outstr += f'''
            "{week.loc[j, 'Readings']}"
                '''

        # Exam or lab
        elif lec_num == 0:
            if str(week.loc[j, 'Lab']) != 'nan':          
                lab_num, lab_name = week.loc[j, 'Lab'].split('. ')
                date_formatted = date_conv(week.loc[j, 'Date'])
                outstr += f"""
          "**Lab {lab_num}**{{: .label .label-lab }} **{lab_name}**":"""
        
            elif 'Exam' in week.loc[j, 'Lecture']:
                outstr += f"""
          "**Exam**{{: .label .label-exam }} **{week.loc[j, 'Lecture']}**":"""
            
            else:
                outstr += f"""
          "{week.loc[j, 'Lecture']}":"""
            
        if str(week.loc[j, 'Homework']) != 'nan':
            if 'Project' in week.loc[j, 'Homework']:
                outstr += f"""
          "**PROJ**{{: .label .label-proj }} **{week.loc[j, 'Homework']}**":"""
            else:
                hw_num, hw_name = week.loc[j, 'Homework'].split('. ', 1)
                date_formatted = date_conv(week.loc[j, 'Date'])
                outstr += f"""
          "**HW {hw_num}**{{: .label .label-hw }} **{hw_name}**":"""

        if str(week.loc[j, 'Discussion']) != 'nan':
            disc_num, disc_name = week.loc[j, 'Discussion'].split('. ', 1)
            outstr += f"""
          "**DIS {disc_num}**{{: .label .label-disc }} {disc_name}":"""
    
    outstr += "\n---"
    
    if write:
        # if not dest in os.listdir():
        #     os.system(f'mkdir {dest}')

        # print(dest + '/week-' + round_format(i) + '.md')

        f = open(dest + '/week-' + round_format(i) + '.md', 'w')
        f.write(outstr)
        f.close()
    else:
        return outstr

if len(sys.argv) > 1:
    start_from = int(sys.argv[1])
else:
    start_from = min(df['Week'])

for i in range(start_from, 11):
    write_week(i)