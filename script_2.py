import pandas as pd


def normalized_csv(name_csv, name_norm_csv):
	df = pd.read_csv(name_csv, index_col=1)
	df.index = pd.to_datetime(df.index)
	df = df.resample('10T').fillna('ffill').drop('Unnamed: 0', 1)
	df.to_csv(name_norm_csv)


normalized_csv('AAVE_ETH_raw.csv', 'AAVE_ETH_normalized.csv')




# def fix_dates(df, frequency):
# 	df.index = pd.to_datetime(df.index)
# 	df = df.resample(frequency).fillna('ffill').drop('Unnamed: 0', 1)
# 	return df

# df = pd.read_csv('AAVE_ETH_raw.csv', index_col=1)
# df = fix_dates(df, '10T')
# df.to_csv('AAVE_ETH_normalized.csv')