import web
#from context_load import write_data_js

render = web.template.render('templates/')
urls = ('/zhuzhuang', 'zhuzhuang_index')

class zhuzhuang_index:
    def GET(self):
        #name = 'Mike'
        return render.zhuzhuang_index()

if __name__ == "__main__":
 #   data_load = write_data_js()
#    data_load.js_write() 
    app = web.application(urls, globals())
    app.run()
