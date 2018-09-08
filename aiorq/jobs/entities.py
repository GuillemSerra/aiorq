from dataclasses import dataclass
from datetime import datetime
from typing import Coroutine


@dataclass
class Job:
    id: str = ''
    task: Coroutine = None
    queue: str = 'default'
    name: str = ''
    queued_time: datetime = None
    start_time: datetime = None
    end_time: datetime = None

    def __eq__(self, other):
        return self.id == other.id
