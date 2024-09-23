from datetime import timedelta
from time import sleep
from prefect import flow, task
from prefect.cache_policies import INPUTS


@task(cache_policy=INPUTS, cache_expiration=timedelta(minutes=1))
def hello_task(name_input: str):
    print(f"Hello {name_input}")


@flow(log_prints=True)
def hello_flow(name_input: str):
    hello_task(name_input)


if __name__ == "__main__":
    hello_flow(name_input="world")
    sleep(100)
    hello_flow(name_input="world")

    # does not rerun, but shouldn't it?
