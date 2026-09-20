# ЕГЭ по информатике

**Сайт с решениями: [neonco.github.io/EGE2026](https://neonco.github.io/EGE2026/)** (собирается автоматически через GitHub Actions).

Решения задач на Python (а также таблицами и скриншотами).

Задачи именуются номерами из банка задач с сайта Алексея Кабанова — [kompege.ru/task](https://kompege.ru/task). Все варианты сопоставлены с банком: каждое решение лежит в `kompege/zadachi_po_nomeru/taskN/` под своим ID kompege.

## Архитектура

Пайплайн «решения → `site/index.html` → GitHub Pages» как интерактивная карта (сгенерирована через [Archify](https://github.com/tt-a1i/archify)):

- **Карта:** [neonco.github.io/EGE2026/architecture.html](https://neonco.github.io/EGE2026/architecture.html)
- **Источник (typed JSON IR):** [`archify-architecture.json`](archify-architecture.json)

Пересборка карты после правок диаграммы:

```bash
npx skills add tt-a1i/archify -g   # один раз
node ~/.agents/skills/archify/bin/archify.mjs deliver architecture \
  archify-architecture.json site/architecture.html --quality showcase
```


## Решения по номерам

ID ведёт на задачу на kompege, `py` — на файл решения.

<details><summary><b>Задание 2</b></summary>

- [20569](https://kompege.ru/task?id=20569) — [py](kompege/zadachi_po_nomeru/task2/20569.py)
- [23548](https://kompege.ru/task?id=23548) — [py](kompege/zadachi_po_nomeru/task2/23548.py)
- [23739](https://kompege.ru/task?id=23739) — [py](kompege/zadachi_po_nomeru/task2/23739.py)
- [24099](https://kompege.ru/task?id=24099) — [py](kompege/zadachi_po_nomeru/task2/24099.py)
- [25341](https://kompege.ru/task?id=25341) — [py](kompege/zadachi_po_nomeru/task2/25341.py)
- [26059](https://kompege.ru/task?id=26059) — [py](kompege/zadachi_po_nomeru/task2/26059.py)
- [27020](https://kompege.ru/task?id=27020) — [py](kompege/zadachi_po_nomeru/task2/27020.py)
- [27898](https://kompege.ru/task?id=27898) — [py](kompege/zadachi_po_nomeru/task2/27898.py)
- [28750](https://kompege.ru/task?id=28750) — [py](kompege/zadachi_po_nomeru/task2/28750.py)
- [29438](https://kompege.ru/task?id=29438) — [py](kompege/zadachi_po_nomeru/task2/29438.py)
- [29736](https://kompege.ru/task?id=29736) — [py](kompege/zadachi_po_nomeru/task2/29736.py)
- [31210](https://kompege.ru/task?id=31210) — [py](kompege/zadachi_po_nomeru/task2/31210.py)

</details>

<details><summary><b>Задание 5</b></summary>

- [20330](https://kompege.ru/task?id=20330) — [py](kompege/zadachi_po_nomeru/task5/20330.py)
- [21891](https://kompege.ru/task?id=21891) — [py](kompege/zadachi_po_nomeru/task5/21891.py)
- [24100](https://kompege.ru/task?id=24100) — [py](kompege/zadachi_po_nomeru/task5/24100.py)
- [24302](https://kompege.ru/task?id=24302) — [py](kompege/zadachi_po_nomeru/task5/24302.py)
- [26061](https://kompege.ru/task?id=26061) — [py](kompege/zadachi_po_nomeru/task5/26061.py)
- [26353](https://kompege.ru/task?id=26353) — [py](kompege/zadachi_po_nomeru/task5/26353.py)
- [27023](https://kompege.ru/task?id=27023) — [py](kompege/zadachi_po_nomeru/task5/27023.py)
- [27760](https://kompege.ru/task?id=27760) — [py](kompege/zadachi_po_nomeru/task5/27760.py)
- [27908](https://kompege.ru/task?id=27908) — [py](kompege/zadachi_po_nomeru/task5/27908.py)
- [29441](https://kompege.ru/task?id=29441) — [py](kompege/zadachi_po_nomeru/task5/29441.py)
- [29731](https://kompege.ru/task?id=29731) — [py](kompege/zadachi_po_nomeru/task5/29731.py)
- [29786](https://kompege.ru/task?id=29786) — [py](kompege/zadachi_po_nomeru/task5/29786.py)
- [29956](https://kompege.ru/task?id=29956) — [py](kompege/zadachi_po_nomeru/task5/29956.py)

</details>

<details><summary><b>Задание 7</b></summary>

- [27025](https://kompege.ru/task?id=27025) — [py](kompege/zadachi_po_nomeru/task7/27025.py)
- [28216](https://kompege.ru/task?id=28216) — [py](kompege/zadachi_po_nomeru/task7/28216.py)
- [28753](https://kompege.ru/task?id=28753) — [py](kompege/zadachi_po_nomeru/task7/28753.py)
- [29443](https://kompege.ru/task?id=29443) — [py](kompege/zadachi_po_nomeru/task7/29443.py)
- [30338](https://kompege.ru/task?id=30338) — [py](kompege/zadachi_po_nomeru/task7/30338.py)

</details>

<details><summary><b>Задание 8</b></summary>

- [23746](https://kompege.ru/task?id=23746) — [py](kompege/zadachi_po_nomeru/task8/23746.py)
- [26356](https://kompege.ru/task?id=26356) — [py](kompege/zadachi_po_nomeru/task8/26356.py)
- [27026](https://kompege.ru/task?id=27026) — [py](kompege/zadachi_po_nomeru/task8/27026.py)
- [27763](https://kompege.ru/task?id=27763) — [py](kompege/zadachi_po_nomeru/task8/27763.py)
- [29444](https://kompege.ru/task?id=29444) — [py](kompege/zadachi_po_nomeru/task8/29444.py)

</details>

<details><summary><b>Задание 9</b></summary>

- [24227](https://kompege.ru/task?id=24227) — [py](kompege/zadachi_po_nomeru/task9/24227.py)
- [24360](https://kompege.ru/task?id=24360) — [py](kompege/zadachi_po_nomeru/task9/24360.py)
- [29962](https://kompege.ru/task?id=29962) — [py](kompege/zadachi_po_nomeru/task9/29962.py)

</details>

<details><summary><b>Задание 12</b></summary>

- [24104](https://kompege.ru/task?id=24104) — [py](kompege/zadachi_po_nomeru/task12/24104.py)
- [25301](https://kompege.ru/task?id=25301) — [py](kompege/zadachi_po_nomeru/task12/25301.py)
- [26021](https://kompege.ru/task?id=26021) — [py](kompege/zadachi_po_nomeru/task12/26021.py)
- [29344](https://kompege.ru/task?id=29344) — [py](kompege/zadachi_po_nomeru/task12/29344.py)

</details>

<details><summary><b>Задание 13</b></summary>

- [22467](https://kompege.ru/task?id=22467) — [py](kompege/zadachi_po_nomeru/task13/22467.py)
- [24971](https://kompege.ru/task?id=24971) — [py](kompege/zadachi_po_nomeru/task13/24971.py)
- [25141](https://kompege.ru/task?id=25141) — [py](kompege/zadachi_po_nomeru/task13/25141.py)
- [25352](https://kompege.ru/task?id=25352) — [py](kompege/zadachi_po_nomeru/task13/25352.py)
- [26282](https://kompege.ru/task?id=26282) — [py](kompege/zadachi_po_nomeru/task13/26282.py)
- [27625](https://kompege.ru/task?id=27625) — [py](kompege/zadachi_po_nomeru/task13/27625.py)
- [28759](https://kompege.ru/task?id=28759) — [py](kompege/zadachi_po_nomeru/task13/28759.py)

</details>

<details><summary><b>Задание 14</b></summary>

- [24048](https://kompege.ru/task?id=24048) — [py](kompege/zadachi_po_nomeru/task14/24048.py)
- [24606](https://kompege.ru/task?id=24606) — [py](kompege/zadachi_po_nomeru/task14/24606.py)
- [24619](https://kompege.ru/task?id=24619) — [py](kompege/zadachi_po_nomeru/task14/24619.py)
- [24629](https://kompege.ru/task?id=24629) — [py](kompege/zadachi_po_nomeru/task14/24629.py)
- [24890](https://kompege.ru/task?id=24890) — [py](kompege/zadachi_po_nomeru/task14/24890.py)
- [27626](https://kompege.ru/task?id=27626) — [py](kompege/zadachi_po_nomeru/task14/27626.py)
- [27769](https://kompege.ru/task?id=27769) — [py](kompege/zadachi_po_nomeru/task14/27769.py)
- [27910](https://kompege.ru/task?id=27910) — [py](kompege/zadachi_po_nomeru/task14/27910.py)
- [28760](https://kompege.ru/task?id=28760) — [py](kompege/zadachi_po_nomeru/task14/28760.py)
- [31222](https://kompege.ru/task?id=31222) — [py](kompege/zadachi_po_nomeru/task14/31222.py)

</details>

<details><summary><b>Задание 15</b></summary>

- [11845](https://kompege.ru/task?id=11845) — [py](kompege/zadachi_po_nomeru/task15/11845.py)
- [18044](https://kompege.ru/task?id=18044) — [py](kompege/zadachi_po_nomeru/task15/18044.py)
- [21503](https://kompege.ru/task?id=21503) — [py](kompege/zadachi_po_nomeru/task15/21503.py)
- [21710](https://kompege.ru/task?id=21710) — [py](kompege/zadachi_po_nomeru/task15/21710.py)
- [23374](https://kompege.ru/task?id=23374) — [py](kompege/zadachi_po_nomeru/task15/23374.py)
- [23755](https://kompege.ru/task?id=23755) — [py](kompege/zadachi_po_nomeru/task15/23755.py)
- [24597](https://kompege.ru/task?id=24597) — [py](kompege/zadachi_po_nomeru/task15/24597.py)
- [24862](https://kompege.ru/task?id=24862) — [py](kompege/zadachi_po_nomeru/task15/24862.py)
- [25184](https://kompege.ru/task?id=25184) — [py](kompege/zadachi_po_nomeru/task15/25184.py)
- [26182](https://kompege.ru/task?id=26182) — [py](kompege/zadachi_po_nomeru/task15/26182.py)
- [26363](https://kompege.ru/task?id=26363) — [py](kompege/zadachi_po_nomeru/task15/26363.py)
- [27627](https://kompege.ru/task?id=27627) — [py](kompege/zadachi_po_nomeru/task15/27627.py)
- [27770](https://kompege.ru/task?id=27770) — [py](kompege/zadachi_po_nomeru/task15/27770.py)
- [27919](https://kompege.ru/task?id=27919) — [py](kompege/zadachi_po_nomeru/task15/27919.py)
- [28793](https://kompege.ru/task?id=28793) — [py](kompege/zadachi_po_nomeru/task15/28793.py)
- [3077](https://kompege.ru/task?id=3077) — [py](kompege/zadachi_po_nomeru/task15/3077.py)
- [6828](https://kompege.ru/task?id=6828) — [py](kompege/zadachi_po_nomeru/task15/6828.py)
- [9370](https://kompege.ru/task?id=9370) — [py](kompege/zadachi_po_nomeru/task15/9370.py)

</details>

<details><summary><b>Задание 16</b></summary>

- [20341](https://kompege.ru/task?id=20341) — [py](kompege/zadachi_po_nomeru/task16/20341.py)
- [21504](https://kompege.ru/task?id=21504) — [py](kompege/zadachi_po_nomeru/task16/21504.py)
- [24114](https://kompege.ru/task?id=24114) — [py](kompege/zadachi_po_nomeru/task16/24114.py)
- [24598](https://kompege.ru/task?id=24598) — [py](kompege/zadachi_po_nomeru/task16/24598.py)
- [24863](https://kompege.ru/task?id=24863) — [py](kompege/zadachi_po_nomeru/task16/24863.py)
- [24891](https://kompege.ru/task?id=24891) — [py](kompege/zadachi_po_nomeru/task16/24891.py)
- [24954](https://kompege.ru/task?id=24954) — [py](kompege/zadachi_po_nomeru/task16/24954.py)
- [25274](https://kompege.ru/task?id=25274) — [py](kompege/zadachi_po_nomeru/task16/25274.py)
- [26364](https://kompege.ru/task?id=26364) — [py](kompege/zadachi_po_nomeru/task16/26364.py)
- [26493](https://kompege.ru/task?id=26493) — [py](kompege/zadachi_po_nomeru/task16/26493.py)
- [27076](https://kompege.ru/task?id=27076) — [py](kompege/zadachi_po_nomeru/task16/27076.py)
- [27628](https://kompege.ru/task?id=27628) — [py](kompege/zadachi_po_nomeru/task16/27628.py)
- [27771](https://kompege.ru/task?id=27771) — [py](kompege/zadachi_po_nomeru/task16/27771.py)
- [27921](https://kompege.ru/task?id=27921) — [py](kompege/zadachi_po_nomeru/task16/27921.py)
- [28761](https://kompege.ru/task?id=28761) — [py](kompege/zadachi_po_nomeru/task16/28761.py)
- [28794](https://kompege.ru/task?id=28794) — [py](kompege/zadachi_po_nomeru/task16/28794.py)
- [29348](https://kompege.ru/task?id=29348) — [py](kompege/zadachi_po_nomeru/task16/29348.py)
- [29452](https://kompege.ru/task?id=29452) — [py](kompege/zadachi_po_nomeru/task16/29452.py)
- [29970](https://kompege.ru/task?id=29970) — [py](kompege/zadachi_po_nomeru/task16/29970.py)
- [29978](https://kompege.ru/task?id=29978) — [py](kompege/zadachi_po_nomeru/task16/29978.py)
- [9371](https://kompege.ru/task?id=9371) — [py](kompege/zadachi_po_nomeru/task16/9371.py)

</details>

<details><summary><b>Задание 17</b></summary>

- [20342](https://kompege.ru/task?id=20342) — [py](kompege/zadachi_po_nomeru/task17/20342.py)
- [21416](https://kompege.ru/task?id=21416) — [py](kompege/zadachi_po_nomeru/task17/21416.py)
- [21505](https://kompege.ru/task?id=21505) — [py](kompege/zadachi_po_nomeru/task17/21505.py)
- [23563](https://kompege.ru/task?id=23563) — [py](kompege/zadachi_po_nomeru/task17/23563.py)
- [23901](https://kompege.ru/task?id=23901) — [py](kompege/zadachi_po_nomeru/task17/23901.py)
- [24892](https://kompege.ru/task?id=24892) — [py](kompege/zadachi_po_nomeru/task17/24892.py)
- [25185](https://kompege.ru/task?id=25185) — [py](kompege/zadachi_po_nomeru/task17/25185.py)
- [25356](https://kompege.ru/task?id=25356) — [py](kompege/zadachi_po_nomeru/task17/25356.py)
- [27629](https://kompege.ru/task?id=27629) — [py](kompege/zadachi_po_nomeru/task17/27629.py)
- [28762](https://kompege.ru/task?id=28762) — [py](kompege/zadachi_po_nomeru/task17/28762.py)

</details>

<details><summary><b>Задание 19–21</b></summary>

- [11282](https://kompege.ru/task?id=11282) — [py](kompege/zadachi_po_nomeru/task192021/11282.py)
- [17532](https://kompege.ru/task?id=17532) — [py](kompege/zadachi_po_nomeru/task192021/17532.py)
- [22066](https://kompege.ru/task?id=22066) — [py](kompege/zadachi_po_nomeru/task192021/22066.py)
- [23329](https://kompege.ru/task?id=23329) — [py](kompege/zadachi_po_nomeru/task192021/23329.py)
- [23337](https://kompege.ru/task?id=23337) — [py](kompege/zadachi_po_nomeru/task192021/23337.py)
- [2369](https://kompege.ru/task?id=2369) — [py](kompege/zadachi_po_nomeru/task192021/2369.py)
- [3740](https://kompege.ru/task?id=3740) — [py](kompege/zadachi_po_nomeru/task192021/3740.py)

</details>

<details><summary><b>Задание 23</b></summary>

- [20346](https://kompege.ru/task?id=20346) — [py](kompege/zadachi_po_nomeru/task23/20346.py)
- [21510](https://kompege.ru/task?id=21510) — [py](kompege/zadachi_po_nomeru/task23/21510.py)
- [24076](https://kompege.ru/task?id=24076) — [py](kompege/zadachi_po_nomeru/task23/24076.py)
- [24083](https://kompege.ru/task?id=24083) — [py](kompege/zadachi_po_nomeru/task23/24083.py)
- [24602](https://kompege.ru/task?id=24602) — [py](kompege/zadachi_po_nomeru/task23/24602.py)
- [24867](https://kompege.ru/task?id=24867) — [py](kompege/zadachi_po_nomeru/task23/24867.py)
- [24928](https://kompege.ru/task?id=24928) — [py](kompege/zadachi_po_nomeru/task23/24928.py)
- [26366](https://kompege.ru/task?id=26366) — [py](kompege/zadachi_po_nomeru/task23/26366.py)
- [27912](https://kompege.ru/task?id=27912) — [py](kompege/zadachi_po_nomeru/task23/27912.py)
- [28764](https://kompege.ru/task?id=28764) — [py](kompege/zadachi_po_nomeru/task23/28764.py)
- [29457](https://kompege.ru/task?id=29457) — [py](kompege/zadachi_po_nomeru/task23/29457.py)
- [29977](https://kompege.ru/task?id=29977) — [py](kompege/zadachi_po_nomeru/task23/29977.py)
- [30471](https://kompege.ru/task?id=30471) — [py](kompege/zadachi_po_nomeru/task23/30471.py)
- [31229](https://kompege.ru/task?id=31229) — [py](kompege/zadachi_po_nomeru/task23/31229.py)

</details>

<details><summary><b>Задание 24</b></summary>

- [13570](https://kompege.ru/task?id=13570) — [py](kompege/zadachi_po_nomeru/task24/13570.py)
- [17685](https://kompege.ru/task?id=17685) — [py](kompege/zadachi_po_nomeru/task24/17685.py)
- [19254](https://kompege.ru/task?id=19254) — [py](kompege/zadachi_po_nomeru/task24/19254.py)
- [19719](https://kompege.ru/task?id=19719) — [py](kompege/zadachi_po_nomeru/task24/19719.py)
- [20347](https://kompege.ru/task?id=20347) — [py](kompege/zadachi_po_nomeru/task24/20347.py)
- [21509](https://kompege.ru/task?id=21509) — [py](kompege/zadachi_po_nomeru/task24/21509.py)
- [22362](https://kompege.ru/task?id=22362) — [py](kompege/zadachi_po_nomeru/task24/22362.py)
- [23568](https://kompege.ru/task?id=23568) — [py](kompege/zadachi_po_nomeru/task24/23568.py)
- [23762](https://kompege.ru/task?id=23762) — [py](kompege/zadachi_po_nomeru/task24/23762.py)
- [24240](https://kompege.ru/task?id=24240) — [py](kompege/zadachi_po_nomeru/task24/24240.py)
- [24603](https://kompege.ru/task?id=24603) — [py](kompege/zadachi_po_nomeru/task24/24603.py)
- [24868](https://kompege.ru/task?id=24868) — [py](kompege/zadachi_po_nomeru/task24/24868.py)
- [24895](https://kompege.ru/task?id=24895) — [py](kompege/zadachi_po_nomeru/task24/24895.py)
- [24977](https://kompege.ru/task?id=24977) — [py](kompege/zadachi_po_nomeru/task24/24977.py)
- [25335](https://kompege.ru/task?id=25335) — [py](kompege/zadachi_po_nomeru/task24/25335.py)
- [25361](https://kompege.ru/task?id=25361) — [py](kompege/zadachi_po_nomeru/task24/25361.py)
- [25974](https://kompege.ru/task?id=25974) — [py](kompege/zadachi_po_nomeru/task24/25974.py)
- [26074](https://kompege.ru/task?id=26074) — [py](kompege/zadachi_po_nomeru/task24/26074.py)
- [26078](https://kompege.ru/task?id=26078) — [py](kompege/zadachi_po_nomeru/task24/26078.py)
- [26114](https://kompege.ru/task?id=26114) — [py](kompege/zadachi_po_nomeru/task24/26114.py)
- [26298](https://kompege.ru/task?id=26298) — [py](kompege/zadachi_po_nomeru/task24/26298.py)
- [26549](https://kompege.ru/task?id=26549) — [py](kompege/zadachi_po_nomeru/task24/26549.py)
- [27777](https://kompege.ru/task?id=27777) — [py](kompege/zadachi_po_nomeru/task24/27777.py)
- [27897](https://kompege.ru/task?id=27897) — [py](kompege/zadachi_po_nomeru/task24/27897.py)
- [28006](https://kompege.ru/task?id=28006) — [py](kompege/zadachi_po_nomeru/task24/28006.py)
- [28007](https://kompege.ru/task?id=28007) — [py](kompege/zadachi_po_nomeru/task24/28007.py)
- [28396](https://kompege.ru/task?id=28396) — [py](kompege/zadachi_po_nomeru/task24/28396.py)
- [28765](https://kompege.ru/task?id=28765) — [py](kompege/zadachi_po_nomeru/task24/28765.py)
- [28799](https://kompege.ru/task?id=28799) — [py](kompege/zadachi_po_nomeru/task24/28799.py)
- [28943](https://kompege.ru/task?id=28943) — [py](kompege/zadachi_po_nomeru/task24/28943.py)
- [29354](https://kompege.ru/task?id=29354) — [py](kompege/zadachi_po_nomeru/task24/29354.py)
- [29803](https://kompege.ru/task?id=29803) — [py](kompege/zadachi_po_nomeru/task24/29803.py)
- [29922](https://kompege.ru/task?id=29922) — [py](kompege/zadachi_po_nomeru/task24/29922.py)
- [5139](https://kompege.ru/task?id=5139) — [py](kompege/zadachi_po_nomeru/task24/5139.py)
- [5381](https://kompege.ru/task?id=5381) — [py](kompege/zadachi_po_nomeru/task24/5381.py)
- [6094](https://kompege.ru/task?id=6094) — [py](kompege/zadachi_po_nomeru/task24/6094.py)
- [9471](https://kompege.ru/task?id=9471) — [py](kompege/zadachi_po_nomeru/task24/9471.py)

</details>

<details><summary><b>Задание 25</b></summary>

- [11470](https://kompege.ru/task?id=11470) — [py](kompege/zadachi_po_nomeru/task25/11470.py)
- [17686](https://kompege.ru/task?id=17686) — [py](kompege/zadachi_po_nomeru/task25/17686.py)
- [20348](https://kompege.ru/task?id=20348) — [py](kompege/zadachi_po_nomeru/task25/20348.py)
- [21511](https://kompege.ru/task?id=21511) — [py](kompege/zadachi_po_nomeru/task25/21511.py)
- [24166](https://kompege.ru/task?id=24166) — [py](kompege/zadachi_po_nomeru/task25/24166.py)
- [24331](https://kompege.ru/task?id=24331) — [py](kompege/zadachi_po_nomeru/task25/24331.py)
- [24385](https://kompege.ru/task?id=24385) — [py](kompege/zadachi_po_nomeru/task25/24385.py)
- [24604](https://kompege.ru/task?id=24604) — [py](kompege/zadachi_po_nomeru/task25/24604.py)
- [24869](https://kompege.ru/task?id=24869) — [py](kompege/zadachi_po_nomeru/task25/24869.py)
- [24896](https://kompege.ru/task?id=24896) — [py](kompege/zadachi_po_nomeru/task25/24896.py)
- [26127](https://kompege.ru/task?id=26127) — [py](kompege/zadachi_po_nomeru/task25/26127.py)
- [26302](https://kompege.ru/task?id=26302) — [py](kompege/zadachi_po_nomeru/task25/26302.py)
- [26557](https://kompege.ru/task?id=26557) — [py](kompege/zadachi_po_nomeru/task25/26557.py)
- [26687](https://kompege.ru/task?id=26687) — [py](kompege/zadachi_po_nomeru/task25/26687.py)
- [27499](https://kompege.ru/task?id=27499) — [py](kompege/zadachi_po_nomeru/task25/27499.py)
- [27778](https://kompege.ru/task?id=27778) — [py](kompege/zadachi_po_nomeru/task25/27778.py)
- [27900](https://kompege.ru/task?id=27900) — [py](kompege/zadachi_po_nomeru/task25/27900.py)

</details>

<details><summary><b>Задание 26</b></summary>

- [13394](https://kompege.ru/task?id=13394) — [py](kompege/zadachi_po_nomeru/task26/13394.py)
- [17643](https://kompege.ru/task?id=17643) — [py](kompege/zadachi_po_nomeru/task26/17643.py)
- [21424](https://kompege.ru/task?id=21424) — [py](kompege/zadachi_po_nomeru/task26/21424.py)
- [21512](https://kompege.ru/task?id=21512) — [py](kompege/zadachi_po_nomeru/task26/21512.py)
- [22168](https://kompege.ru/task?id=22168) — [py](kompege/zadachi_po_nomeru/task26/22168.py)
- [23208](https://kompege.ru/task?id=23208) — [py](kompege/zadachi_po_nomeru/task26/23208.py)
- [23765](https://kompege.ru/task?id=23765) — [py](kompege/zadachi_po_nomeru/task26/23765.py)
- [23786](https://kompege.ru/task?id=23786) — [py](kompege/zadachi_po_nomeru/task26/23786.py)
- [23977](https://kompege.ru/task?id=23977) — [py](kompege/zadachi_po_nomeru/task26/23977.py)
- [24098](https://kompege.ru/task?id=24098) — [py](kompege/zadachi_po_nomeru/task26/24098.py)
- [24870](https://kompege.ru/task?id=24870) — [py](kompege/zadachi_po_nomeru/task26/24870.py)
- [25337](https://kompege.ru/task?id=25337) — [py](kompege/zadachi_po_nomeru/task26/25337.py)
- [25363](https://kompege.ru/task?id=25363) — [py](kompege/zadachi_po_nomeru/task26/25363.py)
- [25957](https://kompege.ru/task?id=25957) — [py](kompege/zadachi_po_nomeru/task26/25957.py)
- [26027](https://kompege.ru/task?id=26027) — [py](kompege/zadachi_po_nomeru/task26/26027.py)
- [2653](https://kompege.ru/task?id=2653) — [py](kompege/zadachi_po_nomeru/task26/2653.py)
- [27913](https://kompege.ru/task?id=27913) — [py](kompege/zadachi_po_nomeru/task26/27913.py)
- [28801](https://kompege.ru/task?id=28801) — [py](kompege/zadachi_po_nomeru/task26/28801.py)
- [29805](https://kompege.ru/task?id=29805) — [py](kompege/zadachi_po_nomeru/task26/29805.py)
- [6759](https://kompege.ru/task?id=6759) — [py](kompege/zadachi_po_nomeru/task26/6759.py)

</details>

<details><summary><b>Задание 27</b></summary>

- [18678 часть A](https://kompege.ru/task?id=18678) — [py](kompege/zadachi_po_nomeru/task27/18678/27_A_18678.py), [данные](kompege/zadachi_po_nomeru/task27/18678/)
- [25300 часть A](https://kompege.ru/task?id=25300) — [py](kompege/zadachi_po_nomeru/task27/25300/27_A_25300.py), [данные](kompege/zadachi_po_nomeru/task27/25300/)
- [25364 часть A](https://kompege.ru/task?id=25364) — [py](kompege/zadachi_po_nomeru/task27/25364/27_A_25364.py), [данные](kompege/zadachi_po_nomeru/task27/25364/)
- [26304 часть A](https://kompege.ru/task?id=26304) — [py](kompege/zadachi_po_nomeru/task27/26304/27_A_26304.py), [данные](kompege/zadachi_po_nomeru/task27/26304/)
- [27035 часть A](https://kompege.ru/task?id=27035) — [py](kompege/zadachi_po_nomeru/task27/27035/27_A_27035.py), [данные](kompege/zadachi_po_nomeru/task27/27035/)
- [27637 часть A](https://kompege.ru/task?id=27637) — [py](kompege/zadachi_po_nomeru/task27/27637/27_A_27637.py), [данные](kompege/zadachi_po_nomeru/task27/27637/)
- [27801 часть A](https://kompege.ru/task?id=27801) — [py](kompege/zadachi_po_nomeru/task27/27801/27_A_27801.py), [данные](kompege/zadachi_po_nomeru/task27/27801/)
- [28766 часть A](https://kompege.ru/task?id=28766) — [py](kompege/zadachi_po_nomeru/task27/28766/27_A_28766.py), [данные](kompege/zadachi_po_nomeru/task27/28766/)
- [29979 часть A](https://kompege.ru/task?id=29979) — [py](kompege/zadachi_po_nomeru/task27/29979/27_A_29979.py), [данные](kompege/zadachi_po_nomeru/task27/29979/)
- [30475 часть A](https://kompege.ru/task?id=30475) — [py](kompege/zadachi_po_nomeru/task27/30475/27_A_30475.py), [данные](kompege/zadachi_po_nomeru/task27/30475/)
- [18678 часть B](https://kompege.ru/task?id=18678) — [py](kompege/zadachi_po_nomeru/task27/18678/27_B_18678.py), [данные](kompege/zadachi_po_nomeru/task27/18678/)
- [25300 часть B](https://kompege.ru/task?id=25300) — [py](kompege/zadachi_po_nomeru/task27/25300/27_B_25300.py), [данные](kompege/zadachi_po_nomeru/task27/25300/)
- [25364 часть B](https://kompege.ru/task?id=25364) — [py](kompege/zadachi_po_nomeru/task27/25364/27_B_25364.py), [данные](kompege/zadachi_po_nomeru/task27/25364/)
- [26304 часть B](https://kompege.ru/task?id=26304) — [py](kompege/zadachi_po_nomeru/task27/26304/27_B_26304.py), [данные](kompege/zadachi_po_nomeru/task27/26304/)
- [26522 часть B](https://kompege.ru/task?id=26522) — [py](kompege/zadachi_po_nomeru/task27/26522/27_B_26522.py), [данные](kompege/zadachi_po_nomeru/task27/26522/)
- [27035 часть B](https://kompege.ru/task?id=27035) — [py](kompege/zadachi_po_nomeru/task27/27035/27_B_27035.py), [данные](kompege/zadachi_po_nomeru/task27/27035/)
- [27637 часть B](https://kompege.ru/task?id=27637) — [py](kompege/zadachi_po_nomeru/task27/27637/27_B_27637.py), [данные](kompege/zadachi_po_nomeru/task27/27637/)
- [27801 часть B](https://kompege.ru/task?id=27801) — [py](kompege/zadachi_po_nomeru/task27/27801/27_B_27801.py), [данные](kompege/zadachi_po_nomeru/task27/27801/)
- [28766 часть B](https://kompege.ru/task?id=28766) — [py](kompege/zadachi_po_nomeru/task27/28766/27_B_28766.py), [данные](kompege/zadachi_po_nomeru/task27/28766/)
- [29979 часть B](https://kompege.ru/task?id=29979) — [py](kompege/zadachi_po_nomeru/task27/29979/27_B_29979.py), [данные](kompege/zadachi_po_nomeru/task27/29979/)
- [30475 часть B](https://kompege.ru/task?id=30475) — [py](kompege/zadachi_po_nomeru/task27/30475/27_B_30475.py), [данные](kompege/zadachi_po_nomeru/task27/30475/)

</details>


## Варианты

Варианты сгруппированы по учебным годам: `kompege/2025-2026/<Автор_N>/` (прошлый год) и `kompege/2026-2027/<Автор_N>/` (текущий год). Сопоставление с банком выполнено по kim-номерам вариантов с [kompege.ru/archive](https://kompege.ru/archive) (47 контрольных якорей, расхождений 0).

### 2025–2026

| Папка | Вариант на kompege |
|-------|--------------------|
| `2025-2026/aprobation_04_03_2026_var1` | [Апробация 04.03.26](https://kompege.ru/variant?kim=25163454) |
| `2025-2026/aprobation_04_03_2026_var2` | [Апробация 04.03.26 II](https://kompege.ru/variant?kim=25164989) |
| `2025-2026/aprobation_14_05_2026` | [Апробация 14.05.26](https://kompege.ru/variant?kim=25192097) |
| `2025-2026/ARogov_1` | [Вариант 1.2025](https://kompege.ru/variant?kim=25138308) |
| `2025-2026/ARogov_10` | [Вариант 10.2025 Антишаблонный](https://kompege.ru/variant?kim=25140445) |
| `2025-2026/ARogov_2` | [Вариант 2.2025](https://kompege.ru/variant?kim=25138309) |
| `2025-2026/ARogov_3` | [Вариант 3.2025](https://kompege.ru/variant?kim=25138311) |
| `2025-2026/ARogov_5` | [Вариант 5.2025](https://kompege.ru/variant?kim=25138313) |
| `2025-2026/ARogov_6` | [Вариант 6.2025](https://kompege.ru/variant?kim=25138319) |
| `2025-2026/DByte_1` | [—](https://kompege.ru/variant?kim=25109507) |
| `2025-2026/DByte_2` | [—](https://kompege.ru/variant?kim=25115343) |
| `2025-2026/DByte_3` | [—](https://kompege.ru/variant?kim=25124397) |
| `2025-2026/DByte_4` | [—](https://kompege.ru/variant?kim=25135264) |
| `2025-2026/DByte_5` | [—](https://kompege.ru/variant?kim=25143077) |
| `2025-2026/DByte_6` | [—](https://kompege.ru/variant?kim=25154203) |
| `2025-2026/DByte_7` | [—](https://kompege.ru/variant?kim=25167515) |
| `2025-2026/DByte_8` | [—](https://kompege.ru/variant?kim=25177298) |
| `2025-2026/DByte_9` | [—](https://kompege.ru/variant?kim=25189996) |
| `2025-2026/dosrok2026` | [Досрочная волна 2026](https://kompege.ru/variant?kim=25177268) |
| `2025-2026/LShastin_DBahtiev_1` | [В1Г2526](https://kompege.ru/variant?kim=25112400) |
| `2025-2026/LShastin_DBahtiev_10` | [В10Г2526](https://kompege.ru/variant?kim=25183809) |
| `2025-2026/LShastin_DBahtiev_14` | [В14Г2526](https://kompege.ru/variant?kim=25198084) |
| `2025-2026/LShastin_DBahtiev_4` | [Вариант №4 (256)](https://kompege.ru/variant?kim=25141693) |
| `2025-2026/LShastin_DBahtiev_7` | [В7Г2526](https://kompege.ru/variant?kim=25165560) |
| `2025-2026/LShastin_DBahtiev_8` | [Вариант №8 (258)](https://kompege.ru/variant?kim=25145224) |
| `2025-2026/MMigunov` | [Вариант №1](https://kompege.ru/variant?kim=25106570) |
| `2025-2026/rezerv_26_06_2026` | [Резерв 22.06.26](https://kompege.ru/variant?kim=25203502) |
| `2025-2026/SGorbachev_1` | [Сергей Горбачев #1](https://kompege.ru/variant?kim=25111879) |
| `2025-2026/SGorbachev_2` | [Сергей Горбачев #2](https://kompege.ru/variant?kim=25121111) |
| `2025-2026/SGorbachev_3` | [Сергей Горбачев #3](https://kompege.ru/variant?kim=25196800) |
| `2025-2026/SSergeev_MVardoev_3` | [—](https://kompege.ru/variant?kim=25134173) |
| `2025-2026/SSergeev_MVardoev_4` | [вар 4](https://kompege.ru/variant?kim=25142942) |
| `2025-2026/TNikitin` | [—](https://kompege.ru/variant?kim=25186594) |
| `2025-2026/VLashin_KIglin_6` | [вариант 6](https://kompege.ru/variant?kim=25147031) |
| `2025-2026/VLashin_KIglin_8` | [8 вариант](https://kompege.ru/variant?kim=25167211) |

### 2026–2027

Пусто — ждём первых вариантов нового учебного года.
