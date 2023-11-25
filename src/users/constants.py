from enum import Enum
from functools import lru_cache


class StrEnum(str, Enum):
	pass


class Role(StrEnum):
	ADMIN = "AD"
	SENIOR = "SR"
	JUNIOR = "JR"

	@classmethod
	@lru_cache(maxsize=1)
	def choices(cls):
		results = []
		for element in cls:
			el = (element.value, element.value)
			results.append(el)
		return results
