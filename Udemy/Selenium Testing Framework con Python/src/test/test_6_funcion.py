import re
import datetime

API_hostAddressBase = u'http://Urldelawebapi.com'
partHost = "Endpoint/FECHAS/Scenario:Today"

def get_full_host(_PartHost):
    _RegexPatrHost = ReplaceWithContextValues(_PartHost)
    _endpoint = API_hostAddressBase + '/' + _RegexPatrHost
    print(_endpoint)
    return _endpoint

def ReplaceWithContextValues(text):
    # Patrón para buscar "Scenario:Today"
    PatronDeBusqueda = r"Scenario:Today"
    
    # Si encontramos el patrón, reemplazamos "Today" con la fecha actual
    if re.search(PatronDeBusqueda, text, re.IGNORECASE):
        dateToday = datetime.date.today().strftime("%d-%m-%Y")
        text = re.sub(PatronDeBusqueda, f"Scenario:{dateToday}", text, re.IGNORECASE)
    
    return text

endpoint = get_full_host(partHost)
