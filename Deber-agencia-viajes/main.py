    
import json

#leerlineas = {}
ruta = './lugar.json'
archivoPersona = open(ruta)
leerlineas = json.load(archivoPersona)
print(leerlineas[1]['nombre'],leerlineas[0]['apellido'])
personaNueva = {
    [
       {
            "ciudad": "Tonsupa",
            "direccion": "Costa",
            "dias": "3",
            "numeropersonas": 3,
            "transporte": si,
            "precio": "400",
            "telefono": "0987890751"
        },
        {
            "ciudad": "Manabi",
            "direccion": "Costa",
            "dias": "3",
            "numeropersonas": 3,
            "transporte": si,
            "precio": "400",
            "telefono": "0987890751"
        }
    ]
}
persona1 = {
            "ciudad": "Laguna Azul",
            "direccion": "Sierra",
            "dias": "3",
            "numeropersonas": 3,
            "transporte": si,
            "precio": "400",
            "telefono": "0987890751"
    }
print(type(personaNueva))
#persona1Json = json.dumps(personaNueva)
#print(type(persona1Json))
#person = json.loads(persona1Json)
#print(type(person))
#guardarArchivo = open(ruta, 'w')
#guardarArchivo.writelines(person)
#personaNueva.update(persona1)
#person = json.dumps(personaNueva)
#guardarArchivo = open(ruta, 'w')
#guardarArchivo.writelines(person)