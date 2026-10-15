# t4 functions + loops - übungen di 13.10
# aufgaben: claude (tutor), aus dem chat nachgebaut. antworten + fehler: meine
# ausgabe jeweils als kommentar drunter

# --- def = rezept aufschreiben, läuft erst beim aufruf
def gruss(name):
    print("Hallo", name)

print("Start")
gruss("Felix")
gruss("Anna")
# Start
# Hallo Felix
# Hallo Anna

def doppel(x):
    print(x * 2)

doppel(4)
doppel(2.5)
# 8
# 5.0
# - mein fehler: 5 statt 5.0, float bleibt float

# --- print vs return
# print = koch ruft, return = kellner bringt, kein return = leerer teller (None)
def plus_print(a, b):
    print(a + b)

def plus_return(a, b):
    return a + b

r1 = plus_print(2, 3)
r2 = plus_return(2, 3)
print(r1, r2)
# 5
# None 5
# - ausgabe richtig, aber in der tabelle r1 = 5 geschrieben -> r1 = None
# - in r1 landet nur was zurückkommt, die 5 wurde nur gerufen
# - mein fehler: danach nach jedem print None gedruckt (übertrieben)
# - print(6) gibt auch None zurück, druckt aber nur 6

# --- range
for i in range(3):
    print(i)
for i in range(2, 5):
    print(i * 10)
# 0
# 1
# 2
# 20
# 30
# 40
# - stop ist exklusiv, start ist dabei
# - mein fehler: range(2, 5) ohne die 2

# --- akkumulator = sparschwein, neuer wert = alter wert + i
total = 0
for i in range(4):
    total = total + i
print(total)
# 6
# - mein fehler: zahlen aus range(2, 5) von davor genommen -> 9
# - print nicht eingerückt -> nur 1x am ende

punkte = 10
for i in range(1, 4):
    punkte = punkte + i
print(punkte)
# 16

# --- default-argument
def plus(zahl, by=1):
    return zahl + by

x = 10
print(plus(x))
print(plus(x, by=5))
print(x)
# 11
# 15
# 10
# - by nicht angegeben -> 1
# - x ändert sich nur wo x = steht

# --- kurs-aufgabe increment (quiz recap, defaults-loop)
def increment(number, by=1):
    return number + by

x = 0
for i in range(5):
    print(increment(x) if i < 2 else increment(x, by=2))
print("x:", x)

for i in range(3):
    x = increment(x)
print("updated x:", x)
# 1
# 1
# 2
# 2
# 2
# x: 0
# updated x: 3
# - mein versuch komplett falsch (1 2 4 5 6 ...), ohne tabelle gemacht
# - fehler 1: in schleife 1 x hochgezählt, da steht aber kein x = -> x bleibt 0
# - fehler 2: nicht eingerücktes print als pro runde gelesen
# - schleife 2 hat x = -> da zählt es hoch

# --- variante mal
def mal(zahl, faktor=2):
    return zahl * faktor

y = 3
for i in range(4):
    print(mal(y) if i % 2 == 0 else mal(y, faktor=10))
print("y:", y)

for i in range(2):
    y = mal(y)
print("neu:", y)
# 6
# 30
# 6
# 30
# y: 3
# neu: 12
# - mein fehler: bedingung auf mal(y) bezogen (6 % 2) und True gedruckt
# - bedingung prüft nur i, wird nie gedruckt
# - nach ca 2h45 gekippt
