#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import datetime
import time
import MySQLdb
import sys
import re

import xlrd

reload(sys)
sys.setdefaultencoding('utf8')

if __name__ == "__main__":

    # 打开excel文件
    data1 = xlrd.open_workbook("/Users/yunba/Documents/egbin_bike_document/150把锁编号对应SN.xlsx")
    # 读取第一个工作表
    table = data1.sheets()[0]
    # 统计行数
    n_rows = table.nrows
    print (n_rows)
    counts = 0
    delete_counts = 0
    insert_counts = 0
    update_counts = 0

    # db = MySQLdb.connect(host='localhost', user='root', passwd='Yunba@123456', port=3306, db='yunba',
    #                      charset='utf8')

    db_elogic = MySQLdb.connect(host='101.200.89.11', user='root', passwd='Yunba@123456', port=3306, db='yunba',charset='utf8')
    for v in range(2, n_rows):
        value = table.row_values(v)[0]
        bike_id = str(int(value))
        print (bike_id, len(bike_id))
        sn = table.row_values(v)[1][2:]
        print (sn, len(sn))
        # bike_id = "0" + table.row_values(v)[3]
        # print (bike_id, len(bike_id))

        db_elogic_cursor = db_elogic.cursor()
        sql_update = "update device_config set bike_id = %s where bike_id=%s" % ("\'" + bike_id + "\'", "\'" + sn + "\'")
        print (sql_update)
        try:
            # 执行SQL语句
            db_elogic_cursor.execute(sql_update)
            # 提交到数据库执行
            db_elogic.commit()

            print ("update:", sn, "," , bike_id , ",", bike_id)
            update_counts += 1
        except:
            # 发生错误时回滚
            db_elogic.rollback()

        # try:
        #     db_cursor = db.cursor()
        #     sql_select = "select * from device_config where imei=\'%s\'" % imei
        #     # print sql_select
        #
        #     db_cursor.execute(sql_select)
        #     db_elogic_cursor = db_elogic.cursor()
        #
        #     rows = db_cursor.fetchall()
        #     if len(rows) == 1:
        #         counts += 1
        #
        #         lock_id = rows[0][8]
        #         lock_uid = int(lock_id,16)
        #         # print lock_id,lock_uid
        #
        #         sql_update = "update device_config set bike_id = %s where imei=%s" % ("\'" + values + "\'","\'" +imei+"\'")
        #         try:
        #             # 执行SQL语句
        #             db_elogic_cursor.execute(sql_update)
        #             # 提交到数据库执行
        #             db_elogic.commit()
        #
        #             print "update:", lock_uid
        #             update_counts += 1
        #         except:
        #             # 发生错误时回滚
        #             db_elogic.rollback()
        #
        #         # sql_delete = "delete from device_config where imei=\'%s\'" % imei
        #         # # print sql_delete
        #         # sql_insert = "insert into device_config (appkey, bike_id, imei, lock_type, aes_key, ble_mac_address, ble_broadcast_name, lock_id, password) " \
        #         #              "values (%s,%s,%s,%d,%s,%s,%s,%s,%s)" % \
        #         #              ("\'59156e35f1ae5ffe3671305a\'", values, imei, 4,
        #         #               "\'11111111000000000000000011111111\'", "\'00:11:22:33:44:55\'", "\'" + rows[0][7] + "\'",
        #         #               "\'" + rows[0][8] + "\'", "\'NULL\'")
        #         # # print sql_insert
        #         #
        #         # db_elogic_cursor = db_elogic.cursor()
        #         # try:
        #         #     # 执行SQL语句
        #         #     db_elogic_cursor.execute(sql_delete)
        #         #     # 提交修改
        #         #     db_elogic.commit()
        #         #     print "delete:", imei
        #         #     delete_counts += 1
        #         #
        #         # except:
        #         #     # 发生错误时回滚
        #         #     db_elogic.rollback()
        #         #
        #         # try:
        #         #     # 执行sql语句
        #         #     db_elogic_cursor.execute(sql_insert)
        #         #     # 提交到数据库执行
        #         #     db_elogic.commit()
        #         #     print "insert:", imei
        #         #     insert_counts +=1
        #         # except:
        #         #     # Rollback in case there is any error
        #         #     db_elogic.rollback()
        #
        #     elif len(rows) == 0:
        #         print values, imei
        #     db_cursor.close()
        # except Exception, e:
        #     print e

    # db.close()
    db_elogic.close()
    print ("all counts", counts)
    print ("delete counts", delete_counts)
    print ("insert counts", insert_counts)
    print ("update counts", update_counts)
