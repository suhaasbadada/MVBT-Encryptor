def caesar_encrypt(s,k):
	k=int(k)
	z=''
	for i in s:
		if i.isupper():
			z+=chr((ord(i)+k-65)%26+65)                
		else:
			z+=chr((ord(i)+k-97)%26+97)    
	result=z

	return result 

def caesar_decrypt(s,k):
	k=int(k)
	z=''
	for i in s:
		if i.isupper():
			z+=chr((ord(i)-k-65)%26+65)                
		else:
			z+=chr((ord(i)-k-97)%26+97)     
	result=z
	
	return result










# def caesar_encrypt(word,k):
#     c = ''
#     for i in word:
#         if (i == ' '):
#             c += ' '
#         else:
#             c += (chr(ord(i) + k))
#     return c

# def caesar_decrypt(word,k):
#     c = ''
#     for i in word:
#         if (i == ' '):
#             c += ' '
#         else:
#             c += (chr(ord(i) - k))
#     return c
  
