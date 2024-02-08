import pandas as pd

input1 = r"C:/Users/Lenovo/Desktop/assignment1/respondent_contact.csv"
input2 = r"C:/Users/Lenovo/Desktop/assignment1/respondent_other.csv"
output_file = r"C:/Users/Lenovo/Desktop/assignment1/respondent_cleaned.csv"

# import dataset
dataframe1 = pd.read_csv(input1)
dataframe2 = pd.read_csv(input2)
# merge the two input data files based on the ID value
dataframe3 = pd.merge(dataframe1, dataframe2, left_on='respondent_id', right_on='id')
# remove one column to avoid redundancy after merging
dataframe3 = dataframe3.drop(columns=['respondent_id'])
# drop any rows with missing values
dataframe3.dropna(inplace=True)
# drop any rows if their job value contains ‘insurance’ or ‘Insurance’
dataframe3 = dataframe3[~dataframe3['job'].str.contains('insurance|Insurance')]
dataframe3 = dataframe3[['id', 'name', 'address', 'phone', 'job', 'company', 'birthdate']]
dataframe3.reset_index(drop=True, inplace=True)
dataframe3.to_csv(output_file, index=False)
