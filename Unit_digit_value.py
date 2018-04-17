'''
unit place values
By mbonea mjema
'''
Numbers={}
#importing prettyprint
import pprint
pp=pprint.PrettyPrinter(indent=4)


for num in range(10):
    container=[]
    temp_list=[]
    for i in  range (1,10,1):
        unit_place_value=(num**i)%10
        if(not unit_place_value in temp_list):
            temp_list.append(unit_place_value)
            container.append((i,unit_place_value))
        else:
            break
    Numbers[num]=container
pp.pprint(Numbers)
        
