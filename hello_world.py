from dagster import job, op, fs_io_manager


@op
def get_name():
    return "dagster"


@op
def hello(name: str):
    print(f"Hello, {name}! This is dagster.")


@job
def hello_dagster():
    hello(get_name())