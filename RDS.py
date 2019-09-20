#!/usr/bin/env python
#-*-encoding:utf-8 -*-
import MySQLdb
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def test_mysql():
    for i in range(10,1000000):
        try:
            #connection = MySQLdb.connect(user='root',passwd='',host='127.0.0.1',db='mysqltest',port=3306)
            connection = MySQLdb.connect(user='soul',passwd='soul_sall123',host='rm-bp1g1qmm8c84t8y453o.mysql.rds.aliyuncs.com',db='mysqltest',port=3306,connect_timeout=5)
            cursor = connection.cursor()
            cursor.execute("SELECT * from testable")
            for row in cursor.fetchall():
                print row[1] + str(i)
            connection.close()

        except:
            print 'mysql 读连接失败%s' %i 
            w = open("/data/bash/test.txt","a+")
            w.write('mysql 读连接失败%s' %i + '\n') 
            w.close()
        try:
           #connection = MySQLdb.connect(user='root',passwd='',host='127.0.0.1',db='mysqltest',port=3306)
           connection = MySQLdb.connect(user='soul',passwd='soul_sall123',host='rm-bp1g1qmm8c84t8y453o.mysql.rds.aliyuncs.com',db='mysqltest',port=3306,connect_timeout=5)
           cursor = connection.cursor()
           sql = "insert into test_write(`country`) values ('CN_%s');" %str(i)
           cursor.execute(sql)
           connection.commit()
           connection.close()
           print '数据写完完成CN_%s' %i
        except:
           print 'mysql 写连接失败%s' %i
           wr = open("/data/bash/test-write.txt","a+")
           wr.write('mysql 写连接失败%s' %i + '\n') 
           wr.close()

if __name__ == "__main__":
     test_mysql()
