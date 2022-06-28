import requests


# link do open_weather: https://openweathermap.org/

API_KEY = "33cd546f75aaca6380b481cd5030513e"

#função responsável por pegar as informações na API
def func_meteorologia(cidade):
    #API
    link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br"

    requisicao = requests.get(link)
    requisicao_dic = requisicao.json()
    descricao = requisicao_dic['weather'][0]['description']
    temperatura = round(requisicao_dic['main']['temp'] - 273.15, 2)
    resultado = [descricao, str(f"{temperatura}ºC")]
    return resultado

