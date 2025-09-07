from abc import ABC, abstractmethod

class ResumePart(ABC):
    @abstractmethod
    def to_typst_str(self) -> str:
        pass
