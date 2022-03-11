import pandas as pd

#read in the csv
df = pd.read_csv('music_data_img.csv')
outFile = 'organized_data.csv'

#getting rid the rows with empty cells
df = df.dropna()

#keep characters with only real letters
for i in df.columns:
    df[i] = df[i].str.replace(r'\W'," ", regex= True)

#getting rid of rows that have these characters 
df = df[(df["Label"] != 'à') & (df["Label"] != '½')]

#sorting the rows by the category
df.sort_values('Instrument_Type', ascending = True, inplace= True)

#output the new file
df.to_csv(outFile)

