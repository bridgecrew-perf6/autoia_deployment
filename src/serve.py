from email.policy import default
import mlflow
import os
import click
import json

from requests import request
from config.definitions import ROOT_DIR

@click.command(
    help="Ejecuta el modelo con el request del usuario "
)
@click.option("--request",default="""{
                "sources": [
                    {
                    "name": "T06",
                    "vars": [
                        {
                            "name": "Gen_RPM_Max",
                            "values": [
                                0, 12.4, 14.5, 20.1
                            ]
                        },
                        {
                            "name": "Gen_Bear_Temp_Avg",
                            "values": [
                                0, 12.4, 14.5, 20.1
                            ]
                        }
                    ]
                    }
                ]
            }""")
def serve(request):
    serveInput = json.loads(request)
    first_var = serveInput['sources'][0]['vars'][0]
    print({'name': first_var['name'], 'values': first_var['values']})


def create_dir(dir):
    if os.path.exists(dir) == False:
        os.makedirs(dir, exist_ok=False)
        print("El directorio ", dir, " ha sido creado")

if __name__ == '__main__':
    serve()