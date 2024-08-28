from rich.console import Console

_package_console: None | Console = None

def get_package_console() -> Console:
    """
    Get the console instance for the package.
    :return:
    """
    return Console(highlight=False, log_time=False, log_path=False)


def get_rich_rendered_output(renderable_element) -> str:
    """

    :param renderable_element:
    :return:
    """
    console = get_package_console()
    console.record = True

    return ""