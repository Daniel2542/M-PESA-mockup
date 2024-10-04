import random
from getpass import getpass
import random
from datetime import datetime

def code_generator():
  code = ""
  chars_8 = []
  chars = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M" "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2" "3", "4", "5","6","7", "8", "9"]
  for i in range(8):
    character = random.choice(chars)
    chars_8.append(character)
  for j in chars_8:
    code += j
  code = f"SI{code}"
  return code


def get_pin(my_pin):
  pin = getpass(prompt="Enter pin: ")
  if pin == my_pin:
     return True
  else:
     print("Transaction failed. You have entered wrong pin")
     return False

def get_timestamp():
  current_timestamp = datetime.now()
  return current_timestamp

def prom_message():
  msgs = ["Sign up for Lipa na Mpesa Till online", "Download new Mpesa app & get 500mb free data", "Buy airtime for 1 bob via Mpesa today", "Separate personal funds through pochi la biashara on *334#", "Register for overdraw services via *234*1*9#"]
  for i in range(1):
    message = random.choice(msgs)
    return message


def mpesa():
    balance = 20000
    airtime_balance = 0
    mshwari_balance = 1000
    mshwari_loan_limit = 1000
    mshwari_loan_amount = 0
    my_pin = "1234"

    for transaction in range(3):
      main_option = input("Choose an option: 1. Safaricom, 2. M-PESA : ")

      if main_option == "1":

          safaricom_option = input("Choose an option: 1. MyAccount, 2. M-banking services : ")

          if safaricom_option == "1":
            account_option = input("Choose an option: 1. Balance inquiry, 2. Top-up, 3. Selfcare, 4. Customer-care : ")
            if account_option == "1":
              print(f"Your airtime balance is kshs {airtime_balance}")
            elif account_option == "2":
              print("b. Top-up")
            elif account_option == "3":
              print("c. Selfcare")
            elif account_option == "4":
              print("d. Customer-care")

          elif safaricom_option == "2":

              mbanking_option = input("Choose an option: 1. Barclays bank, 2. Coop bank, 3. Dtb, 4. Ecobank, 5. Equity, 6. Family, 7. I&M : ")
              if mbanking_option == "1":
                print("Barclays bank")
              elif mbanking_option == "2":
                print("Coop bank")
              elif mbanking_option == "3":
                print("Dtb")
              elif mbanking_option == "4":
                print("Ecobank")
              elif mbanking_option == "5":
                print("Equity")
              elif mbanking_option == "6":
                print("Family")
              elif mbanking_option == "7":
                print("I&M")

      elif main_option =="2":

          mpesa_option = input("Choose an option: 1. Send money, 2. Withdraw cash, 3. Buy airtime, 4. Loans and savings, 5. Lipa na Mpesa,  6. My account : ")

          if  mpesa_option == "1":
              phone_number = input("Enter Phone number: ")
              amount = int(input("Enter amount: "))
              # pin = get_pin(my_pin)
              if get_pin(my_pin):
                balance -= amount
                code = code_generator()
                now = get_timestamp()
                prom_msg = prom_message()

                message = print(f"{code} Confirmed you have sent kshs {amount} at {now} to Merali {phone_number}. New Mpesa balance is kshs {balance}.{prom_msg}.")

          elif mpesa_option == "2":

              withdraw_option = input("Choose an option: 1. From agent, 2. From ATM : ")

              if withdraw_option == "1":
                  agent_number = input("Enter agent number: ")
                  store_number = input("Enter store number: ")
                  amount = int(input("Enter amount: "))
                  if get_pin(my_pin):
                    balance -= amount
                    code = code_generator()
                    now = get_timestamp()
                    prom_msg = prom_message()
                    message = print(f"{code} Confirmed you have withdrawn kshs {amount} at {now} at Westi shop {agent_number}. New Mpesa balance is kshs {balance}. {prom_msg}.")


              elif withdraw_option == "2":
                  agent_number = input("Enter agent number: ")
                  amount = int(input("Enter amount: "))
                  if get_pin(my_pin):
                    balance -= amount
                    code = code_generator()
                    now = get_timestamp()
                    prom_msg = prom_message()
                    message = print(f"{code} Confirmed you have withdrawn kshs {amount} at {now} at Westi shop {agent_number}. New Mpesa balance is kshs {balance}. {prom_msg}.")

          elif mpesa_option == "3":

              airtime_option = input("Choose an option: 1. My phone, 2. Other phone : ")

              if airtime_option == "1":
                  amount = int(input("Enter amount: "))
                  if get_pin(my_pin):
                    balance -= amount
                    airtime_balance += amount
                    code = code_generator()
                    now = get_timestamp()
                    prom_msg = prom_message()
                    message = print(f"{code} Confirmed you have bought airtime kshs {amount} at {now}. New Mpesa balance is kshs {balance}. {prom_msg}.")

              elif airtime_option == "2":
                  phone_number = input("Enter phone number: ")
                  amount = int(input("Enter amount: "))
                  if get_pin(my_pin):
                    balance -= amount
                    code = code_generator()
                    now = get_timestamp()
                    prom_msg = prom_message()
                    message = print(f"{code} Confirmed you have bought airtime kshs {amount} for Merali {phone_number} at {now} . New Mpesa balance is kshs {balance}. {prom_msg}.")

          elif mpesa_option == "4":

              loans_option = input("Choose an option: 1. Mshwari, 2. KCB M-Pesa : ")

              if loans_option == "1":
                
                mshwari_option = input("Choose an option: 1. Send to Mshwari, 2. Withdraw to M-Pesa, 3. Lock savings account, 4. Loan @ 9% for 30 days, 5. Fixed savings account, 6. Check balance : ")

                if mshwari_option == "1":
                  amount = int(input("Enter amount: "))
                  if get_pin(my_pin):
                    balance -= amount
                    mshwari_balance += amount
                    code = code_generator()
                    now = get_timestamp()
                    prom_msg = prom_message()
                    print(f"{code} Confirmed you have deposited kshs {amount} to your mshwari account at {now}. New mshwari balance is kshs {mshwari_balance}. Your mpesa balance is {balance}. {prom_msg}")
                
                elif mshwari_option == "2":
                  amount = int(input("Enter amount to withdraw: "))
                  if get_pin(my_pin):
                    balance += amount
                    mshwari_balance -= amount
                    code = code_generator()
                    now = get_timestamp()
                    prom_msg = prom_message()
                    print(f"{code} Confirmed you have withdrawn kshs {amount} from your mshwari account at {now}. New mshwari balance is kshs {mshwari_balance}. Your mpesa balance is {balance}. {prom_msg}")

                  print("Withdraw to M-Pesa")

                elif mshwari_option == "3":
                  print("Lock savings account")

                elif mshwari_option == "4":
                  mshwari_loan_options = input("Enter your option: 1. Request loan, 2. Pay loan, 3.Check loan limit, 4.Loan balance")

                  if mshwari_loan_options == "1":
                    loan_amount = int(input("Enter loan amount: "))
                    if get_pin(my_pin):
                      if loan_amount <= mshwari_loan_limit:
                        mshwari_loan_amount += loan_amount                  
                        mshwari_balance += loan_amount
                        mshwari_loan_limit -= loan_amount
                        now = get_timestamp()
                        code = code_generator()
                        prom_msg = prom_message()
                        print(f"{code} Confirmed you have received a loan of kshs {loan_amount} at {now}. New mshwari balance is kshs {mshwari_balance}. {prom_msg}")
                      else:
                        print("You don't qualify for a loan") 
                    else:
                      print("You have entered wrong pin")      

                  elif mshwari_loan_options == "2":
                    pay_mshwari_loan_options = input("Enter your option: 1. Pay via Mpesa, 2. Pay via Mshwari")

                    if pay_mshwari_loan_options == "1":
                      mshwari_payment = int(input("Enter amount to pay: "))
                      if get_pin(my_pin):
                        balance -= mshwari_payment
                        mshwari_loan_limit += mshwari_payment
                        mshwari_loan_amount -= mshwari_payment
                        now = get_timestamp()
                        code = code_generator()
                        prom_msg = prom_message()

                        print(f"{code} Confirmed you have paid you have paid ksh {mshwari_payment} via mpesa for loan amount of kshs {loan_amount} at {now}. Your mshwari loan balance is kshs {mshwari_loan_amount}. ")




                    elif pay_mshwari_loan_options == "2":
                      pass    
                    


                  elif mshwari_loan_options == "3":
                    print(f"Your mshwari loan limit is kshs {mshwari_loan_limit}")
                  elif mshwari_loan_options == "4":
                    print("Loan balance")


                elif mshwari_option == "5":
                  print("Fixed savings account")
                elif mshwari_option == "6":
                  prom_msg = prom_message()
                  print(f"Your mshwari balance is kshs {mshwari_balance}. {prom_msg}")

              elif loans_option == "2":

                kcb_option = input("Choose option: 1.deposit from mpesa, 2. withdraw from mpesa, 3.loan @ 8.93% for 30 days, 4.fixed savings account, 5.my account : ")

                if kcb_option == "1":
                  print("Send to Mshwari")
                elif kcb_option == "2":
                  print("Withdraw to M-Pesa")
                elif kcb_option == "3":
                  print("Lock savings account")
                elif kcb_option == "4":
                  print("Loan @ 8.93% for 30 days")
                elif kcb_option == "5":
                  print("Fixed savings account")
                elif kcb_option == "6":
                  print("My account")

          elif mpesa_option == "5":

            lipa_option = input("Choose option: 1. Paybill, 2. Buy goods and services, 3. Pochi la biashara : ")

            if lipa_option == "1":
              paybill_no = input("Enter Paybill number: ")
              acc_no = input("Enter Account number: ")
              amount = int(input("Enter amount: "))
              # pin = get_pin(my_pin)
              if get_pin(my_pin):
                balance -= amount
                code = code_generator()
                now = get_timestamp()
                prom_msg = prom_message()
                message = print(f"{code} Confirmed you have sent kshs {amount} at {now} to Merali, paybill number {paybill_no}. New Mpesa balance is kshs {balance}. {prom_msg}.")

            elif lipa_option == "2":
              till_no = input("Enter Till number: ")
              amount = int(input("Enter amount: "))
              # pin = get_pin(my_pin)
              if get_pin(my_pin):
                balance -= amount
                code = code_generator()
                now = get_timestamp()
                prom_msg = prom_message()
                message = print(f"{code} Confirmed you have sent kshs {amount} at {now} to Merali, Till number {till_no}. New Mpesa balance is kshs {balance}. {prom_msg}.")

            elif lipa_option == "3":
              phone_no = input("Enter Phone number: ")
              amount = int(input("Enter amount: "))
              # pin = get_pin(my_pin)
              if get_pin(my_pin):
                balance -= amount
                code = code_generator()
                now = get_timestamp()
                prom_msg = prom_message()
                message = print(f"{code} Confirmed you have sent kshs {amount} at {now} to Merali, phone number {phone_no}. New Mpesa balance is kshs {balance}. {prom_msg}.")

          elif mpesa_option == "6":

            myaccount_option = (input("Choose option: 1. Mini statement, 2. Mpesa pin manager, 3. Change language, 4. Update customer, 5. Check balance "))

            if myaccount_option == "1":
              print("1. Mini statement")

            elif myaccount_option == "2":
              old_pin = getpass(prompt="Enter your old PIN: ")
              if old_pin == my_pin:
                new_pin = getpass(prompt="Enter your new PIN: ")
                new_pin_confirmation = getpass(prompt="Enter your new PIN again: ")
                if new_pin == new_pin_confirmation:
                  my_pin = new_pin
                else:
                  print("The PINS do not match")
              else:
                print("You have entered wrong pin")

            elif myaccount_option == "3":
              print("3. Change language")
            elif myaccount_option == "4":
              print("4. Update customer")
            elif myaccount_option == "5":
              print(balance)
              

mpesa()
