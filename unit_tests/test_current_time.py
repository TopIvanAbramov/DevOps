import os
import pytest
from datetime import datetime

from flask import Flask, render_template
from app_python.app import zone, time_format, app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_current_time(client):
    """Check if time returned from website matches real time."""

    rv = client.get("/")

    time = datetime.now(zone).strftime(time_format)
    expected_time_string = 'Current time in MOSCOW: {}'.format(time)

    # test 200 response

    assert rv.status_code == 200

    # test if returned time matches current time

    assert expected_time_string in str(rv.data)
