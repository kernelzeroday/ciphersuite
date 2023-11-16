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







$ python megazod.py --alphabets EZSP encode 34 "I am the zodiac killer"
q ♐∏ ∝∅∀ ∪−♓∇♐♒ ∉∇∋∋∀∘


$ python megazod.py --alphabets EZSP decode 34 "q ♐q ♐∏ ∝∅∀ ∪−♓∇♐♒ ∉∇∋∋∀∘"
I am the zodiac killer







$ python nullfinder.py --auto-inject -m "I am the zodiac killer"
Nulls used: 0Fx
Null padded string: I am txhe zodi0ac kilFler


$ python megazod2.py --nulls 0Fx --alphabets "RU,RE,ASC" encode 13 'I am txhe zodi0ac kilFler'
Ф &| >x=_ Г:)[0&( {[}F}_.


$ python megazod2.py --nulls 0Fx --alphabets "RU,RE,ASC" decode 13 'Ф &| >x=_ Г:)[0&( {[}F}_.'
I am the zodiac killer





$ python megazod2.py --nulls 7Rj --alphabets "CH,RU,EN,FR" encode 8 'I like killing people because it is so much fun. It is mor7e fun than killing wild game in the forest because man is the most dangerous aniRmal of all. To kill something gives me the most thrilling experiejnce. It is even better than getting your rocks off with a girl. The best part of it is that when I die, Ill be reborn in paradise, and all that I have killed will become my slaves. I will not give you my name because you will try to slow down, or stop my collection of slaves for my afterlife.'
А ЪШЩФ ЩШЪЪШЬЦ ЮФЭЮЪФ СФТР🤣😁Ф Ш😂 Ш😁 😁Э Ы🤣ТЧ Х🤣Ь. А😂 Ш😁 ЫЭ😀7Ф Х🤣Ь 😂ЧРЬ ЩШЪЪШЬЦ 😄ШЪУ ЦРЫФ ШЬ 😂ЧФ ХЭ😀Ф😁😂 СФТР🤣😁Ф ЫРЬ Ш😁 😂ЧФ ЫЭ😁😂 УРЬЦФ😀Э🤣😁 РЬШRЫРЪ ЭХ РЪЪ. ЙЭ ЩШЪЪ 😁ЭЫФ😂ЧШЬЦ ЦШ😃Ф😁 ЫФ 😂ЧФ ЫЭ😁😂 😂Ч😀ШЪЪШЬЦ Ф😅ЮФ😀ШФjЬТФ. А😂 Ш😁 Ф😃ФЬ СФ😂😂Ф😀 😂ЧРЬ ЦФ😂😂ШЬЦ 😆Э🤣😀 😀ЭТЩ😁 ЭХХ 😄Ш😂Ч Р ЦШ😀Ъ. ЙЧФ СФ😁😂 ЮР😀😂 ЭХ Ш😂 Ш😁 😂ЧР😂 😄ЧФЬ А УШФ, АЪЪ СФ 😀ФСЭ😀Ь ШЬ ЮР😀РУШ😁Ф, РЬУ РЪЪ 😂ЧР😂 А ЧР😃Ф ЩШЪЪФУ 😄ШЪЪ СФТЭЫФ Ы😆 😁ЪР😃Ф😁. А 😄ШЪЪ ЬЭ😂 ЦШ😃Ф 😆Э🤣 Ы😆 ЬРЫФ СФТР🤣😁Ф 😆Э🤣 😄ШЪЪ 😂😀😆 😂Э 😁ЪЭ😄 УЭ😄Ь, Э😀 😁😂ЭЮ Ы😆 ТЭЪЪФТ😂ШЭЬ ЭХ 😁ЪР😃Ф😁 ХЭ😀 Ы😆 РХ😂Ф😀ЪШХФ.

$ python megazod2.py --nulls 7Rj --alphabets "CH,RU,EN,FR" decode 8 'А ЪШЩФ ЩШЪЪШЬЦ ЮФЭЮЪФ СФТР🤣😁Ф Ш😂 Ш😁 😁Э Ы🤣ТЧ Х🤣Ь. А😂 Ш😁 ЫЭ😀7Ф Х🤣Ь 😂ЧРЬ ЩШЪЪШЬЦ 😄ШЪУ ЦРЫФ ШЬ 😂ЧФ ХЭ😀Ф😁😂 СФТР🤣😁Ф ЫРЬ Ш😁 😂ЧФ ЫЭ😁😂 УРЬЦФ😀Э🤣😁 РЬШRЫРЪ ЭХ РЪЪ. ЙЭ ЩШЪЪ 😁ЭЫФ😂ЧШЬЦ ЦШ😃Ф😁 ЫФ 😂ЧФ ЫЭ😁😂 😂Ч😀ШЪЪШЬЦ Ф😅ЮФ😀ШФjЬТФ. А😂 Ш😁 Ф😃ФЬ СФ😂😂Ф😀 😂ЧРЬ ЦФ😂😂ШЬЦ 😆Э🤣😀 😀ЭТЩ😁 ЭХХ 😄Ш😂Ч Р ЦШ😀Ъ. ЙЧФ СФ😁😂 ЮР😀😂 ЭХ Ш😂 Ш😁 😂ЧР😂 😄ЧФЬ А УШФ, АЪЪ СФ 😀ФСЭ😀Ь ШЬ ЮР😀РУШ😁Ф, РЬУ РЪЪ 😂ЧР😂 А ЧР😃Ф ЩШЪЪФУ 😄ШЪЪ СФТЭЫФ Ы😆 😁ЪР😃Ф😁. А 😄ШЪЪ ЬЭ😂 ЦШ😃Ф 😆Э🤣 Ы😆 ЬРЫФ СФТР🤣😁Ф 😆Э🤣 😄ШЪЪ 😂😀😆 😂Э 😁ЪЭ😄 УЭ😄Ь, Э😀 😁😂ЭЮ Ы😆 ТЭЪЪФТ😂ШЭЬ ЭХ 😁ЪР😃Ф😁 ХЭ😀 Ы😆 РХ😂Ф😀ЪШХФ.'
I like killing people because it is so much fun. It is more fun than killing wild game in the forest because man is the most dangerous animal of all. To kill something gives me the most thrilling experience. It is even better than getting your rocks off with a girl. The best part of it is that when I die, Ill be reborn in paradise, and all that I have killed will become my slaves. I will not give you my name because you will try to slow down, or stop my collection of slaves for my afterlife.



```
