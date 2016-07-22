import MySQLdb

class db_init(object):

    file_tb = {"2013-1":"tb201301","2013-2":"tb201302","2014-1":"tb201401"}
    path = "./org_data/"
    sql_L = "insert into "
    sql_R = " values(%s,%s,%s,%s)"
    
    def insert_one_line(self,param):
        flag = self.cursor.execute(self.sql_L + self.tbname + self.sql_R, param)
        return flag
    
    def __init__(self, filename):
        self.tbname = self.file_tb[filename]
        self.filename = filename
        datafile = open(self.path + self.filename + '.txt', 'r') 
        self.lines = datafile.readlines()
        self.conn = MySQLdb.connect("localhost","chenxingyou","123456","grade")
        self.cursor = self.conn.cursor()

    def insert_db(self):
        for line in self.lines:
            line = line.strip()

            if line == '':
                break

            line = line.split('\t')
            print line

            db_line = [int(line[0]),int(line[1]),float(line[2]),float(line[3])]
            flag = self.insert_one_line(db_line)
            if flag != 1:
                print "error insert!"
                return False
       
        return True
    
    def db_init(self):
        flag = self.insert_db()

        self.conn.commit()
        if flag is True:
            self.cursor.execute("select count(*) from " + self.tbname)
            cds = self.cursor.fetchall()
            print cds
        self.cursor.close()
        self.conn.close()

if __name__ == "__main__":
    print "start to run"
    d = db_init("2013-2")
    d.db_init()
