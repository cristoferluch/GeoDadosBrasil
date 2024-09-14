# GeoDadosBrasil

Este repositório contém arquivos [GeoJSON](https://geojson.org/) dos estados, municípios, mesorregiões e regiões do Brasil, disponíveis em três níveis de detalhamento: mínima, intermediária e máxima. Note que todos os arquivos GeoJSON estão minificados, o que significa que foram removidos espaços em branco e quebras de linha para reduzir o tamanho do arquivo e melhorar o desempenho.

## Conjunto de dados

- **Regiões:** Dados sobre as grandes divisões do Brasil.<br>
- **Estados:** Informações detalhadas sobre cada estado brasileiro.<br>
- **Mesorregiões:** Dados das subdivisões das regiões brasileiras.<br>
- **Municípios:** Dados sobre todos os municípios do Brasil.<br>

## Qualidade:
Os dados estão disponíveis em três níveis de qualidade:
- **Mínima:** Para visualizações gerais e análises rápidas.<br>
- **Intermediária:** Um equilíbrio entre detalhe e desempenho.<br>
- **Máxima:** O maior nível de detalhamento para análises precisas.<br>


## Visualização dos Dados
Os arquivos GeoJSON podem ser visualizados interativamente no [geojson.io](https://geojson.io/). Basta carregar os arquivos GeoJSON para ver as informações em um mapa interativo.

## Script Python

### Instalando as Dependências
Para instalar as dependências necessárias para o script Python, execute o seguinte comando:

````shel
pip install -r requirements.txt
````
### Uso
Certifique-se de ter o Python instalado e as dependências configuradas. Em seguida, execute o script:
````shel
python geojson.py
````

### Formato do Arquivo
Os arquivos GeoJSON seguem o formato:
````shel
{
  "type": "Feature",
  "geometry": {
    "type": "Point",
    "coordinates": [125.6, 10.1]
  },
  "properties": {
    "id": 42,
    "nome": "Santa Catarina",
    "uf": "SC"
  }
}
````
<p align="center">
   <img src="https://github.com/cristoferluch/assets/blob/main/geojson-estados.png" alt="#01" width="1200">
</p>


## Fonte dos dados
Os dados são obtidos através da [API do IBGE](https://servicodados.ibge.gov.br/api/docs/).


## Licença
Este projeto está licenciado sob a [Creative Commons CC0 1.0 Universal](https://github.com/cristoferluch/GeoDadosBrasil/blob/main/LICENSE), o que permite que os dados sejam usados sem restrições.


