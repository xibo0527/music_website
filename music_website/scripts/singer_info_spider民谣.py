import csv
import requests
import json
import xlsxwriter

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
}
# 民谣genre=3
url = 'https://v1.itooi.cn/tencent/artist/list?sexId=-100&areaId=-100&genre=3&index=-100&page={}&pageSize=80'.format(1)

ret = requests.get(url,headers=headers).text
ret = json.loads(ret)['data']
print(type(ret))


file_name = '.\\singer_info民谣.xlsx'
workbook = xlsxwriter.Workbook(file_name)
worksheet = workbook.add_worksheet('first_sheet')

worksheet.write_row('A1',['name','img','country','singer_mid','category'])
for i in range(len(ret)):
    worksheet.write_row(f'A{i+2}',[ret[i]['singer_name'],ret[i]['singer_pic'],ret[i]['country'],ret[i]['singer_mid'],2])
workbook.close()