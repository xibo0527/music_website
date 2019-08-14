import csv
import requests
import json
import xlsxwriter

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
}

url = 'https://v1.itooi.cn/tencent/artist/list?sexId=-100&areaId=-100&genre=-100&index=-100&page={}&pageSize=80'.format(1)

ret = requests.get(url,headers=headers).text
ret = json.loads(ret)['data']
print(type(ret))

# with open('singer_info.csv','w',encoding='utf-8') as csvfile:
#     fieldnames = ['name', 'img', 'country', 'singer_mid']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
#     for i in range(len(ret)):
#         writer.writerow({'name':ret[i]['singer_name'],'img':ret[i]['singer_pic'],'country':ret[i]['country'],'singer_mid':ret[i]['singer_mid']})

file_name = '.\\singer_info1.xlsx'
workbook = xlsxwriter.Workbook(file_name)
worksheet = workbook.add_worksheet('first_sheet')

worksheet.write_row('A1',['name','img','country','singer_mid'])
for i in range(len(ret)):
    worksheet.write_row(f'A{i+2}',[ret[i]['singer_name'],ret[i]['singer_pic'],ret[i]['country'],ret[i]['singer_mid']])
workbook.close()