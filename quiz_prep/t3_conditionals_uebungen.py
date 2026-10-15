# t3 conditionals - übungen mo 12.10 / di 13.10
# aufgaben: claude (tutor), aus dem chat nachgebaut. antworten + fehler: meine
# ausgabe jeweils als kommentar drunter

# --- if / elif / else = weiche, immer genau 1 gleis
x = 7
if x > 5:
    print("A")
elif x > 3:
    print("B")
else:
    print("C")
# A
# - erster treffer gewinnt, elif wird nicht mehr geprüft obwohl 7 > 3 auch true

# --- mehrere if = eigene ketten
x = 3
if x > 1:
    print("A")
if x > 5:
    print("B")
else:
    print("C")
# A
# C
# - 2 ketten nicht 3, else gehört nur zum 2. if
# - mein fehler: 1x else-zweig vergessen, 1x 3 ketten gezählt (lesefehler)

# --- == vergleicht, = weist zu
print(10 == 10.0)
print(10 == "10")
print(type(10 == 10.0))
# True
# False
# <class 'bool'>
# - int vs str ist kein error, einfach False
# - mein fehler: type(a == b) als int -> von innen lesen, == gibt immer bool

# --- truthiness: wert -> bool() -> gleis
print(bool("False"))
print(bool(""))
print(bool([0]))
print(bool(0))
# True
# False
# True
# False
# - "False" ist str mit inhalt -> truthy
# - [0] liste mit 1 element -> truthy, egal was drin
# - mein fehler: 0 als truthy (1x, konzentration)
# - mein fehler: in bool( ) das ergebnis statt den wert reingeschrieben

# --- or gibt einen WERT zurück: nimm links, sonst rechts
print("" or "Nudeln")
a = ""
b = "Gast"
print(a or b)
print(b or a)
# Nudeln
# Gast
# Gast
# - kühlschrank: pizza da? sonst nudeln
# - links/rechts-regel hat bei mir nicht geklickt, "nimm x sonst y" schon

# --- ternary: erst die mitte, dann links oder rechts
punkte = 7
label = "bestanden" if punkte >= 4 else "durch"
print(label)
for i in range(4):
    print("klein" if i < 2 else "gross")
# bestanden
# klein
# klein
# gross
# gross
# - die mitte wird nie gedruckt
