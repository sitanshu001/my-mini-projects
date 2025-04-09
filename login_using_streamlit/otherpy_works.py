import pandas as pd
log_df=pd.read_csv('loginpy.csv')

if 'password' in log_df['pass'].values:
    print('yes')
