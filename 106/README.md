# 106 - Event-driven orchestration: run workflows in response to events

## Agenda

- Composite triggers
- Metric triggers
- Event-driven workflows:
  - Data lands in S3 - run a deployment with an automation
  - Webhook is hit: data from it flows into a deployment as a parameter
- State change hooks

## Lab

- Create an automation that runs a deployment in response to a trigger
- Stretch 1: Pass information from the event into the deployment
- Stretch 2: Use a composite trigger in an automation
- Stretch 3: Use a metric trigger in an automation

## Example

[Data Lake Workflow Automation](https://github.com/PrefectHQ/prefect-demos/tree/main/flows/aws/datalake)
