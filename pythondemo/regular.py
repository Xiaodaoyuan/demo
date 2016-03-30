import re

pattern=re.compile('hello')

result1=re.match(pattern,'helloHHHHhelloHsidasfhellosfaosdf')
result2=re.search(pattern,'hlloHHHHhelloHsidasfhellosfaosdf')
result3=re.split(pattern,'helloHHHHhelloHsidasfhellosfaosdf')
result4=re.findall(pattern,'helloHHHHhelloHsidasfhellosfaosdf')
result5=re.finditer(pattern,'helloHHHHhelloHsidasfhellosfaosdf')
print result1.group()
print result2.group()
print result3
print result4
print [m.group() for m in result5]
