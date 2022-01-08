from dagster import job, op, fs_io_manager
from dagster.utils.log import get_dagster_logger

logger = get_dagster_logger()

@op
def get_name():
    return "dagster"


@op
def hello(name: str):
    logger.info("It worked!")
    print(f"Hello, {name}! This is dagster.")


@job
def hello_dagster():
    hello(get_name())