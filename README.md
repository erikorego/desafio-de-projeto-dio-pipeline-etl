# desafio-de-projeto-pipeline-etl
Desafio de Projeto para o BootCamp da DIO com parceria com Santander em Ciência de Dados com Python

O pipeline foi desenvolvido para tratar dados extraídos do site Scryfall.com que contém uma base de dados do Card Game Magic: the Gathering.

1. A extração dos dados foi feita de um arquivo .json
2. Os dados foram tratados para facilitar a sua leitura
3. Os dados tratados foram carregados em um arquivo .xlsx

Algumas melhorias que serão implementadas no futuro:
 - Buscar os dados diretamente da API ao invés de baixa-los para depois tratar;
 - Fazer uma filtragem melhor dos dados que serão extraídos, alguns tipos de carta não apresentam informações relevantes, como tokens, planes, schemas etc. 

Bibliotecas Python necessárias:
* Pandas
* Workbook
* json