#!/usr/bin/env python3

import datetime

Chanukah = datetime.date(2022, 12, 22, 17, 26, 0) - datetime.date.today()
print(Chanukah)

# Alt option below
# now = datetime.datetime.now()
# future = datetime.datetime(2022, 12, 22, 17, 26, 0)
# Chanukay = future - now
# print(Chanukah)
