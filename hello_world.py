from dagster import job, op, fs_io_manager, repository, schedule, ScheduleDefinition
from dagster.utils.log import get_dagster_logger

logger = get_dagster_logger()

@op
def get_name():
    return "dagster"

@op
def get_date():
    return "today"

@op
def hello(name:str, date:str):
    logger.info("It worked!")
    print(f"Hello, {name}! This is dagster on {date}.")


@job
def hello_dagster():
    hello(get_name(),get_date())

@schedule(
    cron_schedule="*/15 * * * *",
    job=hello_dagster,
    execution_timezone="US/Central",
)
def test_schedule(context):
    date = context.scheduled_execution_time.strftime("%Y-%m-%d")
    return {"ops": {"hello": {"config": {"date": date}}}}

@repository
def swa_elt_repository():
    return [hello_dagster, test_schedule]