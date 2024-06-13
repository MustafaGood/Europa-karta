import folium
from folium.plugins import MarkerCluster
import pandas as pd
import random
import tkinter as tk
from tkinter import simpledialog, messagebox
import webbrowser
import os

# Utökad data för europeiska länder och deras huvudstäder
data = {
    'Land': ['Sverige', 'Tyskland', 'Frankrike', 'Spanien', 'Italien', 'Polen', 'Portugal', 'Grekland', 'Finland', 'Norge', 
             'Irland', 'Tjeckien', 'Ungern', 'Belgien', 'Schweiz', 'Nederländerna', 'Luxemburg', 'Danmark', 
             'Österrike', 'Bulgarien', 'Slovakien', 'Slovenien', 'Estland', 'Lettland', 'Litauen', 'Kroatien', 'Bosnien och Hercegovina',
             'Serbien', 'Montenegro', 'Nordmakedonien', 'Albanien', 'Rumänien', 'Ukraina', 'Vitryssland', 'Moldavien', 'Ryssland',
             'Storbritannien', 'Island', 'Malta', 'Cypern', 'Turkiet', 'Kosovo', 'Andorra', 'Monaco', 'Liechtenstein', 
             'San Marino', 'Vatikanstaten'],
    'Huvudstad': ['Stockholm', 'Berlin', 'Paris', 'Madrid', 'Rom', 'Warszawa', 'Lissabon', 'Aten', 'Helsingfors', 'Oslo', 
                  'Dublin', 'Prag', 'Budapest', 'Bryssel', 'Bern', 'Amsterdam', 'Luxemburg', 'Köpenhamn', 
                  'Wien', 'Sofia', 'Bratislava', 'Ljubljana', 'Tallinn', 'Riga', 'Vilnius', 'Zagreb', 'Sarajevo',
                  'Belgrad', 'Podgorica', 'Skopje', 'Tirana', 'Bukarest', 'Kyiv', 'Minsk', 'Chișinău', 'Moskva',
                  'London', 'Reykjavik', 'Valletta', 'Nicosia', 'Ankara', 'Pristina', 'Andorra la Vella', 'Monaco', 
                  'Vaduz', 'San Marino', 'Vatikanstaten'],
    'Latitud': [59.3293, 52.5200, 48.8566, 40.4168, 41.9028, 52.2297, 38.7223, 37.9838, 60.1699, 59.9139, 
                53.3498, 50.0755, 47.4979, 50.8503, 46.9480, 52.3676, 49.6116, 55.6761, 
                48.2082, 42.6977, 48.1486, 46.0569, 59.4370, 56.9496, 54.6872, 45.8150, 43.8563,
                44.7866, 42.4304, 41.9973, 41.3275, 44.4268, 50.4501, 53.9045, 47.4116, 55.7558,
                51.5074, 64.1466, 35.8989, 35.1856, 39.9334, 42.6629, 42.5063, 43.7384, 
                47.1410, 43.9424, 41.9029],
    'Longitud': [18.0686, 13.4050, 2.3522, -3.7038, 12.4964, 21.0122, -9.1393, 23.7275, 24.9384, 10.7522, 
                 -6.2603, 14.4378, 19.0402, 4.3517, 7.4474, 4.9041, 6.1296, 12.5683, 
                 16.3738, 23.3219, 17.1077, 14.5058, 24.7536, 24.1052, 25.2797, 15.9819, 18.4130,
                 20.4489, 19.2621, 21.4331, 19.8187, 26.1025, 30.5234, 27.5667, 28.8469, 37.6173,
                 -0.1278, -21.9426, 14.5146, 33.3823, 32.8597, 21.1669, 1.5218, 7.4246,
                 9.5167, 12.4418, 12.4534]
}

df = pd.DataFrame(data)

# Funktion för att skapa en karta
def skapa_karta():
    # Skapa en karta med centrum över Europa
    europa_karta = folium.Map(location=[54.5260, 15.2551], zoom_start=4)
    marker_cluster = MarkerCluster().add_to(europa_karta)
    
    # Lägg till markörer för varje huvudstad
    for idx, row in df.iterrows():
        folium.Marker(location=[row['Latitud'], row['Longitud']], 
                      popup=f"{row['Huvudstad']}, {row['Land']}",
                      icon=folium.Icon(icon='info-sign')).add_to(marker_cluster)
    
    # Spara kartan till en HTML-fil
    karta_fil = 'europa_karta.html'
    europa_karta.save(karta_fil)
    
    # Öppna kartan i webbläsaren
    webbrowser.open('file://' + os.path.realpath(karta_fil))

# Funktion för att ställa frågor
def ställ_fråga():
    # Välj en slumpmässig huvudstad
    idx = random.randint(0, len(df) - 1)
    huvudstad = df.iloc[idx]['Huvudstad']
    land = df.iloc[idx]['Land']

    # Ställ frågan
    fråga = f"Vilket land är {huvudstad} huvudstad i?"
    svar = simpledialog.askstring("Fråga", fråga)
    
    if svar:
        # Kontrollera svaret
        if svar.lower() == land.lower():
            messagebox.showinfo("Svar", "Rätt!")
        else:
            messagebox.showinfo("Svar", f"Fel! Det rätta svaret är {land}.")
    
    # Fortsätt ställa frågor
    ställ_fråga()

# Huvudprogram
def starta_program():
    skapa_karta()
    ställ_fråga()

# Skapa huvudfönstret
root = tk.Tk()
root.title("Europeisk Huvudstadsquiz")

# Skapa en startknapp
start_knapp = tk.Button(root, text="Starta Quiz", command=starta_program)
start_knapp.pack(pady=20)

# Kör huvudloopen
root.mainloop()
