# Europeisk Huvudstadsquiz

Detta projekt är en interaktiv frågesport om europeiska huvudstäder, som använder ett grafiskt användargränssnitt (GUI) skapat med Tkinter och en karta genererad med Folium. Frågesporten ställer frågor om huvudstäder och deras tillhörande länder och visar en karta över Europa med markörer för varje huvudstad.

## Funktioner

- Skapa en interaktiv karta över Europas huvudstäder.
- Ställa slumpmässiga frågor om vilket land en viss huvudstad tillhör.
- Visa rätt eller fel svar till användaren.

## Installation

För att köra detta projekt behöver du ha Python installerat samt några nödvändiga bibliotek. Följ stegen nedan för att installera dem.

### Krav

- Python 3.x
- Folium
- Pandas
- Tkinter (vanligtvis inkluderat med Python)
- webbrowser (vanligtvis inkluderat med Python)
- OS (vanligtvis inkluderat med Python)

### Installationssteg

1. Klona detta repository eller ladda ner ZIP-filen och extrahera den.
2. Navigera till projektmappen.
3. Installera de nödvändiga biblioteken med pip:

pip install folium pandas

## Användning
1. Kör Python-skriptet `ni.py`:
    
    python ni.py
    
2. Ett grafiskt användargränssnitt (GUI) kommer att öppnas. Klicka på "Starta Quiz" för att börja frågesporten.
3. En karta över Europa med markörer för varje huvudstad kommer att öppnas i din webbläsare.
4. Frågor kommer att visas i GUI:t. Skriv in ditt svar och klicka på OK.
5. Ett meddelande kommer att visa om ditt svar är rätt eller fel. Frågesporten fortsätter sedan med nästa fråga.

## Filstruktur

.ni.py                # Huvud-Python-skriptet
europa_karta.html    # HTML-fil som genereras av programmet (skapas vid körning)
README.md            # Denna README-fil
