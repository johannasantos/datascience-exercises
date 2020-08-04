"""### 3.2 Playing with the odds
A guy is surrounded by a huge crowd. He has a bag full of coins and is claiming: "There are 1000 coins and only 1 have either two heads or two tails, and I will pay one million dollars to the person that finds it". However, there is a condition: "You can only see one face of the coin, but you can flip it as many times as you want. However, every time you throw it you lose 100.000 dollars from the prize."
You, as a data scientist, know that there is a statistical approach to calculate the odds. So you took a coin and start to flip it. 
__What are the probabilities of have grabbed the two-faced coin if at each trial (out of 20) it landed the same face? When would you consider stop flipping it and why?__
Take into account that N=0 means having no observation at all.
Note: the output must have 3 decimals points.
"""

# Solve this problem here

'''
You have to flip the coin less than 10 times because if you flip it 10 times, 
you wouldn't receive any money. The probability of fliping 9 times, 
that the same face comes out and that this will be the correct coin is approximately
0.339 (which is a low chance), but it's the highest probability that can be 
obtained to get some money.
'''
def calculate_proba(flips):
  proba_lucky_coin_and_flip_20 = 1/1000 * 1
  
  proba_lucky_coin = 1/1000
  proba_20_dado_lucky_coin = 1

  proba_bad_coin = 999/1000
  proba_lucky_flip_dado_bad_coin = (1/2)**flips

  proba_total = proba_lucky_coin * proba_20_dado_lucky_coin + proba_bad_coin * proba_lucky_flip_dado_bad_coin

  conditional_proba = proba_lucky_coin_and_flip_20 / proba_total
  return round(conditional_proba, 3)

print(calculate_proba(9))