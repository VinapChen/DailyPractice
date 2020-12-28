# -*- coding: utf-8 -*-
import xlrd
import os


if __name__ == '__main__':
    # 打开excel文件
    data1 = xlrd.open_workbook("./no_upgarde_pre4.xlsx")
    # 读取第一个工作表
    table = data1.sheets()[0]
    # 统计行数
    n_rows = table.nrows
    print n_rows

    for v in range(0, n_rows):
        values = table.row_values(v)[0]
        print values

        command = "ssh %s \'" \
                  "echo Y | sudo apt-get remove iftop && " \
                  "rm m4_1.4.18.orig.tar.xz flex-2.5.37.tar.gz bison-2.7.tar.gz ncurses-6.1.tar.gz libpcap-1.5.3.tar.gz iftop-1.0pre4.tar.gz &&" \
                  "rm -rf m4-1.4.18/ flex-2.5.37/ bison-2.7/ ncurses-6.1/ libpcap-1.5.3/ iftop-1.0pre4/ &&" \
                  "wget https://launchpad.net/ubuntu/+archive/primary/+sourcefiles/m4/1.4.18-2/m4_1.4.18.orig.tar.xz && tar -xvf m4_1.4.18.orig.tar.xz && cd  m4-1.4.18/ && ./configure && make && sudo make install && cd .. &&" \
                  "wget http://nchc.dl.sourceforge.net/project/flex/flex-2.5.37.tar.gz && tar -zxvf flex-2.5.37.tar.gz && cd flex-2.5.37/ && ./configure && make && sudo make install && cd .. && " \
                  "wget http://ftp.gnu.org/gnu/bison/bison-2.7.tar.gz && tar -zxvf bison-2.7.tar.gz && cd bison-2.7/ && ./configure && make && sudo make install && cd .. && " \
                  "wget https://ftp.gnu.org/pub/gnu/ncurses/ncurses-6.1.tar.gz && tar -zxvf ncurses-6.1.tar.gz && cd ncurses-6.1/ && ./configure && make && sudo make install && cd .. && " \
                  "wget http://www.tcpdump.org/release/libpcap-1.5.3.tar.gz && tar -zxvf libpcap-1.5.3.tar.gz && cd libpcap-1.5.3/ && ./configure && make && sudo make install && cd .. && " \
                  "wget http://www.ex-parrot.com/pdw/iftop/download/iftop-1.0pre4.tar.gz && tar zxvf iftop-1.0pre4.tar.gz &&  cd iftop-1.0pre4/ && ./configure && make && sudo make install && cd .. && " \
                  "sudo ldconfig &&" \
                  "sudo iftop -i eth0 -t -s 1 &&" \
                  "rm m4_1.4.18.orig.tar.xz flex-2.5.37.tar.gz bison-2.7.tar.gz ncurses-6.1.tar.gz libpcap-1.5.3.tar.gz iftop-1.0pre4.tar.gz &&" \
                  "rm -rf m4-1.4.18/ flex-2.5.37/ bison-2.7/ ncurses-6.1/ libpcap-1.5.3/ iftop-1.0pre4/ " \
                  "\'"%values

        command_check = "ssh %s \'sudo iftop -i eth0 -t -s 1\'" % values
        try:
            result = os.system(command_check)
            if result != 0:
                print os.system(command)
        except Exception as e:
            print "error:",e
