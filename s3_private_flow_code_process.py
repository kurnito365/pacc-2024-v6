from prefect import flow
from prefect_aws import S3Bucket


@flow(log_prints=True)
def test_flow():
    print("Hello World")


if __name__ == "__main__":
    source = S3Bucket.load("s3-bucket-block")

    flow.from_source(
        source=source,
        entrypoint="s3_private_flow_code_process.py:test_flow",
    ).deploy(name="my-aws-s3-deployment-process-pool", work_pool_name="my-process-pool")
