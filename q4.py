basic_salary=int(input("enter the basic salary "))
if basic_salary>10000:
  DA=basic_salary*80/100
  HRA=basic_salary*18/100
  print(basic_salary+DA+HRA)
elif basic_salary<=20000:
    DA=(basic_salary*90)/100
    HRA=(basic_salary*25)/100
    print(basic_salary+DA+HRA)
else:
    basic_salary>=20000
    DA=(basic_salary*95)/100
    HRA=(basic_salary*30)/100
    


