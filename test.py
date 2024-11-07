from datetime import datetime

test = "December 13, 2016"
time = datetime.strptime(test, '%B %d, %Y')
print(type(time))