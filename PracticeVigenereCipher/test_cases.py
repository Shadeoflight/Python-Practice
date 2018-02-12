
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

  # Print to file
  text_file_name = str(1) + "-" + "data-output.txt"
  text_file = open(text_file_name, "w")
  #
  
  start = time.time()
  ciphertextA = "MSOKKJCOSXOEEKDTOSLGFWCMCHSUSGX"
  key_cracker(ciphertextA, 2, 6, content)
  end = time.time()
  print "---------------------"
  print "Trial 1"
  print "---------------------"
  print(end - start)
  print "---------------------"
  
  # Print to file
  text_file.write("Resulting data: %s" % str(end-start))
  text_file.close()
  #
  
  # Print to file
  text_file_name = str(2) + "-" + "data-output.txt"
  text_file = open(text_file_name, "w")
  #

  start = time.time()
  ciphertextB = "OOPCULNWFRCFQAQJGPNARMEYUODYOUNRGWORQEPVARCEPBBSCEQYEARAJUYGWWYACYWBPRNEJBMDTEAEYCCFJNENSGWAQRTSJTGXNRQRMDGFEEPHSJRGFCFMACCB"
  key_cracker(ciphertextB, 3, 7, content)
  end = time.time()
  print "---------------------"
  print "Trial 2"
  print "---------------------"
  print(end - start)
  print "---------------------"
  
  # Print to file
  text_file.write("Resulting data: %s" % str(end-start))
  text_file.close()
  #
  
  # Print to file
  text_file_name = str(3) + "-" + "data-output.txt"
  text_file = open(text_file_name, "w")
  #

  start = time.time()
  ciphertextC = "MTZHZEOQKASVBDOWMWMKMNYIIHVWPEXJA"
  key_cracker(ciphertextC, 4, 10, content)
  end = time.time()
  print "---------------------"
  print "Trial 3"
  print "---------------------"
  print(end - start)
  print "---------------------"
  
  # Print to file
  text_file.write("Resulting data: %s" % str(end-start))
  text_file.close()
  #
  
  # Print to file
  text_file_name = str(4) + "-" + "data-output.txt"
  text_file = open(text_file_name, "w")
  #

  start = time.time()
  ciphertextD = "HUETNMIXVTMQWZTQMMZUNZXNSSBLNSJVSJQDLKR"
  key_cracker(ciphertextD, 5, 11, content)
  end = time.time()
  print "---------------------"
  print "Trial 4"
  print "---------------------"
  print(end - start)
  print "---------------------"
  
  # Print to file
  text_file.write("Resulting data: %s" % str(end-start))
  text_file.close()
  #
  
  # Print to file
  text_file_name = str(5) + "-" + "data-output.txt"
  text_file = open(text_file_name, "w")
  #

  start = time.time()
  ciphertextE = "LDWMEKPOPSWNOAVBIDHIPCEWAETYRVOAUPSINOVDIEDHCDSELHCCPVHRPOHZUSERSFS"
  key_cracker(ciphertextE, 6, 9, content)
  end = time.time()
  print "---------------------"
  print "Trial 5"
  print "---------------------"
  print(end - start)
  print "---------------------"
  
  # Print to file
  text_file.write("Resulting data: %s" % str(end-start))
  text_file.close()
  #
  
test_cases()
  
  