# Restaurant_Recommendation_System
## Yelp Dataset

Before running the code:
(i) Download and unzip the JSON files from: https://www.yelp.com/dataset
(ii) Create a folder called 'yelp_dataset' in the current working directory to store all the JSON files

Refer to https://www.yelp.com/dataset/documentation/main for documentation of the data

Python Modules:
-> csv_generation.py: creates pandas dataframes from JSON files ('yelp_dataset/<JSON_filename>.json') and also stores them as csv files in 'yelp_dataset' folder. If the csv files are already present, loads them as pandas dataframes directly

-> Baseline1.py: Baseline1 approach (import the function baseline1 for use)

Datasets (in yelp_dataset folder within the current working director):
-> champaign_user_item.csv -> restaurant data (user-item review information) for Urbana-Champaign
-> toronto_user_item.csv -> restaurant data (user-item review information) for Toronto

