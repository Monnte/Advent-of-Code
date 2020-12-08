# Not ideal solution but it works xD ... shame on me
with open("input4") as f:
    lines = f.readlines()
lines = [x.strip() for x in lines]

answer1 = 0
answer2 = 0
passport = []
for a in lines:
    if a == "" or a == "":
        passport = ' '.join(passport)
        if passport.find("pid") != -1 and passport.find("ecl") != -1 and passport.find("hcl") != -1 and passport.find("hgt") != -1 and passport.find("eyr") != -1 and passport.find("iyr") != -1 and passport.find("byr") != -1:
            answer1 += 1
            passport = passport.split(" ")
            passport.sort()
            if passport[1].find("cid") != -1:
                passport.pop(1)
            if int(passport[0][4:]) >= 1920 and int(passport[0][4:]) <= 2002:
                if int(passport[5][4:]) >= 2010 and int(passport[5][4:]) <= 2020:
                    if int(passport[2][4:]) >= 2020 and int(passport[2][4:]) <= 2030:
                        if passport[1][4:] == "amb" or passport[1][4:] == "blu" or passport[1][4:] == "brn" or passport[1][4:] == "gry" or passport[1][4:] == "grn" or passport[1][4:] == "hzl" or passport[1][4:] == "oth":
                            if len(passport[6][4:]) == 9:
                                for i in passport[6][4:]:
                                    if str(i).isdigit() == False:
                                        continue
                                if len(passport[3][5:]) == 6 and passport[3][4] == "#":
                                    for a in passport[3][5:]:
                                        if a.isdigit() == False:
                                            if (a < 'a' or a > 'f'):
                                                continue
                                        int(passport[3][5:20], 16)
                                    hgt = passport[4].split(":")
                                    index = hgt[1].find("cm")
                                    if index != -1:
                                        if int(hgt[1][0:index]) >= 150 and int(hgt[1][0:index]) <= 193:
                                            answer2 = answer2 + 1

                                    elif hgt[1].find("in") != -1:
                                        if int(hgt[1][0:hgt[1].find("in")]) >= 59 and int(hgt[1][0:hgt[1].find("in")]) <= 76:
                                            answer2 = answer2 + 1

        passport = []
    else:
        passport.append(a)

print("1 answer : " + str(answer1))
print("2 answer : " + str(answer2))
