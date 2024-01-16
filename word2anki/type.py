"""Word type define
"""
from typing import TypedDict, Optional,NotRequired

class definition(TypedDict):
	definition: str
	example: NotRequired[str]
	synonyms: list[str]
	antonyms: list[str]


class meaning(TypedDict):
	partOfSpeech: str
	definitions: list[definition]


class phonetic(TypedDict):
	text: str
	audio: str


class word(TypedDict):
	word: str
	phonetic: NotRequired[str]
	phonetics: list[phonetic]
	meanings: list[meaning]
