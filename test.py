import re
s = "test und so methoden in python"
s2 = re.sub(" ", "+", s)
print(s2)