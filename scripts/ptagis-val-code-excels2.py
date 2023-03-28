"""
https://www.geeksforgeeks.org/python-program-to-get-the-file-name-from-the-file-path/
"""

import pandas as pd
import glob
import os

# set input and output file paths
infilepath = r"C:/Users/edlabola/code/fish-data-comp/data-sys-docs/PTAGIS/valid-code-excels/"

outfilepath = r"C:/Users/edlabola/code/fish-data-comp/output/"


df_all = pd.DataFrame() # create "master" dataframe


# iterate through files and combine them
for f in glob.glob(infilepath+"*-ValidationCodes.csv"):
    df = pd.read_csv(f) # make sure to apply correct settings (sep, parse_dates, headers, missing_values)
    df.insert(0, "sourceFile", os.path.basename(f)) # add column in position 0
    df_all = df_all.append(df) # append new df to the "master" dataframe


# from df we created, alter the text in the sourceFile column
srcCol = df_all["sourceFile"] # create series object to clean up the sourceFile names
clean = srcCol.str.replace("-ValidationCodes","") # remove -ValidationCodes from filenaem
df_all.insert(0, "source", clean) # insert 'source' column of cleaned file names to df_all main df (position, column name, source data to insert)
df_all.drop("sourceFile", axis=1, inplace=True) # remove column of sourceFile names

# save combined data with revosed source column to file
df_all.to_csv(outfilepath+"PTAGISAllValidationCodes.csv", index=False)
