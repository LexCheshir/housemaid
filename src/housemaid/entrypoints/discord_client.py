import structlog
from structlog.stdlib import BoundLogger

from housemaid.meta import settings

base_log: BoundLogger = structlog.get_logger()


def main() -> None:
    log = base_log.bind(function="main")
    print(f"{settings.app_name} {settings.version}")
    log.info("Done ^^")
