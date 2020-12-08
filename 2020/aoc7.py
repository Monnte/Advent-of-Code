with open("input7") as f:
    rules = f.readlines()
rules = [x.strip() for x in rules]

bagArray = {}
gold = 0
shinyBag = 0

# part 2
def shinyBagContain(bag, multiply):
    bags = bagArray[bag]
    for b in bags:
        if(b == "no other"):
            continue
        bagNumer = int(b[0])
        b = b[2:]

        global shinyBag
        shinyBag += bagNumer * multiply
        shinyBagContain(b, multiply * bagNumer)


# part 1
def goldyBag(bag):
    if bagArray.get(bag) != None:
        bags = bagArray[bag]
        for b in bags:
            # slice number out
            b = b[2:]
            if b.find("shiny gold") != -1:
                global gold
                gold += 1
                return 1
            if goldyBag(b) == 1:
                return 1


for rule in rules:
    bagName = rule[0:rule.find("bags")].strip()
    rulesForBag = rule[rule.find("bags"):].replace(
        "bags contain ", "").replace("bags", "").replace("bag", "").replace(".", "").split(",")
    for i in range(len(rulesForBag)):
        rulesForBag[i] = rulesForBag[i].strip()

    bagArray[bagName] = rulesForBag

for key, value in bagArray.items():
    goldyBag(key)

shinyBagContain("shiny gold", 1)
print("1 answer : " + str(gold))
print("2 answer : " + str(shinyBag))
