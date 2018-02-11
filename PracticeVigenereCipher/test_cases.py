
import time

from main_key_cracker import key_cracker

# List of dictionary elements
content = []

def test_cases():

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

  start = time.time()
  ciphertextA = "MSOKKJCOSXOEEKDTOSLGFWCMCHSUSGX"
  key_cracker(ciphertextA, 2, 6, content)
  end = time.time()
  print "---------------------"
  print "Trial 1"
  print "---------------------"
  print(end - start)
  print "---------------------"

  start = time.time()
  ciphertextB = "OOPCULNWFRCFQAQJGPNARMEYUODYOUNRGWORQEPVARCEPBBSCEQYEARAJUYGWWYACYWBPRNEJBMDTEAEYCCFJNENSGWAQRTSJTGXNRQRMDGFEEPHSJRGFCFMACCB"
  key_cracker(ciphertextB, 3, 7, content)
  end = time.time()
  print "---------------------"
  print "Trial 2"
  print "---------------------"
  print(end - start)
  print "---------------------"

  start = time.time()
  ciphertextC = "MTZHZEOQKASVBDOWMWMKMNYIIHVWPEXJA"
  key_cracker(ciphertextC, 4, 10, content)
  end = time.time()
  print "---------------------"
  print "Trial 3"
  print "---------------------"
  print(end - start)
  print "---------------------"

  start = time.time()
  ciphertextD = "HUETNMIXVTMQWZTQMMZUNZXNSSBLNSJVSJQDLKR"
  key_cracker(ciphertextD, 5, 11, content)
  end = time.time()
  print "---------------------"
  print "Trial 4"
  print "---------------------"
  print(end - start)
  print "---------------------"

  start = time.time()
  ciphertextE = "LDWMEKPOPSWNOAVBIDHIPCEWAETYRVOAUPSINOVDIEDHCDSELHCCPVHRPOHZUSERSFS"
  key_cracker(ciphertextE, 6, 9, content)
  end = time.time()
  print "---------------------"
  print "Trial 5"
  print "---------------------"
  print(end - start)
  print "---------------------"
  
test_cases()
  
  