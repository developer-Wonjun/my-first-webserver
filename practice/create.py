#!/usr/local/bin/python3
print("Content-Type: text/html")
print()
import cgi, os

files = os.listdir('data')
listStr = ''
for item in files:
  listStr = listStr + '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=item)


form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value
    description = open('data/'+pageId, 'r').read()
else:
    pageId = '우리는 송내동에 모여사는'
    description = '꿈 많은 청년들이야.'
print('''<!doctype html>
<html>
<head>
  <title>산골 팸</title>
  <meta charset="utf-8">
</head>

<body>
  <h1><a href="index.py"> 산 골</a></h1>
  <ul>
  {listStr}
  </ul>
  <a href="create.py">create</a>
  <form action="process_create.py" method="post">
      <p><input type="text" name="title" placeholder="title"></p>
      <p><textarea rows="4" name="description" placeholder="description"></textarea></p>
      <p><input type="submit"></p>
  </form>


</body>
</html>
'''.format(title=pageId, dscr=description, listStr=listStr)) 