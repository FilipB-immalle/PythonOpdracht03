from datetime import datetime, date

def parse_geboortedatum(s):
    """
    een correct geformatteerde datum moet geparset worden
    >>> parse_geboortedatum("2019-10-01")
    datetime.date(2019, 10, 1)

    een foute geboortedatum-string moet de default waarde 2000-01-01 geven
    >>> parse_geboortedatum("bla")
    datetime.date(2000, 1, 1)
    """
    try:
        return datetime.strptime(s, "%Y-%m-%d").date()
    except:
        return date(2000, 1, 1,)

def aantal_waarden(aantal_bits):
    """
    Met 2 bits kunnen we 4 waarden voorstellen
    >>> aantal_waarden(2)
    4
    
    Met 4 bits kunnen we 16 waarden voorstellen
    >>> aantal_waarden(4)
    16
    
    Bij invoer van een ongeldige string moet een exception geworpen worden
    >>> aantal_waarden("bla")
    Traceback (most recent call last):
    ...
    TypeError: unsupported operand type(s) for ** or pow(): 'int' and 'str'
    """
    return 2 ** aantal_bits

def controleer_leeftijd(leeftijd):
    """

    Als de leeftijd tussen 12 en 18 jaar, return True
    >>> controleer_leeftijd(12)
    False

    >>> controleer_leeftijd(13)
    True
    
    >>> controleer_leeftijd(17)
    True
    
    >>> controleer_leeftijd(18)
    False
    """
    if(leeftijd > 12 and leeftijd < 18):
        return True
    else:
        return False

def controleer_stringlengte(str):
    """
    TODO: schrijf zelf de doctests en de implementatie v.d. functie

    >>> controleer_stringlengte("bambi")
    5

    >>> controleer_stringlengte("pok")
    3

    >>> controleer_stringlengte(10)
    Traceback (most recent call last):
    ...
    TypeError: object of type 'int' has no len()

    """
    return len(str)

def maak_groet_boodschap(naam, namenlijst):
    """

    Als naam in namenlijst voorkomt, maak een groet-boodschap
    >>> maak_groet_boodschap("Jos", ["Jos", "Mieke"])
    'Hallo Jos!'

    Als de naam niet voorkomt, is de groet-string
    >>> maak_groet_boodschap("Willy", ["Jos", "Mieke"])
    'Hallo onbekende gebruiker!'

    TODO: voeg nog 2 doctests toe met een andere namenlijst

    >>> maak_groet_boodschap("Jan", ["Jan", "Marie"])
    'Hallo Jan!'

    >>> maak_groet_boodschap("Pieter", ["Pieter", "Chris"])
    'Hallo Pieter!'

    """
    if naam in namenlijst:
        return "Hallo " + naam + "!"
    else:
        return "Hallo onbekende gebruiker!"

def laatste_x_letters(s, x):
    """

    >>> laatste_x_letters("Jos", 3)
    'Jos'

    >>> laatste_x_letters("Willy", 3)
    'lly'

    Als de string korter is dan het gevraagde aantal, toon alles
    >>> laatste_x_letters("Jo", 3)
    'Jo'

    """
    if len(s) < x:
        return s
    else:
        return s[-x:]

def aantal_dagen_in_leven(geboortedatum):
    """

    >>> aantal_dagen_in_leven("2019-10-01")
    24

    Merk op: Je kan hier moeilijk een gepaste test voor schrijven!
    We zouden hier moeten gebruik maken van mock-objecten
    maar dit valt waarschijnlijk buiten de scope van doctest.
    """
    geboortedatum = datetime.strptime(geboortedatum, "%Y-%m-%d")
    return datetime.now().day - geboortedatum.day

if __name__ == "__main__":
    import doctest
    doctest.testmod()