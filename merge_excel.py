import os
import pandas as pd
import numpy as np

dir = "D:/txt"#設定工作路徑
#新建列表，存放檔名（可以忽略，但是為了做的過程能心裡有數，先放上）
filename_excel = []
#新建列表，存放每個檔案資料框（每一個excel讀取後存放在資料框）
frames = []
for root,dirs,files in os.walk(dir):
  for file in files:
    #print(os.path.join(root,file))
    filename_excel.append(os.path.join(root,file))
    df = pd.read_excel(os.path.join(root,file),engine='openpyxl') #excel轉換成DataFrame
    frames.append(df)
#列印檔名
print(filename_excel)  
 #合併所有資料
result = pd.concat(frames)  
#檢視合併後的資料
result.head()
result.shape

result.to_csv('D:/merge/0930.csv',sep=',',index = False)#儲存合併的資料到電腦D盤的merge資料夾中，並把合併後的檔案命名為a12.csv