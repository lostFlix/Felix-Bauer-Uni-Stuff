# Data Analysis with Python – HS26 (UZH, 22BO0143)

Meine Übungen für das Seminar bei Justinas Grigaitis. **Diese Datei ist die Startseite.**

## Öffnen
In VS Code: *Datei → Arbeitsbereich aus Datei öffnen* →
`~/Documents/UZH_HS26/07_Python/Python_HS26.code-workspace`
Oder im Terminal: `code ~/Documents/UZH_HS26/07_Python/Python_HS26.code-workspace`

Links in der Seitenleiste erscheinen dann drei Ordner:

| Ordner | Was drin ist | Regel |
|---|---|---|
| 1 · Meine Übungen | dieses Repo, alles, was ich selbst schreibe | hier arbeiten, committen, pushen |
| 2 · Kurs-Repo Grigaitis | Folien, Homework, Daten vom Kurs | **nicht drin arbeiten**, nur `git pull` |
| 3 · Folien & Notizen | OLAT-PDFs und Markdown-Versionen | nur lesen |

Will ich eine Kurs-Übung bearbeiten: Datei aus Ordner 2 **kopieren** nach `weekN/` hier, dann in der Kopie arbeiten.

## Struktur hier
- `week1_session/` – Notebooks aus der ersten Session (gerettet aus `~/Documents/UZH/ba-programming-2026`)
- `i feel so stupid.ipynb` – erste Übungen Week 1
- `week2_mosh/` – Übungen zum Mosh-Video (28.09.)

## Links
- OLAT-Kurs: https://lms.uzh.ch/url/RepositoryEntry/17903616125
- Kurs-Repo: https://github.com/justgri/ba-programming-2026
- Week 2 Homework: https://github.com/justgri/ba-programming-2026/tree/main/sessions/week_2/homework
- Mosh, Python Full Course for Beginners: https://www.youtube.com/watch?v=K5KVEU3aaeQ
- TA Gustav Pirich (bei Fragen): gustav.pirich@econ.uzh.ch

## Wöchentlicher Ablauf
1. Kurs-Repo aktualisieren: im Terminal von Ordner 2 `git pull`
2. Homework kopieren, hier bearbeiten
3. Speichern auf GitHub:
   ```
   git add .
   git commit -m "Week N: was ich gemacht habe"
   git push
   ```
4. **Assessment in OLAT**: zuerst die Aufgabe per „Auswählen“ übernehmen, dann 3–5 Bullet Points plus Link zu diesem Repo abgeben. Frist jeweils **Donnerstag 12:00**.

## Termine
- **15.10.** Quiz (Code verstehen, ein paar Aufgaben von Hand schreiben). Alter Quiz: `python_quiz_2025.pdf` (Mail vom 25.09. im UZH-Postfach)
- **04.12.** Final-Project-Präsentation, KOL-H-309
- **11.12., 12:00** Projektbericht auf OLAT

Python: `/usr/local/bin/python3` (3.14) mit pandas, numpy, matplotlib, streamlit, requests, ipykernel.
