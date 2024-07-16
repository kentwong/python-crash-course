bicycle = ["trek", "cannondale", "redline", "specialized"]

print(*bicycle)
# trek cannondale redline specialized

print(bicycle)  # ['trek', 'cannondale', 'redline', 'specialized']

print(bicycle[0].title())
# Trek
print(bicycle[-1].title())
# specialized
print(bicycle[-2].title())
# Redline
# In python, we can use negative index to access the last element of a list.
# In JS, we can use array.length - 1 to access the last element of an array.
# or array.at(-1) to access the last element of an array.


# Using individual values from a list
message = f"My first bicycle was a {bicycle[0].title()}."
print(message)
# My first bicycle was a Trek.

# Modifying elements in a list
bicycle[0] = "hero"
print(bicycle)
# ['hero', 'cannondale', 'redline', 'specialized']

# Adding elements to a list
bicycle.append("trek")
print(bicycle)
# ['hero', 'cannondale', 'redline', 'specialized', 'trek']

# Inserting elements to a list
bicycle.insert(0, "atlas")
print(bicycle)
# ['atlas', 'hero', 'cannondale', 'redline', 'specialized', 'trek']

# Removing elements from a list
del bicycle[0]
print(bicycle)
# ['hero', 'cannondale', 'redline', 'specialized', 'trek']

# Removing an item using pop() method
popped_bicycle = bicycle.pop()
print(popped_bicycle)
# trek
print(bicycle)
# ['hero', 'cannondale', 'redline', 'specialized']
# By default, pop() removes the last item in a list. But you can remove any item by passing the index of the item to be removed.
popped_bicycle = bicycle.pop(0)
print(popped_bicycle)
# hero

# Removing an item by value
bicycle.remove("redline")
print(bicycle)
# ['cannondale', 'specialized']
# The remove method deletes only the first occurrence of the value you specify. If there's a possibility the value appears more than once in the list, you'll need to use a loop to determine if all occurrences of the value have been removed.

# Organizing a list
bicycle.sort()
print(bicycle)
# ['cannondale', 'specialized']
# The sort() method changes the order of the list permanently. The original order is lost.
bicycle.sort(reverse=True)
print(bicycle)
# ['specialized', 'cannondale']    # reverse sorting
# You can reverse the original order of the list by passing the reverse=True argument to the sort() method.

# Sorting a list temporarily
print(sorted(bicycle))
# ['cannondale', 'specialized']
print(bicycle)
# ['specialized', 'cannondale']
# The sorted() function lets you display your list in a particular order but doesn't affect the actual order of the list.
# You can also pass the reverse=True argument to the sorted() function to reverse the original order of the list.

# Printing a list in reverse order
bicycle.reverse()
print(bicycle)
# ['cannondale', 'specialized']
# The reverse() method changes the order of a list permanently, but you can revert to the original order anytime by calling reverse() a second time.

# Finding the length of a list
print(len(bicycle))
# 2
# The len() function returns the number of items in a list.

# Read even numbered lines
with open(file_name) as file:
    contents = file.readlines()
    content = []
    for index, c in enumerate(contents):
        if not index % 2 == 0:
            content.append(c)
    return content

## But this can be simplified to:
with open(file_name) as file:
    contents = file.readlines()

    return [line for index, line in enumerate(contents) if index % 2 == 1]
    return contents[1::2]
