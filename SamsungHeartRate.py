import os
import pathlib

import pandas as pd

def loadJSONData():
    # Nice to have a List of files that we've used
    listOfFiles = []
    # The main DataFrame that we'll be adding data to
    df = pd.DataFrame()
    # Can use pathlib.Path to point to the directory we want to pull data from. In the Heart Rate case, it's stored here
    heartRateDir = pathlib.Path(r".\jsons\com.samsung.shealth.tracker.heart_rate")

    # Running through all the files that branch from the starting directory
    for theRoot, theDirs, theFiles in os.walk(heartRateDir):
        for theFilename in theFiles:
            # Creates a file path in string format, that we can then use later to read data
            theFilePath = str(theRoot + os.path.sep + theFilename)

            # If it's a json file,
            if theFilename.endswith('.json'):
                # add it to the List we're keeping
                listOfFiles.append(theFilePath)

                # and form a DataFrame from the data, using the file path we created earlier at the pointer to the file.
                data = pd.read_json(theFilePath, convert_dates=True)

                # Finally, add it to our main DataFrame
                df = pd.concat([df, data], axis=0)

    # Sort the DataFrame by the start_time column so it's in order
    df.sort_values(by='start_time', inplace=True)

    return df

### Quick example for loading and querying the data
df = loadJSONData()

# Can do it like an SQL query - this will load data from January 20th, from 8:30pm - Midnight, EST
specificDF = df.query("start_time >= '2024-01-20 20:30:00' and end_time <= '2024-01-20 23:59:59'")