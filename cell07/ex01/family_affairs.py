def find_the_redheads(family):
  return [item[0] for item in filter(lambda item: item[1] == "red", family.items())]

dupont_family = {
  "florian": "red",
  "marie": "blond",
  "virginie": "brunette",
  "david": "red",
  "franck": "red"
}

print(find_the_redheads(dupont_family))
