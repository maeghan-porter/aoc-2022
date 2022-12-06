#!/usr/bin/env python3
with open('./input.txt', 'r') as f:
  for line in f.readlines():
    chars = list(line.strip())
    marker_found = False
    for i in range(14, len(chars)):
      check = chars[0:i][-14:]
      marker_found = len(set(check)) == len(check)
      if marker_found:
        print(i)
        break