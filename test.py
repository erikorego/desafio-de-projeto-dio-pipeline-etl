import json
import pandas as pd

#extract
with open('oracle-cards.json', 'r', encoding='utf-8') as lista_de_cards_json:
    cartas = json.load(lista_de_cards_json)

nome = []
cor = []
tipo = []
custo = []

for carta in cartas:
    nome.append(carta['name'])
    cor.append(carta['color_identity'])
    tipo.append(carta['type_line'])
    custo.append(carta['cmc'])

#transform

#tratamento da informação cor
for i in range(len(cor)):
    if len(cor[i]) == 0:
        cor[i] = 'Colorless'
    elif len(cor[i]) > 1:
        cor[i] = 'Multicolor'
    elif cor[i][0] == 'R':
        cor[i] = 'Red'    
    elif cor[i][0] == 'G':
        cor[i] = 'Green'
    elif cor[i][0] == 'U':
        cor[i] = 'Blue'
    elif cor[i][0] == 'B':
        cor[i] = 'Black'
    elif cor[i][0] == 'W':
        cor[i] = 'White'

#tratamento da informação tipo
for i in range(len(tipo)):
    if 'Planeswalker' in tipo[i]:
        tipo[i] = 'Planeswalker'
    elif 'Enchantment' in tipo[i]:
        if 'Creature' in tipo[i]:
            tipo[i] = 'Enchantment Creature'
        elif 'Artifact' in tipo[i]:
            tipo[i] = 'Enchantment Artifact'
        elif 'Land' in tipo[i]:
            tipo[i] = 'Enchantment Land'
        else:
            tipo[i] = 'Enchantment'
    elif 'Artifact' in tipo[i]:
        if 'Creature' in tipo[i]:
            tipo[i] = 'Artifact Creature'
        else:
            tipo[i] = 'Artifact'
    elif 'Sorcery' in tipo[i]:
        tipo[i] = 'Sorcery'
    elif 'Instant' in tipo[i]:
        tipo[i] = 'Instant'
    elif 'Token' in tipo[i]:
        tipo[i] = 'Token'
    elif 'Battle' in tipo[i]:
        tipo[i] = 'Battle'
    elif 'Summon' in tipo[i]:
        tipo[i] = 'Creature'
    elif 'Land' in tipo[i]:
        if 'Creature' in tipo[i] and '//' not in tipo[i]:
            tipo[i] = 'Land Creature'
        else:
            tipo[i] = 'Land'
    elif 'Emblem' in tipo[i]:
        tipo[i] = 'Emblem'
    elif 'Plane' in tipo[i]:
        tipo[i] = 'Plane'
    elif 'Creature' in tipo[i]:
        tipo[i] = 'Creature'

#load

dados = {
    "nome": nome,
    "cor": cor,
    "tipo": tipo,
    "custo": custo
}

df = pd.DataFrame(dados)
nome_do_arquivo = 'mtgdb09-23.xlsx'
df.to_excel(nome_do_arquivo, index=False)
