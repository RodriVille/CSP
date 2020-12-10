# a213_pw_analyzer.py
import time
import a213_pwalgorithms_RVV as pwa

password = input("Enter password:")
num = input("last two digits on ID: ")

print("Analyzing a one-word password ...")
time_start = time.time()

# attempt to find password
found, num_guesses = pwa.two_word(password, num)
time_end = time.time()

# report results
if (found):
  print(password, "found in", num_guesses, "guesses")
else: 
  print(password, "NOT found in", num_guesses, "guesses!")
print("Time:", format((time_end-time_start), ".8f"))