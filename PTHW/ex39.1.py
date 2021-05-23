# Creating states map
states = {
    'São Paulo': 'SP',
    'Rio de Janeiro': 'RJ',
    'Santa Catarina': 'SC',
    'Paraná': 'PR',
    'Rio Grande do Sul': 'RS'
}

# Creating cities map
cities = {
    'SC': 'Florianópolis',
    'PR': 'Curitiba',
    'SP': 'São Paulo',
    'RJ': 'Rio de Janeiro'
}

# Add a city
cities['RS'] = 'Porto Alegre'
cities['SC'] = 'Palhoça'
# Add a state
states['Rondônia'] = 'RO'
"""
# Prints
print(cities['SC'])  # Here Python takes just one item
print(cities['SP'])
print(' ')
print(states)
print(' ')
print(states['Paraná'])

# Priting every state abbreviation
for x, y in list(states.items()):
    print(f'State: {x}, Abbreviation: {y}')"""

# Priting every city in state
for abbrevi, city in list(cities.items()):
     # Take just one city from every state
    print(f"City: {city}, State: {abbrevi}") 

