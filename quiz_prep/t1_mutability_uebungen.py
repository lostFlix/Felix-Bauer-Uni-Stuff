# quiz prep - topic 1 mutability


#i used claude to help me preparing, so he gave me exercises and i solved them...


print(9 / 3)            # 3.0   hatte 3. / gibt immer float, auch wenns aufgeht
print(11 // 4, 11 % 4)  # 2 3


# ---------- 1. strings aendern sich nicht ----------
s = "uzh"
s.upper()
print(s)                # uzh   hatte UZH. upper() macht einen neuen string,
                        #       s selber bleibt wie es ist
t = s.upper()
print(t)                # UZH
print(s, t)             # uzh UZH

# wie in R: toupper(s) aendert s auch nicht, man braucht s <- toupper(s)

stadt = "wien"
stadt.upper()
print(stadt)            # wien
stadt = stadt.upper()   # jetzt mit = und dem eigenen namen, also wirklich neu
print(stadt)            # WIEN
kurz = stadt.lower()
print(stadt, kurz)      # WIEN wien


# ---------- 2. listen aendern sich schon ----------
zahlen = [3, 1]
zahlen.append(2)        # kein = noetig, die liste selber wird laenger
print(zahlen)           # [3, 1, 2]   hatte 3 1 2 ohne klammern geschrieben.
                        #             liste wird immer mit [ ] und kommas gedruckt
name = "uzh"
name.upper()
print(zahlen, name)     # [3, 1, 2] uzh


# ---------- 3. alias ----------
a = [1, 2]
b = a                   # keine kopie! eine liste, zwei namen
b.append(3)
print(a)                # [1, 2, 3]
print(b)                # [1, 2, 3]


# ---------- 4. copy ----------
a = [1, 2]
b = a.copy()            # eigene liste mit gleichem inhalt
b.append(3)
print(a)                # [1, 2]
print(b)                # [1, 2, 3]
c = a
c.append(9)
print(a, b)             # [1, 2, 9] [1, 2, 3]

# so merk ich mir das: liste = karton, name = etikett.
# b = a          -> a und b kleben auf dem gleichen karton
# b = a.copy()   -> b kopiert den inhalt von a, hat aber einen eigenen karton


# ---------- 5. == und is ----------
a = [1, 2]
b = a
c = a.copy()
print(a == b)           # True    == fragt: gleicher inhalt?
print(a is b)           # True    is fragt: der gleiche karton?
print(a == c)           # True
print(a is c)           # False   gleicher inhalt, anderer karton


# ---------- 6. append gibt None zurueck ----------
# das fand ich erst komisch. erklaerung die geholfen hat:
# upper() ist wie ein copyshop, man bekommt was neues in die hand.
# append() ist wie ein handwerker, der baut direkt an der liste rum und
# gibt einem nichts zurueck. nichts = None
a = [1, 2]
b = a.append(3)
print(a)                # [1, 2, 3]
print(b)                # None
print(7 % 2, 8 / 4)     # 1 2.0   hatte 1, 2.0 mit komma. kommt kein komma hin

a = [5]
x = a.append(6)
print(x)                # None
print(a)                # [5, 6]
s = "hi"
y = s.upper()
print(y)                # HI
print(s, a)             # hi [5, 6]


# ---------- 7. sorted() und .sort() ----------
obst = [3, 1, 2]
neu = sorted(obst)      # copyshop: neue sortierte liste, obst bleibt
print(neu)              # [1, 2, 3]
print(obst)             # [3, 1, 2]
x = obst.sort()         # handwerker: sortiert obst selber, gibt None
print(x)                # None
print(obst)             # [1, 2, 3]


# ---------- 8. namen neu vergeben (rebinding) ----------
a = [1, 2]
b = a
b = [7, 8]              # etikett b klebt jetzt auf einem neuen karton
b.append(9)             # trifft nur noch den neuen
print(a)                # [1, 2]
print(b)                # [7, 8, 9]
print(a is b)           # False


# ---------- alles gemischt ----------
# hier hab ich die meisten fehler gemacht. einzeln ging alles, gemischt nicht.

x = [4, 2]
y = x
y.append(6)
z = x.copy()
z.append(8)
print(x)                # [4, 2, 6]
print(x == y, x is z)   # True False   hatte bei == die liste hingeschrieben,
                        #              == gibt aber True oder False

w = "Zurich"
w.lower()
v = w.upper()
print(w, v)             # Zurich ZURICH

n = [2, 3, 1]
m = sorted(n)
n = n.append(0)
print(m)                # [1, 2, 3]   hatte [0, 1, 2, 3]. m ist schon fertig
                        #             bevor die 0 dazukommt
print(n)                # None        hatte auch [0, 1, 2, 3]. append gibt None
                        #             und das landet dann in n

p = [9, 7]
q = p
q = [1]
p.sort()
print(p, q)             # [7, 9] [1]  hatte [9, 7] 1. das p.sort() uebersehen
                        #             und bei [1] die klammern vergessen
print(8 / 2)            # 4.0

# zweiter versuch, diesmal mit tabelle auf papier (eine spalte pro name)
a = [3, 1]
b = sorted(a)
a.append(2)
print(a)                # [3, 1, 2]   hatte wieder 0 statt 2 angehaengt,
print(b)                # [1, 3]      und die zahl auch in b. nochmal falsch

k = [5, 4]
k = k.sort()
print(k)                # None

r = [2, 1]
t = r
t = [8]
r.sort()
print(r, t)             # [1, 2] [8]
print(r == t)           # False

c = [4, 2]
d = sorted(c)
c.append(1)
print(d)                # [2, 4]      jetzt richtig
print(c)                # [4, 2, 1]
