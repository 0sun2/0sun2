#7.11
M = 13                 
table = [None]*M       
def hashFn(key) :    
    return key% M

#7.12
def insert(key) :
    i = hashFn(key)
    count = M
    while count>0 :
        if table[i] == None or table[i] == -1 :
            break              
        i = (i + 1) % M      
        count -= 1
    if count > 0 :             
        table[i] = key

#7.13
def search(key) :
    i = hashFn(key)
    count = M
    while count>0 :
        if table[i] == None :   
            return None
        if table[i] == key :  
            return table[i]
        i = (i + 1) % M
        count -= 1

    return None              

#7.14
def delete(key) :
    i = hashFn(key)
    count = M
    while count>0 :
        if table[i] == key :   
            table[i] = -1
            return
        if table[i] == None :   
            return
        i = (i + 1) % M
        count -= 1