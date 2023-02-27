import pymysql
def Mysql_handle(result):
    ''' 
    :param result: [(arg1,arg2)]
    :return: 
    '''
    # 打开数据库连接
    db = pymysql.Connect(
        host='192.168.3.50',
        port=3306,
        user='root',
        passwd="root",
        db='test',
        charset="utf8"
    )
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    try:
        # 执行sql语句
        cursor.executemany("INSERT INTO Grafana_Data(value, metric)  VALUES (%s,%s)",result)
        import time
        t1 = (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        print ('%s Inserting data %s ........'% (t1,result))
        # 提交到数据库执行
        db.commit()
    except Exception as e:
        # 如果发生错误则回滚
        print(e)
        db.rollback()
    finally:
        sql2 = 'select * from Grafana_Data '
        cursor.execute(sql2)
        results = cursor.fetchall()
        print(results)
    # 关闭数据库连接
    db.close()
