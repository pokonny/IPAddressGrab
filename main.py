import socket
import pandas as pd
from socket import gethostbyname, gaierror

#Excel File Sheet Name. Make sure the excel sheet is located in the same folder as the program
#Switch Columns to capture right values
worksheet = pd.read_excel("Excel File that you want to read.xlsx", sheet_name='Sheet1', usecols='B')

#starts from the top of the file
worksheet.head()

#converts excel values into a list
mylist = worksheet['HOSTNAME'].tolist()

#iterates over list and prints ip addresses
for line in mylist:
   try:
    line = line.replace("\xa0", "")
    a = socket.gethostbyname(line)
    print(a)
   except gaierror:
      print(line)