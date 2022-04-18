from string import digits, punctuation, ascii_letters
import itertools
import win32com.client as client
from datetime import datatime
import time

#symbols = digits + punctuation + ascii_letters
#print(symbols)

def brute_excel_doc():
  print('***Hello bro!***')
  
  try:
    password_length = input("Lengths password, for exampel 3 - 7: ")
    password_length = [int(item) for item in password_length.split("-")]
    
  except:
    print("error")
    
  print('1. If in password only numbers enter 1\n2. If in password only letters enter 2\n3. If in password letters and numbers enter 3\n4. If in password numbers, letters and special characters enter 4\n')
  
  try:
    choice = int(input(": "))
    if choice == 1:
      possible_symbols = digits
    elif choice == 2:
      possible_symbols = ascii_letters
    elif choice == 3:
      possible_symbols = digits + ascii_letters
    elif choice == 4:
      possible_symbols = digits + ascii_letters + punctuation
      
  except:
    print('error')
  
  start_timestap = time.time()
  print(f"Started at - {datetime.utcfromtimestamp(time.time()).strftime('%H:%M:%S')}")
  count = 0
  for pass_length in range(password_length[0], password_length[1] + 1):
    for password in itertools.product(possible_symbols, repeat=password_length):
      password = "".join(password)
      #print(password)
      
      opened_doc = client.Dispatch("Excel.Application")
      count += 1 
      
      try:
        opened_doc.Workbooks.Open(
          r"путь",
          False,
          True,
          None,
          password
        )
        time.sleep(0.1)
        print(f'Finished at - {datetime.utcfromtimestamp(time.time()).strftime('%H:%M:%S')}}')
        print(f"Password cracking time - {time.time() - start_timestap}")
        
        return f"Attempt #{count} Password is {password}"
      except:
        print('Attempt #{count} Inctorrect is {password}')

def main():
  brute_excel_doc()
  
if __name__ == "__main__":
  main()
