# 101 Prefect basics: Create a workflow you can schedule and observe

## Agenda

- Setup: version, login
- From Python function to Prefect flow
- Create a deployment with .serve()
- Run a deployment
- Deployment schedules
- Parameters
- Resources

## Lab

Use Open-Meteo API

- Authenticate your CLI to Prefect Cloud
  - Fine to use a personal account or an organization test workspace
- Take a function that fetches data and make it a flow
- Use .serve() method to deploy your flow
- Run your flow from the UI
- Create a schedule for your deployment
- Shut down your server
- Run a deployment from the CLI, override the params

API docs: <https://open-meteo.com/en/docs>

Example: wind speed for the last hour:

`weather.json()["hourly"]["windspeed_10m"][0]`
