'''
Did not figure out part 2 of this one :(
'''
#!/usr/bin/env python3
crate_arrangements = {
    1: ['D', 'H', 'N', 'Q', 'T', 'W', 'V', 'B'],
    2: ['D', 'W', 'B'],
    3: ['S', 'C', 'H', 'F', 'J'],
    4: ['T', 'R', 'M', 'W', 'N', 'G', 'B'],
    5: ['T', 'R', 'L', 'S', 'D', 'H', 'Q', 'B'],
    6: ['M', 'J', 'B', 'V', 'F', 'H', 'R', 'L'],
    7: ['D', 'W', 'R', 'N', 'J', 'M'],
    8: ['B', 'Z', 'T', 'F', 'H', 'N', 'D', 'J'],
    9: ['H', 'L', 'Q', 'N', 'B', 'F', 'T']
}

def flatten(l):
  return [item for sublist in l for item in sublist]

with open('./input.txt', 'r') as f:
  input = f.read()
  stacks = []
  crate_map = ""
  on_instructions = False
  stacks_reversed = False
  for line in input.split("\n"):
    num_crates_to_move, starting_crate, final_crate = [int(word) for word in str.split(line) if word.isdigit()]

    indexer = len(stacks[starting_crate - 1]) - num_crates_to_move # Get elements to remove from front of list.
  
    crate_to_append = stacks[starting_crate - 1][indexer:] # We make a separate crate with the contents we are moving.
  
    stacks[final_crate - 1].append(crate_to_append)
    stacks[final_crate - 1] = flatten(stacks[final_crate - 1])

    stacks[starting_crate - 1] = stacks[starting_crate - 1][:-num_crates_to_move] # Remove crates that have been moved from the memory of starting_crate.

  final_crate_values = list(stacks)
  answer_list = list()

  [answer_list.append(nested_list[-1:]) for nested_list in final_crate_values]

  answer = ('').join(flatten(answer_list)) # Flatten one final time and stringify.
  print(answer) # Turn off line 50 / crate_to_append.reverse() for part_2_answer.
#       if not stacks_reversed:
#         for i in range(0, len(stacks)):
#           stacks[i].reverse()
#         print(stacks)
#         stacks_reversed = True
#       print(line)
#       print(stacks)
#       vals = re.findall('[0-9]+', line)
#       starting_stack = stacks[int(vals[1])-1]
#       from_idx = len(starting_stack)-int(vals[0])
#       print(starting_stack)
#       crates = starting_stack[from_idx:]
#       print(crates)
#       stacks[int(vals[2])-1] = stacks[int(vals[2])-1] + crates
#       for val in crates:
#         stacks[int(vals[1])-1].remove(val)
#       print(stacks[int(vals[2])-1])
# for stack in stacks:
#   print(stack[-1], end='')