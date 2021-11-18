import collections
from modified_vignere import mvencrypt,mvdecrypt
import time



class newNode():
 
    def __init__(self, data):
        self.key = data
        self.left = None
        self.right = None
         

def inorder(temp):
  
    if (not temp):
        return
 
    inorder(temp.left)
    print(temp.key,end = " ")
    inorder(temp.right)
 

def insert(temp,key):
 
    if not temp:
        root = newNode(key)
        return
    q = []
    q.append(temp)

    while (len(q)):
        temp = q[0]
        q.pop(0)
 
        if (not temp.left):
            temp.left = newNode(key)
            break
        else:
            q.append(temp.left)
 
        if (not temp.right):
            temp.right = newNode(key)
            break
        else:
            q.append(temp.right)

def levelOrderTraversal(root):
    ans = ""
 
    if root is None:
        return ans
    
    queue = collections.deque()
    queue.append(root)

    while queue:
        currSize = len(queue)
        #currList = ""
 
        while currSize > 0:
            currNode = queue.popleft()
            ans+=(currNode.key)
            #currList+=(currNode.key)
            currSize -= 1   

            if currNode.left is not None:
                queue.append(currNode.left)

            if currNode.right is not None:
                queue.append(currNode.right)       
        

    return ans


def mirror(root):
      if root:
          mirror(root.left)
          mirror(root.right)
          root.left, root.right = root.right, root.left

def printLevelOrder(root):
    h = height(root)
    for i in range(1, h+1):
        printCurrentLevel(root, i)
 
def printCurrentLevel(root, level):
    if root is None:
        return
    if level == 1:
        print(root.data, end=" ")
    elif level > 1:
        printCurrentLevel(root.left, level-1)
        printCurrentLevel(root.right, level-1)
 
def height(node):
    if node is None:
        return 0
    else:
        lheight = height(node.left)
        rheight = height(node.right)

        if lheight > rheight:
            return lheight+1
        else:
            return rheight+1
            
def decrypt(encrypt):
    root = newNode(encrypt[0])
    i = 1
    while(i<len(encrypt)):
        insert(root, encrypt[i])
        i+=1
    mirror(root)
    t=levelOrderTraversal(root)
    decrypted=""
    for i in range(len(t)):
        pos=i+1
        ascii=ord(t[i])
        if(pos%2 == 0):
            ascii = ascii - i

        else:
                ascii = ascii - i - 2
        decrypted += chr(ascii)
    
    return decrypted

def vigenereKey(string,key):
    i=0
    n=len(key)
    while(len(string)!=len(key)):
      key+=key[i]
      i=(i+1)%n 
    return key

def getVigKey(string,keyword):
    global start_time
    start_time=time.time()
    return vigenereKey(string, keyword)


def dec1(string,keyword):

    cipher_text = mvencrypt(string,keyword)
   
    s=cipher_text
    arr=[]

    for i in range(len(s)):
        ascii=ord(s[i])
        arr.append(ascii)
    temp = arr[len(s)-1]
    for i in range(0,len(s)-1,2):
        arr[i]+=i+2
        arr[i+1]+=i+1
    if len(s)%2!=0:
        arr[len(s)-1]=temp+len(s)+1

   
    b=""
    for i in range(len(s)):
        b+=chr(arr[i])
    
    
    root = newNode(b[0])

   
    i = 1
    while(i<len(arr)):
        insert(root, b[i])
        i+=1
    
    mirror(root)
    
    p=levelOrderTraversal(root)

    return (p)   

def dec2(p):
    return decrypt(p)

def dec3(d,k):
    return mvdecrypt(d,k)
    
def execution_time():
    t=(time.time()-start_time)
    formatted = '{0:.3g}'. format(t)
    s1=str(formatted)
    s2=" seconds"
    return s1+s2
