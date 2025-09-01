from dataclasses import dataclass
from datetime import datetime
from typing import Literal, Optional, Sequence

Difficulty = Literal["easy", "medium", "hard"]

@dataclass(frozen=True)
class FilterOptions:
    difficulty: Optional[Difficulty] = None
    languages: Optional[Sequence[str]] = None
    date_from: Optional[datetime] = None
    date_to: Optional[datetime] = None
    starred_repos: Optional[Sequence[str]] = None
    bookmark_ids: Optional[Sequence[str]] = None
