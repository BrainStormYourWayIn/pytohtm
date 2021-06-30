# Please read the documentation for importing
from sierra import *

title('nothing')
#addInitc()
head('nothing more', font_size='90px', color='blue', text_align='center', background_color='orange')
openBody(background_color='green', opacity=0.8)
    
x = tTags(True)
x.start_p("I'm sure about this man")
x.css(color='red', background_color='orange', line_height='25px')
closeTags('p')

x = tTags(div_class='newClass')
x.start_div()
x.css(color='yellow', font_family='Times New Roman', background_color='blue')

writeHTML("I'm REALLY" + b + "sure of this")
closeTags('div')

s_class = 'anotherClass'
x = tTags(sec_class=s_class)
x.start_sec()
x.css(color='whitesmoke', background_color='rgb(35, 51, 89)')

writeHTML("I'm defo" + b + "sure of this")
closeTags('section')

a = startTable()
c = ['england', 'best', 'six', 'euros']
r1 = ['kane', 'grealish', 'sancho', 'sterling']
r2 = ['foden', 'mount', 'bellingham', 'reece']
r3 = ['trippier', 'stones', 'walker', 'coady']
a.createTable(cols=c, r1, r2, r3)
#a.getTable("path\to\csv\file.csv")
    
closeBody()
closeHTML()
autoPrettify()