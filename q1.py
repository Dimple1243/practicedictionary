# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# for i in d2:
#     if i in d1:
#         d1[i]=d1[i]+d2[i]
#     else:
#         d1[i]=d2[i]
# print(d1)


# dic1={'a':10,'b':12,'c':16}
# dic2={'d':12,'v':14,'c':18}
# for i in dic2:
#     if i in dic1:
#         dic1[i]=dic1[i]+dic2[i]
#     else:
#         dic1[i]=dic2[i]
# print(dic1)

dic={'param':20,'anjili':30,'bijender':45,'roshini':50,'deepak':60}
d={}
lenghth=len(dic)
for i in range(lenghth):
    max=0
    for value in dic:
        if max<dic[value]:
            max=dic[value]
            key=value
    d.update({key:max})
    dic.pop(key)
print(d)





