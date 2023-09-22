FROM ghcr.io/mlflow/mlflow

RUN pip install --no-cache-dir psycopg2-binary boto3

ENTRYPOINT [ "mlflow", "server" ]