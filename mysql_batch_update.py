#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import datetime
import time
import MySQLdb
import sys
import re
reload(sys)
sys.setdefaultencoding('utf8')
if __name__ == "__main__":

	db = MySQLdb.connect(host='localhost',user='root',passwd='123456', port=3306, db='yunba',charset='utf8')
	try:
		db_cursor = db.cursor()
		db_cursor.execute('select imei from device_config where lock_type=6')
		rows = db_cursor.fetchall()
		with open('/tmp/mysql_tmp.txt', 'w') as fout:
			#print >>fout, rows
			for row in rows:
				fout.write('%s\n'%(row[0]))
		db_cursor.close()
	except Exception,e:
		print e
	finally:
		db.close()

	db1 = MySQLdb.connect(host='localhost',user='root',passwd='123456', port=3306, db='yunba',charset='utf8')
	db_cursor1 = db1.cursor()
	count = 0

	for line in open("/tmp/mysql_tmp.txt"):
		line = line.strip('\n')
		if len(line) == 12:
			tmp = re.findall(r'.{2}', line)
			mac = tmp[0]+':'+tmp[1]+':'+tmp[2]+':'+tmp[3]+':'+tmp[4]+':'+tmp[5]
			# print mac,line
			sql="update device_config set ble_mac_address = '%s' where imei='%s';"%(mac,line)
			# print sql
			try:
				db_cursor1.execute(sql)  # 执行sql语句
				db1.commit()  # 提交到数据库执行
				count +=1
			except:
				db1.rollback()  # 发生错误后回滚
		else:
			print line,type(line),len(line)
	print count
	db1.close()  # 关闭数据库