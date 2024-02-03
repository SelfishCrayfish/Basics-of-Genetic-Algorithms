## Zadanie 1  
Załóżmy, że mamy zbiór 10 genów, z któych każdy może przyjąć wartość binarną (0 lub 1). Funkcja
przystosowania jest obliczana jako liczba genów o wartości 1 obecnych w chromosomie. Im większ
liczba genów o wartości 1, tym wyższy poziom dopasowania. Zaimplementuj algorytm genetyczny,
który będzie się starał zmaksymalizować poziom przystosowania osobników w populacji. Przyjmij
rozmiar populacji równy 10. W każdej generacji dwóch najlepiej przystosowanych osobników z całej
populacji jest wybieranych i poddawanych operacji krzyżowania, w wyniku której powstaje dwóch
potomków. Zastępują oni dwóch najmniej przystosowanych osobników w populacji. Dodatkowo z
prawdopodobieństwem 60% może nastąpić mutacja polegająca na zamianie wartości losowego genu
na przeciwną, wśród dwóch najlepszych osobników.

## Zadanie 2  
Napisz program wyznaczający za pomocą algorytmu genetycznego rozwiązanie równania $2a^2 + b = 33$, gdzie $a, b ∈< 0, 15 >$. Chromosom powinien składać się z 8 bitów (po 4 bity zajmowane przez
wartość zmiennej a i b). Obliczanie funkcji przystosowania powinno odbywać się na podstawie fenotypu (wartościach zmiennych a i b). Rozmiar populacji przyjmij na 10 osobników, w każdej generacji
nowa populacja wybierana jest za pomocą metody ruletki, a następnie 50% osobników tej populacji
podlega krzyżowaniu, potomek zastępuje w populacji jednego z rodziców. Każdy z osobników nowej
populacji może ulec mutacji z prawdopodobieństwem 10%.

## Zadanie 3 - problem plecakowy  
Napisz program, który będzie rozwiązywał problem plecakowy za pomocą algorytmu genetycznego.
Problem plecakowy często przedstawia się jako problem złodzieja rabującego sklep – znalazł on
10 towarów; j–ty przedmiot jest wart vj oraz waży wj . Złodziej dąży do zabrania ze sobą jak
najwartościowszego łupu, przy czym nie może zabrać więcej niż 35 kilogramów. Nie może też zabierać
ułamkowej części przedmiotów (byłoby to możliwe w ciągłym problemie plecakowym). Wartość
funkcji przystosowania będzie obliczania zgodnie z następującym wzorem:  

![image](https://github.com/SelfishCrayfish/Basics-of-Genetic-Algorithms/assets/137427463/d5b37774-5f34-4c90-a5b5-041f8037a606)

gdzie:  
• $n$ - długość chromosomu (odpowiada liczbie wszystkich przedmiotów w sklepie),  
• $c_i$ - wartość i-tego genu (1 oznacza, że dany przedmiot jest spakowany do torby, 0, że nie),  
• $w_i$ - waga i-tego przedmiotu,  
• $v_i$ - wartość i-tego przedmiotu.  

Przyjmij rozmiar populacji równy 8. W trakcie implementacji algorytmu wykorzystaj zasadę elitarności, jako próg przyjmij 25% osobników w populacji. Z całej populacji wybierana jest tymczasowa
populacja za pomocą metody ruletki, a następnie dochodzi do krzyżowań pomiędzy osobnikami, a
nowo powstałe osobniki trafiają do nowej populacji. Dodatkowo każdy gen każdego z nowych osobników może podlegać mutacji z prawdopodobieństwem 5%. Oznacza to, że nowa populacja będzie
składała się w 25% z osobników poprzedniej populacji oraz w 75% z potomków, którzy mogą podlegać
mutacji.  
Przetestuj działanie swojego algroytmu na zestawie danych przedstawionym w tabeli 1. Optymalnym (prawdopodobnie) rozwiązaniem dla tego przykładu jest wybranie rzeczy o numerach:
$0, 2, 3, 4, 5, 8$, waga wybranych rzeczy to 32, a wartość 2222.  
| ID | Waga | Wartość |
| -- | ---- | ------- |
| 0 | 3 | 266 |
| 1 | 13 | 442 |
| 2 | 10 | 671 |
| 3 | 9 | 526 |
| 4 | 7 | 388 |
| 5 | 1 | 245 |
| 6 | 8 | 210 |
| 7 | 8 | 145 |
| 8 | 2 | 126 |
| 9 | 9 | 322 |

## Zadanie 4 - problem komiwojażera  
Napisz program, który będzie rozwiązywał problem komiwojażera za pomocą algorytmu genetycznego. Problem komiwojażera (ang. travelling salesman problem, TSP) – zagadnienie optymalizacyjne,
polegające na znalezieniu minimalnego cyklu Hamiltona w pełnym grafie ważonym. Nazwa pochodzi
od typowej ilustracji problemu, przedstawiającej go z punktu widzenia wędrownego sprzedawcy (komiwojażera): dane jest $n$ miast, które komiwojażer ma odwiedzić, oraz odległość podróży pomiędzy
każdą parą miast. Celem jest znalezienie najkrótszej drogi łączącej wszystkie miasta, zaczynającej
się i kończącej się w tym punkcie.
W tym przypadku genem będą współrzędne miasta $(x, y)$ lub indeks miasta (w zależności od
tego, co będzie łatwiej przechowywać). Algorytm powinien działać analogicznie do tego z zadania 3.  

Przyjmij następujące parametry:  
• wielkość populacji - 100,  
• poziom elitarności - 20%,  
• prawdopodobieństwo mutacji - 1%.  

Przetestuj działanie algorytmu na zestawie danych z tabeli 2. Optymalnym (prawdopodobnie)
rozwiązaniem dla tego przykładu jest następująca trasa: $20, 14, 17, 13, 4, 18, 1, 19, 21, 23, 0, 16, 15, 2, 12, 11,
5, 7, 22, 9, 24, 10, 3, 8, 6$, o długości 869.  
| ID | x   | y   |
| -- | --- | --- |
| 0  | 119 | 38  |
| 1  | 37  | 38  |
| 2  | 197 | 55  |
| 3  | 85  | 165 |
| 4  | 12  | 50  |
| 5  | 100 | 53  |
| 6  | 81  | 142 |
| 7  | 121 | 137 |
| 8  | 85  | 145 |
| 9  | 80  | 197 |
| 10 | 91  | 176 |
| 11 | 106 | 55  |
| 12 | 123 | 57  |
| 13 | 40  | 81  |
| 14 | 78  | 125 |
| 15 | 190 | 46  |
| 16 | 187 | 40  |
| 17 | 37  | 107 |
| 18 | 17  | 11  |
| 19 | 67  | 56  |
| 20 | 78  | 133 |
| 21 | 87  | 23  |
| 22 | 184 | 197 |
| 23 | 111 | 12  |
| 24 | 66  | 178 |
