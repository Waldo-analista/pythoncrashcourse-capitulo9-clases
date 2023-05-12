'''
Ejercicio del uso de la clase OrderedDict del módulo collections
'''
from collections import OrderedDict

favorite_languages=OrderedDict()
favorite_languages['jen']='python'
favorite_languages['sarah']='c'
favorite_languages['edward']='ruby'
favorite_languages['phil']='python'

for name, language in favorite_languages.items():
    print("El lenguaje favorito de "+name.title()+" es "+language.title())