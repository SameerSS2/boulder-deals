from abc import ABC, abstractmethod
from typing import Any


class BaseScraper(ABC):
    @abstractmethod
    def scrape(self) -> list[dict[str, Any]]:
        raise NotImplementedError
