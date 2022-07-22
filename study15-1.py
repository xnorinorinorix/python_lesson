import re

st = "The ghost that says boo haunts the loo"

ex = re.findall(".oo", st)

print(ex)
