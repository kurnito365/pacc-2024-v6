import os
from time import sleep

from prefect import task, flow
from prefect.transactions import transaction


@task
def write_file(filename: str, contents: str):
    "Writes to a file."
    with open(filename, "w") as f:
        f.write(contents)


@write_file.on_rollback
def del_file(txn):
    "Deletes file."
    os.unlink(txn.get("filename"))


@task
def quality_test(filename):
    "Checks contents of file."
    with open(filename, "r") as f:
        data = f.readlines()

    if len(data) < 2:
        raise ValueError(f"Not enough data!")


@flow
def pipeline(filename: str, contents: str):
    with transaction() as txn:
        txn.set("filename", filename)
        write_file(filename, contents)
        sleep(2)  # sleeping to give you a chance to see the file
        quality_test(filename)


if __name__ == "__main__":
    pipeline(
        filename="side-effect.txt",
        contents="hello world",
    )
