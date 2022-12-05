#!/usr/bin/env python3

part1_total = 0
part2_total = 0
with open('./input.txt', 'r') as f:
  for pair in f.readlines():
    input = pair.strip().split(',')
    elf1 = [int(v) for v in input[0].split('-')]
    elf2 = [int(v) for v in input[1].split('-')]
    if (elf1[0] <= elf2[0] and elf1[1] >= elf2[1]) or \
      (elf1[0] >= elf2[0] and elf1[1] <= elf2[1]):
      part1_total += 1

    if elf1[0] <= elf2[0] and elf1[0] >= elf2[1]:
      # 1st elf's starting value is in the middle the 2nd elf's range
      part2_total +=1
    elif elf2[0] >= elf1[0] and elf2[0] <= elf1[1]:
      # 2nd elf's starting value is in the middle the 1st elf's range
      part2_total +=1
    elif elf1[1] >= elf2[0] and elf1[1] <= elf2[1]:
      # 1st elf's ending value is in the middle the 2nd elf's range
      part2_total +=1
    elif elf2[1] >= elf1[0] and elf2[1] <= elf1[1]:
      # 1st elf's ending value is in the middle the 2nd elf's range
      part2_total +=1
print(part2_total)