logsof2021 = 



list2 = []
for crime in logsof2021:
  print(crime["FIELD6"])

  list2.append(crime["FIELD6"])
  # for crime.field6 in crime:
  #   print(e,b)


dictionary2 = {}
print(dictionary2)
for campus in list2:

  var = dictionary2.get(campus)

  if var:
    dictionary2[campus] = dictionary2[campus]+1
  else:
    dictionary2.update({campus : 1})


print(dictionary2)

list3 = []
for actualcrime in logsof2022:
  print(actualcrime["FIELD8"])

  list3.append(actualcrime["FIELD8"])


print(list3)



dictionary3 = {}
print(dictionary3)
for ret in list3:

  var = dictionary3.get(ret)

  if var:
    dictionary3[ret] = dictionary3[ret]+1
  else:
    dictionary3.update({ret : 1})


print(dictionary3)



sortedcrimes = dict(sorted(dictionary3.items(), key=lambda item: item[1]))

print(sortedcrimes)