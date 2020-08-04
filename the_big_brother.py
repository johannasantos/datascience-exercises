# Function to download the data

def dataframe_creator(url, filename):

  import urllib.request
  import pandas as pd

  u = urllib.request.urlopen(url)
  data = u.read()
  u.close()

  with open(filename, "wb") as f :
      f.write(data)

  return pd.read_csv(filename)

"""## I. Basic Coding
### 1.1 The big brother
The office is preparing an identification system for its people. ___They ask you to find a way to create a function that can use the person's name to deliver an ID (str).___
Some specifications:
- It needs to include the first and last letter of the name (capitalized)
- Some DateTime-based coding must be added
- It must finish with a random alphanumeric label (5 characters) with at least one capped letter (randomly assigned)
Example: Lucas is Ls-110512062020-x3Mz3
"""

# Solve this problem here

from datetime import datetime
import random
import string


def ID_creator(name):
    if not name:
        raise Exception("Empty names are not allowed, sorry")
    # the first and last letter of the name (capitalized)
    first_letter = name[0].upper()
    last_letter = name[-1]

    # datetime object containing current date and time
    date_time = datetime.now()
    dt_string = date_time.strftime("%H%M%S%d%m%Y")

    # random alphanumeric label (5 characters) with at least one capped letter (randomly assigned)
    cap_letter = random.choice(string.ascii_letters).upper()
    alphanumeric_letters = string.ascii_letters + string.digits
    random_list = [random.choice(alphanumeric_letters) for i in range(5)]

    position = random.randint(0, 4)
    random_list[position] = cap_letter
    random_string = "".join(random_list)

    return first_letter + last_letter + "-" + dt_string + "-" + random_string


result_ID = ID_creator("johanna")

print(result_ID)
