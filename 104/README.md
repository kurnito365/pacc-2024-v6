# 104 - Run your flows in the cloud and easily switch infrastructure with work pool-based deployments

## Agenda

- Create work pool-based deployments with .deploy()
- Flow code storage
- Prefect managed work pools
- Hybrid work pools with workers
- Push work pools

## Lab

- Create a Prefect Managed work pool.
- Create and run a deployment with .deploy() that uses the work pool.
- Use flow code stored in your own GitHub repository with a deployment.
  - ❗️Push your code to GitHub manually.
- Pause and resume the work pool from the UI.
- Stretch 1: add an environment variable to a work pool and use it.

- If you don’t have Docker installed:
  - Stretch 2a: use a Process work pool to run a flow locally in a subprocess.
    - Create a Process work pool from the UI
    - Create a deployment that references flow code stored in GitHub

- If you have Docker installed:
  - Stretch 2b: created a deployment where you bake your flow code into a Docker image with .deploy().
  - Don’t push the image to a remote repository (or do log in and push it to DockerHub).

  - Don’t forget to:
    - Start Docker on your machine
    - `pip install -U prefect-docker`
    - Make a Docker work pool
