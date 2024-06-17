# FIFO Capital gain calculation

import pandas as pd
import logging

# Import Excel file
df = pd.read_excel("tax_2021.xlsx", sheet_name="Sheet2")
df.head()

# Seperate Stock names
df_1 = pd.read_excel("tax_2021.xlsx", sheet_name="Sheet2", skiprows=1, nrows=9)
df_1.drop(columns=['Company', 'Unit Price ($)', 'Trade Value ($)', 'Brokerage+GST ($)', 'GST ($)', 'Contract Note'], inplace=True)
df_1['Unit Value ($)'] = df_1['Total Value ($)'] / df_1['Quantity']

df_2= pd.read_excel("tax_2021.xlsx", sheet_name="Sheet2", skiprows=12, nrows=4)
df_2.drop(columns=['Company', 'Unit Price ($)', 'Trade Value ($)', 'Brokerage+GST ($)', 'GST ($)', 'Contract Note'], inplace=True)
df_2['Unit Value ($)'] = df_2['Total Value ($)'] / df_2['Quantity']

df_3= pd.read_excel("tax_2021.xlsx", sheet_name="Sheet2", skiprows=21, nrows=3)
df_3.drop(columns=['Company', 'Unit Price ($)', 'Trade Value ($)', 'Brokerage+GST ($)', 'GST ($)', 'Contract Note'], inplace=True)
df_3['Unit Value ($)'] = df_3['Total Value ($)'] / df_3['Quantity']

df_4= pd.read_excel("tax_2021.xlsx", sheet_name="Sheet2", skiprows=27, nrows=17)
df_4.drop(columns=['Company', 'Unit Price ($)', 'Trade Value ($)', 'Brokerage+GST ($)', 'GST ($)', 'Contract Note'], inplace=True)
df_4['Unit Value ($)'] = df_4['Total Value ($)'] / df_4['Quantity']

# Concatenate data
df = pd.concat([df_1, df_2, df_3, df_4], axis=0) # Concatenate 2020 and 2021 data into a table
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True) # Date : String to datetime format
df.sort_values(['Code', 'Date'], ascending=True, inplace=True) # Sorting multiple names [Code, Date]
df.reset_index(drop=True, inplace=True) # Reset index from 0

mask1 = df['Code'] == 'MQG'
mask2 = df['Code'] == 'OSH'
mask3 = df['Code'] == 'IOZ'
mask4 = df['Code'] == 'NDQ'
mask5 = df['Code'] == 'SYI'
mask6 = df['Code'] == 'ETHI'

df1 = df[mask1]
df1.reset_index(drop=True, inplace=True)
df2 = df[mask2]
df2.reset_index(drop=True, inplace=True)
df3 = df[mask3]
df3.reset_index(drop=True, inplace=True)
df4 = df[mask4]
df4.reset_index(drop=True, inplace=True)
df5 = df[mask5]
df5.reset_index(drop=True, inplace=True)
df6 = df[mask6]
df6.reset_index(drop=True, inplace=True)

trans_list=list()
for i in range(0, df1.shape[0]):
    trans = Trans(df1['Date'][i].date(), df1['Quantity'][i], df1['Unit Value ($)'][i])
    trans_list.append(trans)
trans_result = balanceFifo(trans_list)
df1_capital = pd.DataFrame(trans_result, columns = ['Date Purchased', 'Date Sold', 'Quantity', 'Buy Price', 'Sell Price', 'Capital Gain'])
df1_capital

print(df1['Code'][0], df1_capital['Capital Gain'].sum())

trans_list=list()
for i in range(0, df2.shape[0]):
    trans = Trans(df2['Date'][i].date(), df2['Quantity'][i], df2['Unit Value ($)'][i])
    trans_list.append(trans)
trans_result = balanceFifo(trans_list)
df2_capital = pd.DataFrame(trans_result, columns = ['Date Purchased', 'Date Sold', 'Quantity', 'Buy Price', 'Sell Price', 'Capital Gain'])
df2_capital

print(df2['Code'][0], df2_capital['Capital Gain'].sum())

trans_list=list()
for i in range(0, df3.shape[0]):
    trans = Trans(df3['Date'][i].date(), df3['Quantity'][i], df3['Unit Value ($)'][i])
    trans_list.append(trans)
trans_result = balanceFifo(trans_list)
df3_capital = pd.DataFrame(trans_result, columns = ['Date Purchased', 'Date Sold', 'Quantity', 'Buy Price', 'Sell Price', 'Capital Gain'])
df3_capital

trans_list=list()
for i in range(0, df4.shape[0]):
    trans = Trans(df4['Date'][i].date(), df4['Quantity'][i], df4['Unit Value ($)'][i])
    trans_list.append(trans)
trans_result = balanceFifo(trans_list)
df4_capital = pd.DataFrame(trans_result, columns = ['Date Purchased', 'Date Sold', 'Quantity', 'Buy Price', 'Sell Price', 'Capital Gain'])
df4_capital

trans_list=list()
for i in range(0, df5.shape[0]):
    trans = Trans(df5['Date'][i].date(), df5['Quantity'][i], df5['Unit Value ($)'][i])
    trans_list.append(trans)
trans_result = balanceFifo(trans_list)
df5_capital = pd.DataFrame(trans_result, columns = ['Date Purchased', 'Date Sold', 'Quantity', 'Buy Price', 'Sell Price', 'Capital Gain'])
df5_capital

print(df5['Code'][0], df5_capital['Capital Gain'].sum())

trans_list=list()
for i in range(0, df6.shape[0]):
    trans = Trans(df6['Date'][i].date(), df6['Quantity'][i], df6['Unit Value ($)'][i])
    trans_list.append(trans)
trans_result = balanceFifo(trans_list)
df6_capital = pd.DataFrame(trans_result, columns = ['Date Purchased', 'Date Sold', 'Quantity', 'Buy Price', 'Sell Price', 'Capital Gain'])
df6_capital