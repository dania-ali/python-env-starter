my_list = [20,56,43,20,45,56,20,10,54,100]


def remove_duplicates(list):
  new_list = []

  for item in list:
    if item not in new_list:
      new_list.append(item)
  return new_list

print(f'Original List: {my_list}')
list1 = remove_duplicates(my_list)
print(f'New List: {list1}')

def max_finder(list):
  max_num = 0
  max_num = max(list)
  return max_num


def min_finder(list):
  min_num = 0
  min_num = min(list)
  return min_num
