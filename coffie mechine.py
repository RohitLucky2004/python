def checker(n,na,a5,a10,a20,a100,a200,a500):
    acs=(a5*5)+(10*a10)+(20*a20)+(100*a100)+(200*a200)+(500*a500)
    if acs>=na:
       change=acs-na
       print("collect your cash\n",change," cash retirved succesfully")
       print("please wait , your coffee is preparing")
    else:
        print("not enough money for selected item, try again later")

def coffee(n,na,itms):
    itms['Total Cash']+=na
    if n=='report':
        for i in itms.keys():
            print(i,"-",itms[i])
    else:
        itms['Water']-=0.020
        if n=='Tea':
           itms['Milk']-=0.160
           itms['Water']-=0.070
           itms['Sugar']-=0.100
           itms['Tea Powder']-=0.50
        elif n=='Coffee':
           itms['Coffee Powder']-=0.050
           itms['Milk']-=0.160
           itms['Water']-=0.050
           itms['Sugar']-=0.100
        elif n=='Black Coffee':
           itms['Black Powder']-=0.075
           itms['Water']-=0.200
           itms['Sugar']-=0.080
        elif n=='Green Tea':
           itms['Water']-=0.200
           itms['Green Powder']-=0.080
        elif n=='Cappuccino':
           itms['Coffee Powder']-=0.080
           itms['Milk']-=0.210
           itms['Water']-=0.010
           itms['Sugar']-=0.100
        print("your coffee is Ready, please collect it")
        
itms={'Milk':10.00,'Water':20.00,'Sugar':5.00,'Tea Powder':2.00,'Green Powder':2.00,'Black Powder':2.00,'Coffee Powder':3.00,'Total Cash':0}
while 1:
   print("wellcome to COFIIII")
   print("MENU:")
   cs={'Tea':25,'Black Coffee':5,'Coffee':35,'Green Tea':30,'Cappuccino':60}
   for i in cs.keys():
      print(i,"-",cs[i])
   n=input("enter your choice:")
   if n=='report':
      coffee(n,na,itms)
   else:
      a5=int(input("how many 5 Rupee coins(only 5 Rupee coin accepted):"))
      a10=int(input("how many 10 Rupee notes:"))
      a20=int(input("how many 20 Rupee notes:"))
      a100=int(input("how many 100 Rupee notes:"))
      a200=int(input("how many 200 Rupee notes:"))
      a500=int(input("how many 500 Rupee notes:"))
      if n in cs.keys():
         na=cs[n]
         checker(n,na,a5,a10,a20,a100,a200,a500)
         coffee(n,na,itms)
