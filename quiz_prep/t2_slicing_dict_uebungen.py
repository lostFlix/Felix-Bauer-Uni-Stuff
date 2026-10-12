# quiz prep - topic 2 indexing, slicing, dict (so 11.10. nachmittag)


# exercises from claude (tutor), i wrote the output on paper first.
# output + my mistakes as comments.


# ---------- 0. wiederholung ----------
z = [5, 2, 9]
s = sorted(z)
z.append(1)
print(z, s)             # [5, 2, 9, 1] [2, 5, 9]   sorted = momentaufnahme
print(s == z)           # False

print(7 / 7, 7 // 2)    # 1.0 3   hatte 3.0. // mit zwei int bleibt int
print(9 // 2, 9 / 3)    # 4 3.0
print(6 / 2, 6 // 2)    # 3.0 3


# ---------- 1. index, zaehlt ab 0 ----------
word = "Zurich"
fruits = ["apple", "kiwi", "plum"]
print(word[0])          # Z
print(fruits[1])        # kiwi
print(word[2], fruits[0])   # r apple


# ---------- 2. negativer index ----------
nums = [10, 20, 30, 40]
print(word[-1])         # h
print(nums[-2], nums[0])    # 30 10
print(nums[-1] + nums[1])   # 60


# ---------- 3. slice [start:stop], stop nicht dabei ----------
print(word[1:4])        # uri
print(word[0:2])        # Zu
print(nums[1:3])        # [20, 30]   hatte 20 30. slice von liste = liste

print(nums[0:2])        # [10, 20]
print(nums[2], nums[3]) # 30 40      hatte [30] [40]. ohne : = element
print(nums[2:4])        # [30, 40]   hatte [30] [40]. eine liste, klammern aussen


# ---------- 4. fruits[1] vs fruits[1:2] ----------
print(fruits[1])        # kiwi
print(fruits[1:2])      # ['kiwi']          hatte 'kiwi' ohne [ ]
print(fruits[0:2])      # ['apple', 'kiwi'] hatte 'apple' 'kiwi'
# regel: ' ' nur wenn auch [ ] da sind. erst [ ] hinschreiben, dann fuellen

tiere = ["hund", "katze", "maus", "igel"]
print(tiere[2])         # maus
print(tiere[2:3])       # ['maus']
print(tiere[1:3])       # ['katze', 'maus']   leerzeichen nach komma!
print(tiere[0], tiere[3])   # hund igel


# ---------- 5. grenzen weglassen ----------
print(word[:3])         # Zur
print(word[3:])         # ich
print(nums[:2], nums[2:])   # [10, 20] [30, 40]   zwei listen


# ---------- 6. [::-1] umdrehen, neues objekt ----------
n3 = [1, 2, 3]
r = n3[::-1]
print(word[::-1])       # hciruZ
print(r, n3)            # [3, 2, 1] [1, 2, 3]


# ---------- 7. zwei klammern hintereinander ----------
fr = ["apple", "kiwi", "banana"]
print(fr[2][:3])        # ban   hatte "ban" mit anfuehrungszeichen
print(fr[0][-1])        # e
print(fr[1][0], fr[-1][1:3])    # k an

staedte = ["Wien", "Bern", "Basel"]
print(staedte[0][1:])   # ien
print(staedte[1:2])     # ['Bern']
print(staedte[2][0], staedte[0][-1])    # B n


# ---------- 8. fruit[1] vs fruits[1] in der schleife ----------
# fruit = ein wort (wandert), fruits = ganze liste (bleibt gleich)
for fruit in fruits:
    print(fruit[1], fruits[1])
# p kiwi
# i kiwi
# l kiwi
# hatte nur "i kiwi", dazwischen 'apple' und 'Kiwi'. ausgeschrieben pro runde hats geklappt

namen = ["Tom", "Ida", "Max"]
for name in namen:
    print(name[0], namen[2])
# T Max
# I Max
# M Max


# ---------- 9. dict: key statt position ----------
preis = {"apple": 3, "kiwi": 5}
print(preis["kiwi"])                    # 5
print(preis["apple"] + preis["kiwi"])   # 8
print(preis["apple"], preis["kiwi"])    # 3 5

p = {"name": "Felix", "noten": [5, 6, 4]}
print(p["name"])        # Felix
print(p["noten"])       # [5, 6, 4]
print(p["noten"][0], p["name"][0])      # 5 F

unis = {
    "wien": {"land": "AT", "ects": 180},
    "uzh": {"land": "CH", "ects": 36},
}
print(unis["uzh"]["land"])      # CH   hatte AT, key von wien genommen
print(unis["wien"]["ects"] + unis["uzh"]["ects"])   # 216
print(unis["wien"]["land"], unis["uzh"]["land"][0]) # AT C


# ---------- 10. key fehlt: [ ] vs .get ----------
print(preis.get("kiwi", 0))     # 5      key da -> default egal
print(preis.get("plum"))        # None
print(preis.get("plum", 0), preis["apple"])     # 0 3
# print(preis["plum"])          # KeyError, danach laeuft nichts mehr


# ---------- 11. mix t1 + t2 ----------
a = [3, 1, 2]
b = a           # alias, gleicher karton
c = a[1:]       # slice, neuer karton
b.append(9)
d = {"x": a[-1], "y": c}
print(a, c)                 # [3, 1, 2, 9] [1, 2]   hatte a ohne 9
print(d["x"], d["y"][0])    # 9 1                   hatte 2 1

p2 = [7, 4]
q = p2[:]       # slice = kopie
r2 = p2         # alias
r2.append(5)
info = {"lang": p2[-1], "kurz": q}
print(p2, q)                        # [7, 4, 5] [7, 4]   hatte q mit 5
print(info["lang"], info["kurz"][-1])   # 5 4           hatte 5 5
# regel: nur der nackte name rechts vom = ist ein alias.
# p[:], p[1:], p.copy(), sorted(p) = neuer karton
