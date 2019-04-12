from getpass import getuser


class HalError(RuntimeError):
    """
    A class implementation an exception.

    """

    def __init__(self, message="", template=None):

        # Get the username
        try:
            username = getuser()
        except Exception:
            username = "Dave"

        # Get the template
        if template is None:
            template = (
                "\n\nI'm sorry, {username}. I'm afraid I can't do that.\n\n{message}"
            )

        # Put in HAL error text.
        text = template.format(username=username, message=message)

        # Init base class
        super().__init__(text)
