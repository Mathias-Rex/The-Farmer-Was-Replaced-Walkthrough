# The Farmer Was Replaced - Agent Rules

## A játék nyelve

A The Farmer Was Replaced **nem valódi Pythont** használ. A szintaxis Python-szerű, de a futtatókörnyezet egy saját, leegyszerűsített motor.

### Ami nincs benne (Python feature-ök, amik nem működnek):
- `class`, `lambda`, list comprehension
- `*args`, `**kwargs`
- `async`/`await`
- ternáris operátor: `a if cond else b`
- limitált `list`/`dict`/`set` metódusok
- standard library (nincs `import os`, `import math`, stb.)

### Adattípus eltérések:
- Minden szám **float** - nincs valódi `int`, ne használj `int()` castolást
- `lst[1.2] == lst[1]` - tört index működik
- `range(0, 1, 0.1)` - tört lépés is ok
- `set` típus **nem elérhető** - helyette `list` + `not in` ellenőrzés

### Furcsa viselkedések:
- `foo(x, y) == x.foo(y)` - metódushívás felcserélhető
- Default paraméterek **híváskor** számolódnak ki (nem definiáláskor, mint Pythonban)

### Output:
- `print()` → füstbe írja a drone felett (lassú, 1s)
- `quick_print()` → output.txt-be ír (0 tick)

### Összefoglalva:
- Amit a játékban írsz → nagyjából valid Python szintaxis
- De nem minden Python kód fut a játékban
- Kezelj DSL-ként: egyszerű, procedurális kód → működik; haladó Python → nem

---

Ez a projekt nem teljesen standard Python futtatókörnyezetet használ. Az alábbi szabályokat tartsd be minden kódmódosításnál.

## 1) Ne hasonlíts függvény objektumot `==`-val

A runtime safeguard hibát dob, ha függvény objektumot közvetlenül hasonlítasz:

- Kerüld: `if plant1 == None`
- Kerüld: `if plant1 != None`

Hiba jelleg: "Trying to use == on the function ...".

## 2) Ne használj függvény objektumot logikai feltételben

A runtime safeguard ezt is blokkolja:

- Kerüld: `if plant1:`
- Kerüld: `if not plant1:`
- Kerüld: `if plant1 and plant2:`

Hiba jelleg: "Trying to check if the function ... is True".

## 3) Az `is` operátor nem megbízható / nem támogatott

Ebben a környezetben `is` használata szintaktikai hibát okozhat
("A COLON is expected here"), ezért ne használd.

- Kerüld: `if plant1 is None:`

## 4) Ajánlott minta callback paramétereknél

Ha opcionális callback paramétereket adnál át (pl. `plant1`, `plant2`), ne ellenőrizd őket közvetlenül.
Ehelyett strukturáld úgy az API-t, hogy mindig ugyanazzal a szignatúrával hívd:

- Jó minta: `do_smtg(plant1, plant2)` minden esetben
- A callback oldalon legyenek default paraméterek: `def fn(a=None, b=None): ...`

## 5) Refaktor guideline

Ha olyan kódot találsz, ami `None`-ellenőrzést csinál függvény referencia változón:

1. Ne cseréld automatikusan `is None`-ra.
2. Inkább kerüld el az ellenőrzést (API-szintű egységes hívás).
3. Ha ellenőrzés kell, ne függvény objektumon történjen, hanem külön flag/enum alapján.

---

Röviden: ebben a projektben a függvény objektumok közvetlen összehasonlítása és truthiness vizsgálata tiltott, az `is` pedig kerülendő.
