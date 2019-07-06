# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

# Core modules
import datetime
from datetime import date
from time import time

# Pip module
from camelcase import CamelCase

# Custome module
import validator

# today=datetime.date.today()
today = date.today()

timestamp = time()

camel = CamelCase()
text = 'hello there world'
print(camel.hump(text))

email = "test@test.com"
if validator.validate_email(email):
    print('Email is valid')
else:
    print('Not an email')
