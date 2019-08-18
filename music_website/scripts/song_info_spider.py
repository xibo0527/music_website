import pandas as pd
import requests
import json
import xlsxwriter

df = pd.read_excel('song_mid_流行.xlsx')
data = df.iloc[:,[0]]
data = data.values.tolist()

'''
[['000P8peU0HhORi'], ['002E3MtF0IAMMY'], ['000wocYU11tSzS']]
'''
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
}

file_name = '.\\song_info_流行.xlsx'
workbook = xlsxwriter.Workbook(file_name)
worksheet = workbook.add_worksheet('first_sheet')
worksheet.write_row('A1',['name','song_mid','url','img','lyric'])
for i in range(len(data)):
    try:
        music_detail_url = 'https://v1.itooi.cn/tencent/song?id={}'.format(data[i][0])
        ret = requests.get(music_detail_url,headers=headers).text
        ret = json.loads(ret)['data'][0]
        song_name = ret['title']
        singer_name = ret['singer'][0]['name']
        song_url = 'https://v1.itooi.cn/tencent/url?id={}&quality=128'.format(data[i][0])
        song_img = 'https://v1.itooi.cn/tencent/pic?id={}'.format(data[i][0])
        song_lyric = 'https://v1.itooi.cn/tencent/lrc?id={}'.format(data[i][0])
        worksheet.write_row(f'A{i+2}',[f'{song_name}-{singer_name}',data[i][0],song_url,song_img,song_lyric])
        print(f'第{i+2}行写入完成')
    except Exception as e:
        pass
workbook.close()
