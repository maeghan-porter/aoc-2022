#!/usr/bin/env python3

def part1():
  point_map = {
    'X': 1,
    'Y': 2,
    'Z': 3
  }
  vals_lookup = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors'
  }
  total_score = 0
  with open('./input.txt', 'r') as f:
    round_score = 0
    for game in f.readlines():
      opp = game.split(' ')[0]
      me = game.split(' ')[1].strip()
      round_score += point_map[me]
      if vals_lookup[opp] == vals_lookup[me]:
        round_score += 3
      elif vals_lookup[opp] == 'rock' and vals_lookup[me] == 'paper' or \
        vals_lookup[opp] == 'paper' and vals_lookup[me] == 'scissors' or \
        vals_lookup[opp] == 'scissors' and vals_lookup[me] == 'rock':
        round_score += 6
      total_score += round_score
      round_score = 0
  print(total_score)

def win(opp_val):
  match opp_val:
    case 'A':
      return 'paper'
    case 'B':
      return 'scissors'
    case _:
      return 'rock'

def lose(opp_val):
  match opp_val:
    case 'A':
      return 'scissors'
    case 'B':
      return 'rock'
    case _:
      return 'paper'

def part2():
  point_map = {
    'A': 1,
    'B': 2,
    'C': 3,
    'rock': 1,
    'paper': 2,
    'scissors': 3
  }
  total_score = 0
  with open('./input.txt', 'r') as f:
    round_score = 0
    for game in f.readlines():
      opp = game.split(' ')[0]
      me = game.split(' ')[1].strip()
      match me:
        case 'X':
          round_score += point_map[lose(opp)]
        case 'Y':
          round_score += (3 + point_map[opp])
        case _:
          round_score += (6 + point_map[win(opp)])
      total_score += round_score
      round_score = 0
    print(total_score)
part2()
part2()