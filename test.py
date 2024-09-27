import re
s = "test und so methoden in python"
s2 = re.sub("\s", "-", s)
print(s2)