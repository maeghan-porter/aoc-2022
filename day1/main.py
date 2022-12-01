#!/usr/bin/env python3
with open("./input.txt", "r") as f:
  input = f.read()
  elves = []
  total = 0
  for line in input.split("\n"):
    try:
      total += int(line)
    except Exception as e:
      # Done with this elf.
      elves.append(total)
      total = 0
     
elves.sort(reverse=True)
print("Part 1: %d"%elves[0])
print("Part 2: %d"%sum(elves[0:3]))