stops = [ "Croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket" ]

#1. Add "Edinburgh Waverley" to the end of the list
stops.append ('Edinburgh Waverly')
print(stops)
#2. Add "Glasgow Queen St" to the start of the list
stops.insert(0, "Glasgow Queen St")
print(stops)
#3. Add "Polmont" at the appropriate point (between "Falkirk High" and "Linlithgow")
stops.insert(4, "Polmont")
print(stops)
#4. Print out the index position of "Linlithgow"

index = stops.index("Linlithgow")
print(index)
# OR....
#print(stops.index("Linlitgow"))
#5. Remove "Livingston" from the list using its name
stops.remove("Livingston")
print(stops)

#6. Delete "Cumbernauld" from the list by index
stops.pop(2)
print(stops)

#OR...
#stops.pop(stops.index("Cumbernauld"))

#7. Print the number of stops there are in the list
number_of_stops = len(stops)
print(number_of_stops)
#OR...
#print(len(stops))

#8. Sort the list alphabetically
alphabetically = sorted(stops)
print (alphabetically)

#OR...
# stops.sort() original list is changed. adding a variable creates a separate sorted list

#9. Reverse the positions of the stops in the list
reverse_list = stops.reverse()
print(stops)

# OR....
# stops.sort(reverse=True)
#10 Print out all the stops using a for loop

for stations in stops:
    print(f"This train stops at {stations}.")

for stop in stops:
    print(stop)