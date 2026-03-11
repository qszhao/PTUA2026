#Creating dictionary from gal file where key is id of spatial unit and value is list of neighbour ids
dict1 = {}
with open("C:/Users/caras/PTUA2026/Lab07/Lab/Lab07-1.gal") as fp:

    for i, value in enumerate(fp):
        if i == 0 or i % 2 != 0:
            continue
        dict1[int(i/2)] = value.split()
        print(value)  
  

print(dict1)       

#Creating list of neighbour counts - how many neighbours does each id have? .append adds each iteration through the loop
counts = []
for key, value in dict1.items():
    counts.append(len(value))
    
print(counts)

#reduce to unique values - set() function does unordered
u_counts = set(counts)
print(u_counts)

for value in u_counts:
    print(value, counts.count(value))

dict2 = {}
for value in u_counts:
    dict2[value] = [key for key, v in dict1.items() if len(v) == value] 
    
    #says add the key from dict1 to dict2 where, in dict 1, (cont)
    #the length of list is same as value from u_counts - iterates through each item in list

print(dict2)
    
print(dict1)

for key in dict1:
    print(key, dict1[key])
    for neighbor in dict1[key]:
        print(key,' says ',neighbor, 'is a neighbor')
        if str(key) in dict1[int(neighbor)]:
            print('ok')
        else:
            print('not ok')
            print('because ', neighbor, ' says that ', key, 'is not a neighbor')
        
#Asymmetry found - 9 does not say that 21 is a neighbour, but 21 says 9 is a neighbour




