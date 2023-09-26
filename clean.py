import pandas as pd

# load the dataset
df1 = pd.read_csv('crop.csv', low_memory=False)
df1.shape

# create dictionary of SiteID and Location values
siteID_location = {188: 'AURN Bristol Centre', 203: 'Brislington Depot', 206: 'Rupert Street', 209: 'IKEA M32', 213: 'Old Market', 215: 'Parson Street School', 228: 'Temple Meads Station', 270: 'Wells Road', 271: 'Trailer Portway P&R', 375: 'Newfoundland Road Police Station', 395: "Shiner's Garage", 452: 'AURN St Pauls', 447: 'Bath Road', 459: 'Cheltenham Road \\ Station Road', 463: 'Fishponds Road', 481: 'CREATE Centre Roof', 500: 'Temple Way', 501: 'Colston Avenue', 672: 'Marlborough Street'}

# filter for mismatch in SiteID and Location values
mismatch = df1.loc[df1['SiteID'].isin(siteID_location) & (df1['Location'] != df1['SiteID'].map(siteID_location)), ['SiteID', 'Location']]

# print mismatched rows
if not mismatch.empty:
    print("Mismatch found in the following rows:")
    print(mismatch)

    # fill 0 to any of the mismatch found
    df1.loc[mismatch.index, 'Location'] = 0
    
    # delete any mismatch replaced with 0
    df1.drop(df1[(df1['SiteID'].isin(siteID_location)) & (df1['Location'] == 0)].index, inplace=True)

    # save the clean csv as clean.csv
    df1.to_csv('clean.csv', index=False)
    print("Clean dataset saved as clean.csv")
    df1.shape

else:
    print("No mismatches found.")
    

