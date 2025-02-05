sum=pos=neg=0
nb=input("enter a nb 0 to exit")
try :
    nb=int(nb)
    while nb!=0:
      if nb>0:
       pos+=1
      else :
       neg+=1
     
       try :
        
        nb=input("enter a nb 0 to exit")
        nb=int(nb)
        
       
      
     
       except ValueError:
         print("hh")
        
except ValueError:
    print("ss")
print("sum",sum)
print("nb of neg",neg)
print("nb of pos",pos)
    