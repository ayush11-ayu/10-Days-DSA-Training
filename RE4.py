import re
x="\\s"
x="\\S"
x="\\d"
x="\\D"
x="\\w"
x="\\W"
matcher=re.finditer(x,"a7bD2@k2$D8z")
for match in matcher:
    print(match.start(),'...',match.group())
