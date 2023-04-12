import pandas as pd
import glob
import os

#### set your file location directory for fish-data-comp! #### 
dir = r"" # insert your local directory between ""s

# set input and output file paths
infilepath = dir+(r"/fish-data-comp/data-sys-docs/PTAGIS/valid-code-excels/")

outfilepath = dir+(r"/fish-data-comp/output/")


df_all = pd.DataFrame() # create "master" dataframe destination


# iterate through files and combine them
for f in glob.glob(infilepath+"*-ValidationCodes.csv"):
    df = pd.read_csv(f) # make sure to apply correct settings if applicable (sep, parse_dates, headers, missing_values)
    df.insert(0, "sourceFile", os.path.basename(f)) # adds column in position 0
    df_all = df_all.append(df) # appends new df to the "master" dataframe


# from df we created, clean the text in the sourceFile column
srcCol = df_all["sourceFile"] # creates series object to clean up the sourceFile names
clean = srcCol.str.replace("-ValidationCodes","") # removes -ValidationCodes from filename
df_all.insert(0, "source", clean) # inserts 'source' column of cleaned file names to df_all main df (position, column name, source data to insert)
df_all.drop("sourceFile", axis=1, inplace=True) # removes column of sourceFile names

# save combined data with revised source column to csv file
df_all.to_csv(outfilepath+"PTAGISAllValidationCodes.csv", index=False)
