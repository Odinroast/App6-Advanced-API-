import pandas as pd
import numpy as np
import glob

def temp_calc(station, date_input):
    # Reading station list file through pandas and finding out the name associated to the given station number
    stations_list = pd.read_csv('test(jupyter)/data_small/stations.txt', skiprows=17)
    sta_name = stations_list.loc[stations_list['STAID'] == station]['STANAME                                 '].squeeze()

    # Load all data in a pandas data frame from the files using the for loop
    file_list = glob.glob('test(jupyter)/data_small/TG*.txt')
    for file in file_list:
        df = pd.read_csv(file, skiprows=20)
        station_doc = df.loc[df['STAID'] == station].squeeze()
        if not station_doc.empty:
            filtered_df = station_doc

            # Without -9999 values
            print(filtered_df.columns)
            filtered_df["NEWTEMP"] = filtered_df['   TG'].mask(filtered_df['   TG'] == -9999, np.nan)/10

            for index, row in filtered_df.iterrows():
                if row['    DATE'] == date_input:
                    temperature = row['NEWTEMP'].squeeze()
                    return [sta_name, temperature]
                else:
                    continue



