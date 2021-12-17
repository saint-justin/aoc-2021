import numpy as np
import pathlib
path = f'{pathlib.Path().resolve()}/aoc-2021/Day3'

def dec_from_bin(arr):
  sum = 0
  current = 1
  for i in range(len(arr)-1, -1, -1):
    sum += (current) * arr[i]
    current *= 2
  return sum

arr = []
entries = np.array([line.strip() for line in open(f'{path}/input_test.txt')])
adjusted = np.array([[int(ch) * 2 - 1 for ch in num] for num in entries])
accumulated = np.ones(adjusted.shape[1])
for item in adjusted:
  accumulated = accumulated + item

out_normal = dec_from_bin([1 if num >= 1 else 0 for num in accumulated])
out_inverted = dec_from_bin([0 if num >= 1 else 1 for num in accumulated])
print(f'normal: {out_normal}   inverted: {out_inverted}   solution: {out_normal * out_inverted}')





# def get_value_difference_at_index(arr, i):
#   diff = 0
#   for item in arr: 
#     diff += 1 if item[i] == '1' else -1
#   return diff
# i = 0
# while len(entries) > 1 and i < 10:
#   most_common_at_index = '0' if get_value_difference_at_index(entries, i) >= 1 else '1'
#   entries = entries[np.where(entries[i] == most_common_at_index)]
#   i += 1
#   print(f'\nRound {i}:')
#   print(entries)
