import boto3


def download_data_from_s3(bucket_name, remote_path, local_path):
    s3 = boto3.client('s3')
    try:
        s3.download_file(bucket_name, remote_path, local_path)
        print(f"Datos descargados desde {bucket_name}/{remote_path} a {local_path}")
    except Exception as e:
        print(f"Error al descargar datos desde S3: {e}")


if __name__ == "__main__":
    bucket_name = 'mlops-testing-course'
    remote_path = 'data_scientific/data.csv'
    local_path = 'data/data.csv'

    download_data_from_s3(bucket_name, remote_path, local_path)
