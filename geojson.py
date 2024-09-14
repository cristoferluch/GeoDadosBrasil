from rich.progress import track
from rich import print
import requests
import json
import time

lista_qualidades = ['minima', 'intermediaria', 'maxima']
URL_BASE_LOCALIDADES = 'https://servicodados.ibge.gov.br/api/v1/localidades/'
URL_BASE_MALHAS = 'https://servicodados.ibge.gov.br/api/v3/malhas/'

def get_json_base():
    return { "type": "FeatureCollection", "features": []}

def cria_arquivo(geojson, nome):
    
    with open(f'{nome}.geojson', 'w', encoding='utf-8') as f:
        json.dump(geojson, f, ensure_ascii=False)
    print('[bright_green]Arquivo salvo[/bright_green]')

def get_dados(url):
    try:
        response = requests.get(url)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")
        time.sleep(10)
        return get_dados(url)

def get_regiao():
    response = requests.get(f'{URL_BASE_LOCALIDADES}regioes?view=nivelado')
    return response.json()

def get_mesorregioes():
    response = requests.get(f'{URL_BASE_LOCALIDADES}mesorregioes')
    return response.json()


def get_estados():
    response = requests.get(f'{URL_BASE_LOCALIDADES}estados')
    return response.json()


def get_municipios():
    response = requests.get(f'{URL_BASE_LOCALIDADES}municipios?orderBy=nome')
    return response.json()

def montaGeoJsonMesorregioes(qualidade):

    dados = get_mesorregioes()
    geojson_base = get_json_base()

    for dado in track(dados, description="Baixando dados das mesorregiões..."):

        print(f"[cyan]{dado['id']}[/cyan] - [green]{dado['nome']}[/green] - [yellow]{dado['UF']['sigla']}[/yellow]")

        id = dado['id']
        nome = dado['nome']
        sigla_uf = dado['UF']['sigla']

        geojson = get_dados(f'{URL_BASE_MALHAS}mesorregioes/{id}?formato=application/vnd.geo+json&qualidade={qualidade}')

        for feature in geojson['features']:
            feature['properties']['id'] = id
            feature['properties']['nome'] = nome
            feature['properties']['uf'] = sigla_uf
            feature['properties'].pop('codarea', None)
           
            geojson_base['features'].append(feature)

    cria_arquivo(geojson_base, f'mesorregioes_{qualidade}')

def montaGeoJsonEstados(qualidade):

    dados = get_estados()
    geojson_base = get_json_base()

    for dado in track(dados, description="Baixando dados dos estados..."):

        print(f"[cyan]{dado['id']}[/cyan] - [green]{dado['nome']}[/green] - [yellow]{dado['sigla']}[/yellow]")

        id = dado['id']
        nome = dado['nome']
        sigla_uf = dado['sigla']
    
        geojson = get_dados(f'{URL_BASE_MALHAS}estados/{id}?formato=application/vnd.geo+json&qualidade={qualidade}')

        for feature in geojson['features']:
            feature['properties']['id'] = id
            feature['properties']['nome'] = nome
            feature['properties']['uf'] = sigla_uf
            feature['properties'].pop('codarea', None)
           
            geojson_base['features'].append(feature)

    cria_arquivo(geojson_base, f'estados_{qualidade}')

def montaGeoJsonRegiao(qualidade):

    dados = get_regiao()
    geojson_base = get_json_base()

    for dado in track(dados, description="Baixando dados das regiões..."):

        print(f"[cyan]{dado['regiao-id']}[/cyan] - [green]{dado['regiao-nome']}[/green] - [yellow]{dado['regiao-sigla']}[/yellow]")

        id = dado['regiao-id']
        nome = dado['regiao-nome']
        sigla_regiao = dado['regiao-sigla']

        geojson = get_dados(f'{URL_BASE_MALHAS}regioes/{id}?formato=application/vnd.geo+json&qualidade={qualidade}')

        for feature in geojson['features']:
            feature['properties']['id'] = id
            feature['properties']['nome'] = nome
            feature['properties']['regiao'] = sigla_regiao
            feature['properties'].pop('codarea', None)

            geojson_base['features'].append(feature)

    cria_arquivo(geojson_base, f'regiao_{qualidade}')

def montaGeoJsonMunicipios(qualidade):
    dados = get_municipios()
    geojson_base = get_json_base()

    for dado in track(dados, description="Baixando dados dos municípios..."):
        print(f"[cyan]{dado['id']}[/cyan] - [green]{dado['nome']}[/green] - [yellow]{dado['microrregiao']['mesorregiao']['UF']['sigla']}[/yellow]")

        id = dado['id']
        nome = dado['nome']
        sigla_uf = dado['microrregiao']['mesorregiao']['UF']['sigla']

        geojson = get_dados(f'{URL_BASE_MALHAS}municipios/{id}?formato=application/vnd.geo+json&qualidade={qualidade}')

        for feature in geojson['features']:
            feature['properties']['id'] = id
            feature['properties']['nome'] = nome
            feature['properties']['uf'] = sigla_uf
            feature['properties'].pop('codarea', None)

            geojson_base['features'].append(feature)

    cria_arquivo(geojson_base, f'municipios_{qualidade}')

if __name__ == "__main__":

    print('Informe qual GeoJson baixar')
    print('1 - Estados')
    print('2 - Região')
    print('3 - Mesorregião')
    print('4 - Municípios')
    print('5 - Todos')

    opc_mapa = int(input())

    print('Informe a qualidade das malhas')
    print('1 - minima')
    print('2 - intermediaria')
    print('3 - maxima')

    opc_qualidade = int(input())

    qualidade = lista_qualidades[opc_qualidade - 1]

    print(opc_mapa)


    try:

        if opc_mapa == 1 or opc_mapa == 5:
            montaGeoJsonEstados(qualidade)
        if opc_mapa == 2 or opc_mapa == 5:
            montaGeoJsonRegiao(qualidade)
        if opc_mapa == 3 or opc_mapa == 5:
            montaGeoJsonMesorregioes(qualidade)
        if opc_mapa == 4 or opc_mapa == 5:
            montaGeoJsonMunicipios(qualidade)
        else:
            print("Opção de mapa inválida")

    except Exception as e:
        print(f"Erro: {e}")