import requests
import json
import xlsxwriter

import pandas as pd

df = pd.read_excel('singer_info流行.xlsx')
data = df.iloc[:,[3]]
# print(data)
# print(type(data))
# print(dir(data))
data = data.values.tolist()
# print(data)

file_name = '.\\song_mid流行.xlsx'
workbook = xlsxwriter.Workbook(file_name)
worksheet = workbook.add_worksheet('first_sheet')
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
}
# worksheet.write_row('A1',['song_mid'])

# for item in data:
#     url = 'https://v1.itooi.cn/tencent/song/artist?id={}'.format(item[0])

for j in range(len(data)):
    url = 'https://v1.itooi.cn/tencent/song/artist?id={}'.format(data[j][0])


# url = 'https://v1.itooi.cn/tencent/song/artist?id=001fNHEf1SFEFN'
    ret = requests.get(url,headers=headers).text
    ret = json.loads(ret)['data']

    for i in range(len(ret)):
        worksheet.write_row(f'A{30*j+i+1}',[ret[i]['musicData']['songmid']])
    print(data[j])
workbook.close()
