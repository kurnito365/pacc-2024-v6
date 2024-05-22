from prefect import flow
from prefect.events.schemas import DeploymentEventTrigger


@flow(log_prints=True)
def downstream_flow(ticker: str = "AAPL") -> str:
    print(f"got {ticker}")


downstream_deployment_trigger = DeploymentEventTrigger(
    name="Upstream Flow - Pipeline",
    enabled=True,
    match_related={
        "prefect.resource.id": "prefect.flow.5c933ae4-dd43-4705-90eb-cfdeb4c028fb"
    },
    expect={"prefect.flow-run.Completed"},
)


if __name__ == "__main__":
    downstream_flow.from_source(
        source="https://github.com/prefecthq/pacc-2024-v3.git",
        entrypoint="105/deployment-trigger.py:downstream_flow",
    ).deploy(
        name="ticker-deploy",
        work_pool_name="managed1",
        triggers=[downstream_deployment_trigger],
    )


# To get familiar with the events see the docs
# and check out the event feed in the UI and click the Raw tab
