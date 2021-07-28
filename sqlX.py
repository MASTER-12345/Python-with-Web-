
import sqlite3
import  csv
#操作数据库工具

class SqliteX:


    #查询表名字段
    def search_head(self,db):
        conn = sqlite3.connect(db)
        cu = conn.cursor()

        # 获取表名，保存在tab_name列表
        cu.execute("select name from sqlite_master where type='table'")
        tab_name = cu.fetchall()
        tab_name = [line[0] for line in tab_name]

        # 获取表的列名（字段名），保存在col_names列表,每个表的字段名集为一个元组
        col_names = []
        for line in tab_name:
            cu.execute('pragma table_info({})'.format(line))
            col_name = cu.fetchall()
            col_name = [x[1] for x in col_name]
            col_names.append(col_name)

        return col_names[0]
    #增
    def insert_for(self,db,date):

        print(db)
        print(date)
        head=SqliteX.search_head(1,db)
        print(head)

        head_=tuple(head)
        print(head_)
        date_=tuple(date)
        print((date_))

        sql="INSERT INTO COMPANY"+"%s"%str(head_)+"VALUES"+"%s"%str(date_)
        print(sql)



        conn = sqlite3.connect(db)
        c = conn.cursor()

        c.execute("%s"%sql)

        conn.commit()

        conn.close()
    #查All
    def search_all(self,db):
        conn = sqlite3.connect(db)
        c = conn.cursor()


        cursor = c.execute("SELECT *  from COMPANY")
        for row in cursor:
          print(row)
        conn.close()
    #查指定
    def search_which(self,db,type,value):

        conn = sqlite3.connect(db)
        c = conn.cursor()
        sql="SELECT *  from COMPANY Where"+" "+"%s"%(type)+"="+"%s"%value


        cursor = c.execute(sql)
        for row in cursor:
            print(row)
        conn.close()

    #删全部
    def del_all(self,db):
        conn = sqlite3.connect(db)
        c = conn.cursor()
        c.execute("DELETE  from COMPANY ;")
        conn.commit()
        conn.close()
        print("删除成功！")
    #删除某个
    def del_which(self,db,type,value):

        conn = sqlite3.connect(db)
        c = conn.cursor()

        sql="DELETE from COMPANY where"+" "+"%s"%type+"="+"%s"%value
        print(sql)

        c.execute(sql)
        conn.commit()

        conn.close()
    #更新某个数据
    def update_which(self,db,type,type_value,where,where_value):
        conn = sqlite3.connect(db)
        c = conn.cursor()
        sql="UPDATE COMPANY set"+"  "+"%s"%(type)+"="+"'%s'"%(type_value)+"  "+"Where"+"  "+"%s"%(where)+"="+"%s"%(where_value)
        print(sql)
        c.execute(sql)
        conn.commit()
        conn.close()
        print("更新成功！")


class CsvX:
    def search_all(self):
        print('')


class MysqliteX:
    def search_all(self):
        print('')




