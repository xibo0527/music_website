import sqlite3
import xlrd

# xlrd：操作Excel
# pandas


#　连接数据库
conn = sqlite3.connect('../db.sqlite3')
cur = conn.cursor()

# 清空表
# sql = "delete from repo_musicinfo"
# cur.execute(sql)
# conn.commit()

# 读取数据并入库
workbook = xlrd.open_workbook('song_info_轻音乐.xlsx')
sheet_names= workbook.sheet_names()
for sheet_name in sheet_names:
    sheet = workbook.sheet_by_name(sheet_name)
    print(sheet_name)
    # 获取行数
    print(sheet.nrows)
    try:
        for i in range(1, sheet.nrows):
            print(f"正在插入第{i}行")
            # print(sheet.row_values(i))
            name = sheet.row_values(i)[0]
            song_mid = sheet.row_values(i)[1]
            url = sheet.row_values(i)[2]
            img = sheet.row_values(i)[3]
            lyric = sheet.row_values(i)[4]
            category = 4
            singer_mid = sheet.row_values(i)[5]
            sql = f"""insert into repo_musicinfo ('name', 'song_id', 'url', 'img','lyric','category_id','singer_id') values ('{name}','{song_mid}','{url}','{img}','{lyric}','{category}','{singer_mid}')"""
            cur.execute(sql)
    except Exception as e:
            print('error', e)
    conn.commit()
    # sql = "select * from repo_questions"
    # cur.execute(sql)
    # print(cur.fetchall())

conn.close()
# rows = sheet2.row_values(3) # 获取第四行内容
# cols = sheet2.col_values(1) # 获取第二列内容
# print(rows)
# print(cols)
#

