#
# Copyright (C) 2019 James Parkhurst
#
# This code is distributed under the BSD license.
#
import pytest
import mock
import getpass
from halerror import HalError


def test_halerror():

    expected_output = (
        "\n\n"
        "I'm sorry, .*. I'm afraid I can't do that."
        "\n\n"
        "Open the pod bay doors, HAL."
    )

    with pytest.raises(HalError, match=expected_output):
        raise HalError("Open the pod bay doors, HAL.")


@mock.patch("getpass.getuser")
def test_halerror_no_getuser(mocked_getuser):
    def raise_runtime_error():
        raise RuntimeError("An error occurred")

    mocked_getuser.side_effect = raise_runtime_error

    expected_output = (
        "\n\n"
        "I'm sorry, Dave. I'm afraid I can't do that."
        "\n\n"
        "Open the pod bay doors, HAL."
    )

    with pytest.raises(HalError, match=expected_output):
        raise HalError("Open the pod bay doors, HAL.")
