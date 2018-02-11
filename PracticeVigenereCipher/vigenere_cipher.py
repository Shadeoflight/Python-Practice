
from cipher_map import conversion_table, character_table

def encrypt(plaintext, key):
  
  plaintext_int_arr = [conversion_table[i] for i in plaintext]
  
  key_int_arr = [conversion_table[i] for i in key]
  
  ciphertext = ''
  
  k = 0
  for i in range(len(plaintext_int_arr)):
    
    if k == len(key_int_arr):
      k = 0
    
    shifted_int = (int(plaintext_int_arr[i]) + int(key_int_arr[k])) % 26
    
    if shifted_int == 0:
      shifted_int = 26
      
    ciphertext = ciphertext + character_table[int(shifted_int)]
    
    k = k+1
  
  return ciphertext

# For testing purposes
def decrypt(ciphertext, key):
  
  ciphertext_int_arr = [conversion_table[i] for i in ciphertext]
  
  key_int_arr = [conversion_table[i] for i in key]
  
  plaintext = ''
  
  k = 0
  for i in range(len(ciphertext_int_arr)):
    
    #print str(ciphertext_int_arr[i])
    if k == len(key_int_arr):
      k = 0
    #print " :: " + str(key_int_arr[k])
    
    reverse_shifted_int = (int(ciphertext_int_arr[i]) - int(key_int_arr[k])) % 26
    #print reverse_shifted_int
    # Map values start at 1
    if reverse_shifted_int == 0:
      reverse_shifted_int = 26
      
    plaintext = plaintext + character_table[int(reverse_shifted_int)]
    
    k = k+1
    
  return plaintext