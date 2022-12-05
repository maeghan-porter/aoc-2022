#!/usr/bin/env python3

tracker = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', \
  'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', \
  'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', \
  'U', 'V', 'W', 'X', 'Y', 'Z']
total = 0
with open('./part1-input.txt', 'r') as f:
  for line in f.readlines():
    items = list(line.strip())
    size = len(items)//2
    compartment1 = items[0:size]
    compartment2 = items[size:]
    for val in compartment1:
      if val in compartment2:
        total += int(tracker.index(val))+1
        break
  print(total)

total = 0
with open('./part2-input.txt', 'r') as f:
  input = f.read().split()
  marker = 0
  while(marker+3 <= len(input)):
    group = input[marker: marker+3]
    marker += 3
    for val in group[0]:
      if val in group[1] and val in group[2]:
        total += int(tracker.index(val))+1
        break
print(total)