# -*- coding: UTF-8 -*-



class HtmlOutputer(object):
    def __init__(self):
        self.datas = []
    
    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)
    
    def output_html(self):
        fout = open('output.html', 'w', encoding='UTF-8')
        
        fout.write("<html>")
        fout.write("<head>")
        fout.write('<meta charset="UTF-8"></meta>')
        fout.write("<title>Crawl Result</title>")
        fout.write("</head>")
        fout.write("<body>")
        fout.write('<h1 style="text-align:center">Crawl Result</h1>')
        fout.write('<table style="border-collapse:collapse;"  border="1">')
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td><a href='%s'>%s</a></td>" % (data["url"],data["title"]))
            fout.write("<td>%s</td>" % data["summary"])
            fout.write("</tr>")
        fout.write("</table>")
        fout.write('<br /><br /><p style="text-align:center">Power By Edwin.Xie</p>')
        fout.write("</body>")
        fout.write("</html>")
        fout.close()
    
    



