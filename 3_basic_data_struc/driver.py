from Unordered_list import UnorderedList

my_list = UnorderedList()
my_list.add(31)
my_list.add(77)
my_list.add(17)
my_list.add(93)
my_list.add(26)
my_list.add(54)

# print(dir(my_list.head))
# print(my_list.length())
print(my_list.head.get_next().get_data())
print(my_list.length())
print(my_list.remove(54))
print(my_list.length())