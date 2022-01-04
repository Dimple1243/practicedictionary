# dic1={1:10,2:20}
# dic2={3:30,2:40}
# dic3={5:50,6:60}
# dic4={}
# for i in dic1:
#     for j in dic2:
#         if i in dic2:
#             dic4[i]=dic1[i]+dic2[i]
#             if i!=j:
#                 dic4[j]=dic2[j]
#         else:
#             dic4[i]=dic1[i]
# for l in dic3:
#     if i in dic3:
#         dic4[i]=dic1[i]+dic3[l]
#         if j in dic3:
#             dic4[j]=

i = int(input("enter a number :"))
i=str(i)
l= ((len(i)-1)*"0")
n = ""
j=0
c=1
while j< len(i):
    l= i[j]+((len(i)-c)*"0")
    if i[j]!= "0":
        n=n+l
        if i[j]!= "0" and j!=len(i)-1:
            n=n+"+"
    c+=1
    j+=1
k=len(n)-1
if n[k]=="+":
    print(n[:k])
else:
    print(n)
