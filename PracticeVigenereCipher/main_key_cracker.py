
import vigenere_cipher
from vigenere_cipher import decrypt, encrypt

import itertools
from itertools import product

def main():
  file_name = ""
  ciphertext = ""
  key_length = 0
  
  content = []
  
  print "Vigenere encryption menu:"
  print "1: Encrypt"
  print "2: Decrypt"
  print "3: Dictionary Decrypt"
  print "4: Exit"
  choice_bool = int(raw_input('Option: '))
  
  # Exit program
  if choice_bool == 4:
    return
  
  if choice_bool == 1:
    
    plaintext_to_encrypt = str(raw_input('Enter text to encrypt: '))
    key_to_encrypt = str(raw_input('Enter the key for encryption: '))
    
    print "Encrypted text: " + encrypt(plaintext_to_encrypt, key_to_encrypt)
    
    return
  
  elif choice_bool == 2:
    
    ciphertext_to_decrypt = str(raw_input('Enter ciphertext to decrypt: '))
    key_to_decrypt = str(raw_input('Enter the key for decryption: '))
    
    print "Decrypted text: " + decrypt(ciphertext_to_decrypt, key_to_decrypt)
    
    return
  
  # Initialize file_name
  file_name = raw_input('Enter a dictionary file name: ')
  
  # Remove spaces of input
  try:
    with open(file_name, 'r') as f:
      content = f.readlines()
      # Remove whitespace characters like `\n` at the end of each line
      content = [x.strip() for x in content]
      
  except:
    print "Invalid file name!"
    return
  
  ciphertext = raw_input('Enter ciphertext: ')
  key_length = raw_input('Enter key length: ') # TODO: EDIT
  first_word_length = raw_input('Enter first word length: ')
  
  key_cracker(ciphertext, key_length, first_word_length, content)
  
  
def key_cracker(ciphertext, key_length, first_word_length, content):
  
  # Remove spaces from the string
  ciphertext.replace(" ", "")
  
  alphabet_arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  keywords = [''.join(i) for i in itertools.product(alphabet_arr, repeat = int(key_length))]
  
  # Print to file
  text_file_name = str(key_length) + "-" + str(first_word_length) + "output.txt"
  text_file = open(text_file_name, "w")
  #
  
  for i in range(len(keywords)):
    result_plaintext = decrypt(ciphertext, keywords[i]);
    
    result_first_substring = result_plaintext[:int(first_word_length)] # Get first substring
    
    # Read from dictionary
    for j in range(len(content)):
      
      if result_first_substring == content[j]:
        
        # Print to terminal
        
        #print "Resulting string: " + result_first_substring
        #print "Resulting key: " + keywords[i]
        #print "Resulting plaintext: " + result_plaintext
        
        #
        
        # Print to file
        text_file.write("Resulting string: %s" % result_first_substring)
        text_file.write("Resulting key: %s" % keywords[i])
        text_file.write("Resulting plaintext: %s" % result_plaintext)
        #
        
        break
    
  #print "LENGTH: " + str(len(content))
  
  # Print to file
  text_file.close()
  #
  
# UNCOMMENT TO RUN BASIC CRYPTO SUITE
#main()

