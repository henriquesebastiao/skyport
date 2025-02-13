from dataclasses import dataclass, field
from datetime import date as dt
from typing import Optional


@dataclass
class Apod:
    title: str
    date: dt
    explanation: str = field(repr=False)
    media_type: str
    url: str = field(repr=False)
    service_version: str = field(repr=False)
    copyright: Optional[str] = field(default=None)
    hdurl: Optional[str] = field(repr=False, default=None)

    def __post_init__(self):
        if self.copyright:
            self.copyright = self.copyright.strip('\n')
        self.date = dt.fromisoformat(self.date)
