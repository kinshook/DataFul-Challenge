

            #remove  empty and unused cols
#dfs.drop(columns=['unit','note'], inplace= True)
# print(dfs.head(5))
# Finds exact duplicates based on selected columns
# dups = dfs[dfs.duplicated(keep=False)]
# print(f"dups: {dups.shape[0]}" )

# dfs['date'] = pd.to_datetime(dfs['date'], format='mixed')
# print(dfs.dtypes)
#print(dfs.isna().sum())    #sum the number of nulls 
df1= pd.read_csv(r"D:\KG PD\KG\Codebasics\Codebasics DATAFUL Chll\CodeBasics Dataful co chll\rpc16_input_file\DATASETS\Diseases AQI dataset.csv",encoding='latin')
df1_copy= df1.copy()
df1_copy=df1.to_csv('staging_AQI_diseases.csv', index= False)
df1_copy_df=pd.read_csv('staging_AQI_diseases.csv')
# print(df1_copy.head(5))
print(df1_copy_df.dtypes)
df1_copy_df['year'] = pd.to_datetime(df1_copy_df['year'].astype(str) + '-01-01').dt.year
#print(df1_copy.tail(5))
print(df1_copy_df.dtypes)
print(df1_copy_df['year'].apply(lambda x: isinstance(x, int)).all())
#if df1_copy_df.iloc[1280:1851,0:12].is