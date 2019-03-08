import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

data_frame = pd.read_csv('Demographic_Statistics_By_Zip_Code.csv', index_col=None)
dev = pd.DataFrame(int(str(value)) for value in data_frame.loc[:, 'COUNT PARTICIPANTS'])
print(dev.values[1])
data_frame_col_condition = data_frame.loc[:, 'COUNT PARTICIPANTS']
print(data_frame_col_condition.values[0])