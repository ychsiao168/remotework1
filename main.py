#!/usr/bin/env python
# -*- coding: utf-8 -*-

from aapl_history import *

if __name__ == '__main__':
  apple = AaplHistory('2021/09/05', '2021/09/22')
  json_arr = apple.get_json()

  for day in json_arr:
    print(day)
