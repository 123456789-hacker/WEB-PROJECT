#names_list = []
#names_list.append("Alan")
#names_list.append("Natan")

#names_list = ["Alan", "Natan", "Adam", "Alan"]

#names_list = ("Alan", "Natan", "Adam", "Alan")

#print(names_list)

#person = ("Alan", "Sochacki", 17)
#print(len(person))
#print(person)

#print(person.count("Alan"))
#print(person)



#names_list2 = ["Dominik"]

#names_list3 = names_list + names_list2
#print(names_list3)

#names_list.remove("Alan")
#print(names_list)

#names_list.clear()
#print(names_list)

#print(names_list)
#print()
#print(names_list[0])
#print()
#print(names_list)

#print(names_list)
#print()
#print(names_list.pop(0))
#print()
#print(names_list)




#print(names_list)

#names_list.reverse()
#names_list.sort()

#names_list.sort(reverse=True)
#print(names_list)

#for name in names_list:
   # print(name)

#print(names_list[0])


#print(names_list.count("Rafał"))

#print(len(names_list))


#names_set = {"Alan","Natan", "Alan"}
#print(names_set)

#names_set = set()

#names_list = []
#names_tuple = ()


#names_set.add("Alan")
#names_set.add("Natan")

#names_set2 = {"Mariusz", "Tytus", "Alan"}
#names_set3 = names_set.difference(names_set2)
#names_set3 = names_set.intersection(names_set2)
#names_set3 = names_set.symmetric_difference(names_set2)
#names_set.clear()

#names_set = set()
#names_set.add("Alan")
#names_set.add("Natan")
#names_set2 = {"Mariusz", "Tytus", "Alan"}
#names_list = ["Artur","Rafał"]
#names_list.extend(names_set2)
#print(names_list)



#names_set.update(names_set2)

#names_set3 = names_set.union(names_set2)
#names_set.add(names_list)
#names_set.add(names_tuple)

#names_set.remove("Alan")
#names_set.discard("Alan")
#print(names_set)

#print(names_set[0])
#for name in names_set:
#  # print(name)

countries_and_capitals = {"Poland":"Warsaw", "Germany":"Berlin"}
countries_and_capitals['Czechia'] = 'Prague'
#for key in countries_and_capitals.keys(): 
#  #print(key)
#print(countries_and_capitals)



#for capitals in countries_and_capitals.values():
# print(capitals)



#for country, capital in countries_and_capitals.items():#
#print(country +"-" + capital)


#print(countries_and_capitals["Poland"])
#print(countries_and_capitals.get("Poland"))

#print(countries_and_capitals.setdefault("USA","Washington DC"))
#print(countries_and_capitals)

#countries_and_capitals["Poland"] = "Cracow"
#print(countries_and_capitals.pop("USA","Washington DC" ))

#print(countries_and_capitals.popitem())
#print(countries_and_capitals)

if "Poland" in countries_and_capitals.keys():
 print("Znaleziono!")
else:
   print("Nie znaleziono!")

   print("Poland" in countries_and_capitals)

