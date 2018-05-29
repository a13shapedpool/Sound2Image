import urllib.request as urlr
import urllib.parse as urlp
import re

url = ''
values = {'s': 'basic',
          'submit': 'search'}

data = urlp.urlencode(values)
data = data.encode('utf-8')
req = urlr.Request(url, data)
resp = urlr.urlopen(req)
respData = resp.read()


# !-- First Section -->\n<p class=\'verse\'>

paragraphs = re.findall(r'Section -->(.*?)<!--',str(respData))
# paragraphs = paragraphs[1:]

for p in paragraphs:
    line = p.split('<br>\\n')

    print("ALO", line)
    # for l in line:
    #     print("SALUT    ")
    #     print(l)
    #     # new_line=str(l)
    #     new_line = l.split('</p>')
    #     new_line = l.replace(r"\'", "'").replace("<p class='verse'>","")
    #
    #     # print(new_line)
