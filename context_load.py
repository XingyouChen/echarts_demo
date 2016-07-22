from get_context import get_context

class write_data_js:
    def __init__(self):
        self.data_context = get_context()
        self.def_com = "var data_com = new Array();"
        self.def_test = "var data_test = new Array();"
        self.list_com = "data_com = "
        self.list_test = "data_test = "

    def data_load(self):
        self.data_context.get_list()

    def js_write(self):
        self.data_load()
        
        datafile = open("./static/js/sandian_data.js",'w')

        datafile.write(self.def_com + '\n' + self.def_test + '\n')

        self.list_com = self.list_com + str(self.data_context.context_list_com)
        self.list_test = self.list_test + str(self.data_context.context_list_test)
        datafile.write(self.list_com + ';\n' + self.list_test + ';')

        datafile.close()

if __name__ == '__main__':
    w = write_data_js()
    w.js_write()

