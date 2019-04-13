#
# Copyright (C) 2019 James Parkhurst
#
# This code is distributed under the BSD license.
#
import getpass


class HalError(RuntimeError):
    """
    A sci-fi error message!

    """

    def __init__(self, message="", template=None):
        """
        Initialise the exception

        :param message: The exception message
        :param template: The exception template  

        """

        # Get the username
        try:
            username = getpass.getuser()
        except Exception:
            username = "Dave"

        # Get the template
        if template is None:
            template = (
                "{message}\n\nI'm sorry, {username}. I'm afraid I can't do that."
            )

        # Put in HAL error text.
        text = template.format(username=username, message=message)

        # Init base class
        super().__init__(text)
