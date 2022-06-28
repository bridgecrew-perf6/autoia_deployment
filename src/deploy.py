from email.policy import default
import os
import click
import mlflow
from config.definitions import ROOT_DIR
from mlflow.tracking import MlflowClient
import json

@click.command(
    help="Despliega el modelo y los deja listo para servir "
)
@click.option("--experiment_id", default="1")
@click.option("--tracking_uri", default="http://54.197.194.191:5000")
@click.option("--pipeline_req", default='{"runs":[{"name":"selection", "id":"fe4e9f343c3049828ffcc61f0ab75770"}, {"name":"imputation", "id":"e3b3599c573444d081215c08a707e0e2"}]}')
def deploy(pipeline_req, experiment_id, tracking_uri):
    pipeline_info = json.loads(pipeline_req)
    mlflow.set_tracking_uri(tracking_uri)
    with mlflow.start_run(experiment_id=experiment_id):
        client = MlflowClient()
        downloaded_artifact_dir = "downloaded_artifacts"
        local_dir = os.path.join(ROOT_DIR, downloaded_artifact_dir)
        create_dir(local_dir)
        for run_info in pipeline_info['runs']:
            print("Downloading artifacts of ", run_info['name'])
            local_path = os.path.join(local_dir, run_info['name'])
            create_dir(local_path)
            client.download_artifacts(run_info['id'], "", local_path)
        print('Pipeline deployed and ready for use')

def create_dir(dir):
    if os.path.exists(dir) == False:
        os.makedirs(dir, exist_ok=False)
        print("El directorio ", dir, " ha sido creado")

if __name__ == '__main__':
    deploy()