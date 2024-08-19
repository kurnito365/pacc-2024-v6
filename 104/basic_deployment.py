from prefect import flow


@flow(log_prints=True)
def my_flow(name: str = "World"):
    print(f"Hello {name}!")


if __name__ == "__main__":
    my_flow.from_source(
        source="https://github.com/PrefectHQ/pacc-2024-v4.git",
        entrypoint="104/basic_deployment.py:my_flow",
    ).deploy(
        name="pacc-deployment-process-3",
        work_pool_name="pacc-process-pool",
        tags=["pacc", "hello"],
    )
