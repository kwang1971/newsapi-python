import pymysql

json = [
    {"time": 1605868916, "kw": "携程"},
    {"time": 1605868992, "kw": "丽江"},
    {"time": 1605869065, "kw": "c6179"},
    {"time": 1605869267, "kw": "丽江景点"},
    {"time": 1605869312, "kw": "女童误服近40粒降压药不幸身亡"},
    {"time": 1606112160, "kw": "python爬虫请求头"},
    {"time": 1606112420, "kw": "useragent"},
    {"time": 1606112494, "kw": "手机useragent"},
    {"time": 1606112849, "kw": "谷歌浏览器useragent"},
    {"time": 1606114944, "kw": "百度贴吧"},
]


def insert(json):
    connect = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="",
        database="python",
        charset="utf8",
    )
    cursor = connect.cursor()
    # 循环插入数据库中
    for i in range(len(json)):
        sql = "insert into users(name, age) value('%s','%s')" % (
            json[i]["time"],
            json[i]["kw"],
        )
        cursor.execute(sql)
        connect.commit()

    connect.close()


insert(json)
