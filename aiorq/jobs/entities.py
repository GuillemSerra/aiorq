from dataclasses import dataclass
from datetime import datetime
from typing import Callable


@dataclass
class Job:
    id: str = ''
    task: Callable = None
    queue_id: str = 'default'
    name: str = ''
    queued_time: datetime = None
    start_time: datetime = None
    end_time: datetime = None

    def __eq__(self, other):
        return self.id == other.id
