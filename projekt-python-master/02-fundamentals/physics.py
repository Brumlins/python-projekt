'''
Konstanty v Pythonu

Konstanta je vlastně speciální typ proměnné, jejíž hodnota nemůže být změněna.
V Pythonu jsou konstanty obvykle deklarovány a přiřazovány v modulu, který bývá importován do souboru aplikace.
Konstanty jsou pojmenovány velkými písmeny a jednotlivá slova jsou oddělována podtržítky.
'''

# normální gravitační zrychlení na zemi (m/s²)
earth_gravity = 9.81

# gravitační zrychlení na měsíci (m/s²)
moon_gravity = 1.62

# rychlost světla ve vakuu (m/s)
speed_of_light = 299792458

# rychlost zvuku ve vzduchu při 20 °c (m/s)
speed_of_sound = 343

''' 
Úkol:
1. Doplňte správně hodnoty uvedených konstant.
2. Doplňte physics.py o několik výpočtových funkcí (opatřené docstrings), v nichž využijete minimálně všechny výše uvedené konstanty.
Samozřejmě můžete své řešení rozšířit i o jiné fyzikální konstanty.
3. Vytvořte z tohoto souboru samostatný modul v Pythonu podle návodu, který si sami najdete na internetu.      
4. Vytvořte vlastní aplikaci myapp.py, do níž tento modul importujte. Demonstrujte v ní na jednoduchých příkladech využití vámi
připravených funkcí.  
'''


def calculate_weight_on_earth(mass):
    """
    Vypocita vahu na zemi.

    Parametry:
    mass (float): Hmotnost v kg.

    Navratova hodnota:
    float: Vaha v Newtonach.
    """
    return mass * earth_gravity


def calculate_weight_on_moon(mass):
    """
    Vypocita vahu na mesici.

    Parametry:
    mass (float): Hmotnost v kg.

    Navratova hodnota:
    float: Vaha v Newtonach.
    """
    return mass * moon_gravity


def time_to_fall(height):
    """
    Vypocita cas padu z urcite vysky na zemi.

    Parametry:
    height (float): Vyska v metrech.

    Navratova hodnota:
    float: Cas v sekundach.
    """
    return (2 * height / earth_gravity) ** 0.5


def sound_travel_time(distance):
    """
    Vypocita cas, co zvuk potrebuje na prekrocenie urcite vzdalenosti.

    Parametry:
    distance (float): Vzdalenost v metrech.

    Navratova hodnota:
    float: Cas v sekundach.
    """
    return distance / speed_of_sound
