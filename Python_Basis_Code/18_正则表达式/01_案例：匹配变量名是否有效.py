import re

names = ["name1", "_name", "2_name", "_name_"]
ok_name = list()
for name in names:
    ret = re.match(r"^[a-zA-Z_][a-zA-Z0-9]*$", name)
    if ret is not None:
        ok_name.append(ret.group())
print(ok_name)
