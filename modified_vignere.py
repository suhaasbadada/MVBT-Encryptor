import sys

def intersecting_text(p,k):
    it=""
    for i in range(len(p)):
        c1=ord(p[i])
        c2=ord(k[i])

        val=c1-33+c2

        if(val>126):
            val-=94
        
        
        it+=chr(val)

    return it
    
def final_intersecting_text(itrm,k):
    fit=""

    for i in range(len(itrm)):
        c1=ord(itrm[i])
        c2=ord(k[i])

        val=c1+33-c2

        if(val>=126):
            val-=94
        if(val<=33):
            val+=94       
        
        fit+=chr(val)

    return fit

def singleDigSum(n):
    sum = 0
    while(n > 0 or sum > 9):
     
        if(n == 0):
            n = sum
            sum = 0
         
        sum += n % 10
        n //= 10
     
    return sum

def rotate_by(s):
    min_ascii=sys.maxsize*2+1

    for i in s:
        min_ascii=min(min_ascii,ord(i))
    return singleDigSum(min_ascii)

def left_rotate(it,n):
    arr=[]
    for i in it:
        arr.append(i)
   

    for i in range(0,n): 
        
        first=arr[0]  
        for j in range(0,len(it)-1): 
            arr[j]=arr[j+1];  
        arr[len(it)-1] = first; 

    z=""
    for i in arr:
        z+=i
    
    return z

def right_rotate(it,n):
    arr=[]
    for i in it:
        arr.append(i)

    for i in range(0,n): 
        
        last=arr[len(it)-1]  
        for j in range(len(arr)-1, -1, -1): 
            arr[j]=arr[j-1];  
        arr[0] = last 
    
    z=""
    for i in arr:
        z+=i
    
    return z


def mvencrypt(p,k):
    it=intersecting_text(p,k)
    rb=rotate_by(it)

    cipher_text=left_rotate(it,rb)

    return cipher_text


def mvdecrypt(cipher_text,k):
    rb=rotate_by(cipher_text)
    intermediate=right_rotate(cipher_text,rb)

    plaintext=final_intersecting_text(intermediate,k)

    return plaintext

 