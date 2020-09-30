import random
def primary():
   print("Keep it logically awesome.")

   f = open("quotes.txt")
   quotes = f.readlines()
   f.close()
   quotes_len = len(quotes)
   rand_quote = random.randint(0,quotes_len)

   print(quotes[rand_quote])

if __name__== "__main__":
  primary()
