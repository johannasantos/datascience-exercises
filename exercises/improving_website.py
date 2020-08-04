""" III. Statistics
 3.1 Improving a website
A coworker performed an A/B test to improve the revenue of your company's website. He created two different flows and registered the amount of money that each customer expended.
The test is finished and your colleague uploaded all the data to a spreadsheet.
He asked you to analyze the data and help him to decide whether the alternative configuration is better than control. Also, since this is going to be presented at the management, you need to find a way to explain and show (justifying from the data) how this change could potentially impact company revenue.
Some notes about how data was collected:
- Users were randomly assigned to each config from the minute they entered the website.
- It is a representative sample.
- All the variables were properly controlled.
"""

# Solve this problem here

'''
Due to the fact that the data was randomly assigned to each config from the 
minute they entered the website, it is a representative sample and all 
the variables were properly controlled, we can conclude that it is convenient 
to choose group B since it will bring higher profits and benefits.
As you can see in the graph the amount spent by group B is greater than the 
amount spent by group A.
'''

import requests
import matplotlib.pyplot as plt


def dataframe_creator(url):
    response = requests.get(url)
    open('ab_testing.csv', 'wb').write(response.content)

    amount_a = 0.0
    amount_b = 0.0

    with open('ab_testing.csv') as f:
      for line in f.readlines():
        elements = line.strip().split(',')
        if elements[1] == 'A':
          amount_a += float(elements[2])
        elif elements[1] == 'B':
          amount_b += float(elements[2])

    data = [amount_a, amount_b]
    plt.bar(['group A', 'group B'], data)
    plt.show()    

dataframe_creator("https://www.dropbox.com/s/1a5ss6oknp93bku/ab_website.csv?dl=1")