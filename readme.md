# cipher suite

usage:

```
$ python zodiac.py encode 4 "I am the Zodiac Killer"
M eq xli ♋shmeg Omppiv


$ python zodiac.py decode 4 "M eq xli ♋shmeg Omppiv"
I am the zodiac Killer






$ python greekzodiac.py encode 23 "I am the zodiac killer"
♍ x♑ ε♌♉ λ♓♈♍xz ♏♍♐♐♉γ


$ python greekzodiac.py decode 23 "♍ x♑ ε♌♉♍ x♑ ε♌♉ λ♓♈♍xz ♏♍♐♐♉γ"
i am the zodiac killer







$ python multizod.py --alphabets ZAG encode 25 "I am the zodiac killer"
ك ΜΩ ♎ΤΠ ا♉ΟΥΜΞ ΧΥΨΨΠ♌


$ python multizod.py --alphabets ZAG decode 25 "ك ΜΩ ♎ΤΠ ا♉ΟΥΜΞ ΧΥΨΨΠ♌"
I am the zodiac killer
```
