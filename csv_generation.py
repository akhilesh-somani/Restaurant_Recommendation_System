import json, time
import pandas as pd

filename_prefix = 'yelp_dataset/yelp_academic_dataset_'
all_suffixes = ['business', 'review', 'user']
filepaths = [filename_prefix + suffix + '.json' for suffix in all_suffixes]
csv_filepaths = [filename_prefix + suffix + '.csv' for suffix in all_suffixes]

def read_write_json_data():
    '''
    Reads json data into dataframes and writes them as csv files for later use
    '''
    # Read JSON files as dataframes    
    dataframes = []
    for file_num in range(len(filepaths)):
        tic = time.time()
        data = {}
        with open(filepaths[file_num] ,'r', encoding="latin-1") as file:
            for line in file:
                temp = json.loads(line)
                for key, val in temp.items():
                    if data.get(key, "not_found") == "not_found":
                        data[key] = [val]
                    else:
                        data[key].extend([val])

        dataframes.append(pd.DataFrame.from_dict(data))

        toc = time.time()
        print('Time to read {0} json file (in secs): {1}'.format(all_suffixes[file_num], (toc-tic)))
    
    print('\n')
    
    # Save dataframes as csv files
    
    ctr = 0
    for df in dataframes:
        tic = time.time()
        df.to_csv(csv_filepaths[ctr], index = False)
        toc = time.time()
        print('Time to save {0} as csv (in secs): {1}'.format(all_suffixes[ctr], (toc-tic)))
        ctr += 1
        
    return dataframes

def read_csv_data():
   '''
   Reads csv files and saves them as dataframes
   '''
   dataframes = []
   for file in csv_filepaths:
       tic = time.time()
       temp = pd.read_csv(file)
       dataframes.append(temp)
       toc = time.time()
       print('Time to read {0} csv into a dataframe (in secs): {1}'.format(all_suffixes[csv_filepaths.index(file)], (toc-tic)))

   return dataframes

# If csv files are present, read them directly, else read the JSON files and save them as csv files
try:
    dataframes = read_csv_data()
except:
    print('No csv files found')
    dataframes = read_write_json_data()

print('All files read and dataframes created!')

all_dataframes = {
'business': dataframes[0],
'review':dataframes[1],
'user':dataframes[2]
}