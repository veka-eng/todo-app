import pytest
from app import add_task

def test_add_task():
    tasks = []
    result = add_task(tasks, "Test")
    assert "Test" in result
