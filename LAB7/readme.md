# Test strony internetowej simplilearn

Platforma edukacyjna oferująca szeroką gamę kursów online w dziedzinie technologii, zarządzania projektami, danych, programowania itp.
Strona oferuje zarówno kursy jednostkowe, jak i programy specjalistyczne, które prowadzą do certyfikacji w różnych dziedzinach.

## Podgląd Testu:

Platforma edukacyjna musi spełniać wymagania umożliwiające obsługę łącznie 1000 użytkowników końcowych. W ramach zestawu testów obciążeniowych przeprowadzimy serię testów, wysyłając tę liczbę zapytań w różnych interwałach czasowych, aby ocenić wydajność platformy edukacyjnej.

### Status 1:

1000 wątków w 150 sekund
![plot](./results_image/Status1_150.png)
<br>
Poniżej następujące wyniki:
<br>
Średnia: 219ms
<br>
Minimun: 144ms
<br>
Maksimum: 502ms
<br>
Procent błędu: 0%

![plot](./results_image/Status1_150_Summary_Report.png)

### Status 2:

1000 wątków w 120 sekund
![plot](./results_image/Status2_120.png)
<br>
Lekkie zmiany w wynikach, wartość maksiumum wzrosła z 502ms na 21241 tys. ms, test będzie dalej kontynuowany.

<br>
Poniżej następujące wyniki:
<br>
Średnia: 228ms
<br>
Minimun: 148ms
<br>
Maksimum: 21241ms
<br>
Procent błędu: 0%

![plot](./results_image/Status2_120_Summary_Report.png)

### Status 3:

1000 wątków w 90 sekund
![plot](./results_image/Status3_90.png)
<br>
Zauważono spadek Średniej = 203ms oraz Maksimum = 461ms.

<br>
Poniżej następujące wyniki:
<br>
Średnia: 203ms
<br>
Minimun: 145ms
<br>
Maksimum: 461ms
<br>
Procent błędu: 0%

![plot](./results_image/Status3_90_Summary_Report.png)

### Status 4:

1000 wątków w 60 sekund
![plot](./results_image/Status4_60.png)
<br>
Zaobserwowano limit zwiększenie opóźnienia maksimum aż z 461ms do 1267 tys ms. Kontynuacja testu w celu znalezienia kolejnego limitu np: pojawienie się błędu połączeń HTTP.

<br>
Poniżej następujące wyniki:
<br>
Średnia: 215ms
<br>
Minimun: 146ms
<br>
Maksimum: 1267ms
<br>
Procent błędu: 0%

![plot](./results_image/Status4_60_Summary_Report.png)

### Status 5:

1000 wątków w 40 sekund
![plot](./results_image/Status5_40.png)
<br>
Osiągnięto kolejny limit maksimum na 21334 tys ms. Kontynuacja testu.

<br>
Poniżej następujące wyniki:
<br>
Średnia: 244ms
<br>
Minimun: 154ms
<br>
Maksimum: 21334ms
<br>
Procent błędu: 0%

![plot](./results_image/Status5_40_Summary_Report.png)

### Status 6:

1000 wątków w 30 sekund
![plot](./results_image/Status6_30.png)
<br>
Następny wzrost maksimum do 21261 tys ms.

<br>
Poniżej następujące wyniki:
<br>
Średnia: 267ms
<br>
Minimun: 159ms
<br>
Maksimum: 21261ms
<br>
Procent błędu: 0%

![plot](./results_image/Status6_30_Summary_Report.png)

### Status 7:

1000 wątków w 20 sekund
![plot](./results_image/Status7_20.png)
<br>
Spadek maksimum z 21261 tys ms na 1311 tys ms. Kontynuacja dalej testu. Wzrost średniej na 275ms z 267ms oraz Minimum na 166ms z 159ms.

<br>
Poniżej następujące wyniki:
<br>
Średnia: 275ms
<br>
Minimun: 166ms
<br>
Maksimum: 1311ms
<br>
Procent błędu: 0%

![plot](./results_image/Status7_20_Summary_Report.png)

### Status 8:

1000 wątków w 15 sekund
![plot](./results_image/Status8_15.png)
<br>
Bez zmian. Jedynie wzrost średniej na 363ms oraz maksimum na 1402 tys ms.

<br>
Poniżej następujące wyniki:
<br>
Średnia: 363ms
<br>
Minimun: 177ms
<br>
Maksimum: 1402ms
<br>
Procent błędu: 0%

![plot](./results_image/Status8_15_Summary_Report.png)

### Status 9:

1000 wątków w 10 sekund
![plot](./results_image/Status9_10.png)
<br>
Limit dużego wzrostu opóźnienia. Średnie opóźnienie wzrosło z 363ms do ponad 2289 tys.ms. Zwiększono maksymalne opóźnienie z 1402 tys.ms do 22570 tys. ms. Dalsza kontynuacja testu.

<br>
Poniżej następujące wyniki:
<br>
Średnia: 2289ms
<br>
Minimun: 292ms
<br>
Maksimum: 22570ms
<br>
Procent błędu: 0%

![plot](./results_image/Status9_10_Summary_Report.png)

### Status 10:

1000 wątków w 6 sekund
![plot](./results_image/Status10_6.png)
<br>
Poraz kolejny wzrost średniego i maksymalnego opóźnienia. Kontynuacja testu w celu znalezienia pierwszych występujących błędów połączeń HTTP.

<br>
Poniżej następujące wyniki:
<br>
Średnia: 9012ms
<br>
Minimun: 199ms
<br>
Maksimum: 38401ms
<br>
Procent błędu: 0%

![plot](./results_image/Status10_6_Summary_Report.png)

### Status 11:

1000 wątków w 4 sekund
![plot](./results_image/Status11_4.png)
<br>
Osiągnięto następujący wynik: Średnia wzrosła z 9012 tys.ms na 11666 tys.ms a maksymalna zwiększyła się aż do 177019 tys.ms.
Procent błędów wzrósł z 0% do 0,20%. Osiągnęliśmy limit, gdzie przerywamy kontynuację testów obciążeniowych.

<br>
Poniżej następujące wyniki:
<br>
Średnia: 11666ms
<br>
Minimun: 294ms
<br>
Maksimum: 177019ms
<br>
Procent błędu: 0,20%

![plot](./results_image/Status11_4_Summary_Report.png)
