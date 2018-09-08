from dataclasses import dataclass
from datetime import datetime
from typing import Coroutine


@dataclass
class Job:
    id: int
    task: Coroutine
    name: str = ''
    start_time: datetime = datetime.now()
    end_time: datetime = None

    def __eq__(self, other):
        return self.id == other.id
