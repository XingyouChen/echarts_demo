import MySQLdb

class get_context:
    def get_tuple(self):
        conn = MySQLdb.connect("localhost","chenxingyou","123456","grade")
        cursor = conn.cursor()
        cursor.execute("select * from tb201301")
        self.context_tuple = cursor.fetchall()
        cursor.close()
        conn.close()
#        print self.context_tuple[0]

    context_list_com = []
    context_list_test = []

    def get_list(self):
        self.get_tuple()

        for line_tuple in self.context_tuple:
            line_list = [int(line_tuple[1]) % 1001 % 730,float(line_tuple[2])]
            self.context_list_com.append(line_list)
            line_list = [int(line_tuple[1]) % 1001 % 730,float(line_tuple[3])]
            self.context_list_test.append(line_list) 
 #       print self.context_list_com[0]
 #       print self.context_list_test[0]
    
    def write_file(self):
        fout = open("context.txt",'w')
        fout.write(str(self.context_list_com) + '\n')
        fout.write(str(self.context_list_test))
        fout.close()

if __name__ == '__main__':
#    print "start to run."

    get_context_c = get_context()
    
    get_context_c.get_list()
    
    get_context_c.write_file()

    #print get_context_c.context_list_com
