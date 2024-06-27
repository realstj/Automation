## Annual Capital Gain calculation for Tax return
This Jupyter notebook extract data from a excel file with all tracsactions since 2020 and load into a dataframe.
Then the capital gain for the tax year (e.g. 2022-2023 as 2023) will be calculated via First In First Out rule. 
The result will be exported into a excel file. 

Note #1 - Currently, this notebook works for the US market transaction data from stake.com while there is another version for the transactions in Australian market from both Commsec and stake.com. 
Note #2 - The input file, in excel format, should be prepared via extract and transform (cleanse) process from the different original tax statements in, pdf files or excel files, and will be loaded into a dataframe at the first part of the notebook. 

Next changes will be: 
 - Unifying input process for both Australian and US market into one notebook.
 - Automatic extraction of data from the original files (pdf, excel)
 - Defining a function for the whole process thus we can use it as a function with a input file excution.
 - Modifying code to make it work with an input "Year" without changing code. 
 - ...