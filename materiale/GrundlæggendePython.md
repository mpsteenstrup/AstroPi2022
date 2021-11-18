### Opsamling programmering ###

Her er nogle centrale elementer i programmering.

### Løkker ###
Løkker eller loops, er dele af programmet som gentages. I python sker det ved indryk og : (i andre programmet bruges eks. vec {}).


```python.run
# Løkke itereret over i
i = 0
while i < 10:
  print(i)
  i += 1


# uendelig løkke
#while True:
#  print('hej med jer')
```

* Eksperimenter, prøv at lav om i begingelsen så i kun printer lige tal.
* Fjern # i linje 9 og 10, husk at stop løkken, ellers fortsætter den.



### Hvis betingelser og forgreninger###
Betingelser som kan være sande eller falske, True, False, får programmet til at forgrene sig i forskellige retninge. De er også kaldet if statements. If statements tjekker en betingelse og udfører det indrykkede hvis betingelsen er opfyldt.

```python.run
# Løkke itereret over i
i = 0
while i < 20:
  print(i)
  if i<10:
      i += 1
  if i>=10:
    i +=2
```

* Beskriv hvad betingelserne gør.
* Hvorfor bliver 10 ikke printet?


### Break ###

Vi kan også få noget til at køre uendeligt, eller indtil en betingelse er opfyldt. Det sker med if True og break.

```python.run
# Løkke itereret over i
i = 0
while True:
  print(i)
  i +=1
  if i>14:
    break
print('done')
```
* Beskriv koden og prøv at lave om i den.

### Lister ###

Lister kaldes også arrays og skrives med [] omkring. Man kan putte alt muligt ind i listerne.

```python.run

n = [-1,1,-3,3,-5,5,-7,7] # indeholder tal
t = ['en','to','tre','hej','med','dig','fra','mig'] # indeholder strenge

i = 0
while True:
  print(t[i])
  i = i+1
  if i>7:
    break

i = 0
k = 0
while True:
  k = k + n[i]
  print(k)
  i = i+1
  if i>7:
    break

print('længden af vektoren er')
print(len(t))
```

* Hvordan får man fat i den 'tre' i listen t?
* Prøv at lav betingelsen i>7 om til i>8, hvad sker der?
* Hvordan skal betingelsen være hvis vi skal kunne tage en liste af vilkårlig længde?.



### Funktioner ###

Funktioner er en smarte. De kan bruges til at give overblik eller hvis man skal lave samme operation flere gange. Funktioner bliver defineret med ```def funktionsnavn():``` herefter indryk på næste linje.

```python.run

# funktion uden input og output
def myFunction():
    print('det er min funktion')
myFunction()

# funktion med input
def printMyName(name):
    print(name)
printMyName('Mads Peter')

# funktion med output
def myAdder(a,b):
    return a+b
c = myAdder(5,7)
print(c)

```
* Gennemgå de tre eksempler og lav om i dem.
