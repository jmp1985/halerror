import pytest
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
