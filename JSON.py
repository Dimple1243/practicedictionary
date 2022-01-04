# import json
# data='{"var1":"harry","var2":56}'
# parsed=json.loads(data)
# print(type(parsed))

import json
data='{"name":"dimple","cars":["bmw","audi8","ferrari"],"fridge":("roti,540)}'
jscomp=json.dumps(data)
print(jscomp)