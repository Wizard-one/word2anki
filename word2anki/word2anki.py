from .store import _get_model,make_package
from .search import FreeDictAPI
import genanki
import time
from tqdm import tqdm
from typing import Optional

def word2anki(file:str,
			  model_id=114514,
			  model_name="English",
			  deck_id=114514,
			  deck_name="English",
			  savename:Optional[str]=None)->None:
	"""read word list from file and convert to anki package.
	
	Parameters
	----------
	file
		word list file.
	model_id, optional
		model id, by default 114514
	model_name, optional
		model name, by default "English"
	deck_id, optional
		deck id, by default 114514
	deck_name, optional
		deck name, by default "English"

	Examples
	--------
	>>> word2anki("wordlist.txt")
		fetch progress: 100%|████| 40/40 [00:59<00:00,  1.49s/it]
		Packaging progress: 100%|████| 40/40 [00:00<00:00, 409.89it/s]
		Save to 2024-01-16.apkg

	Notes
	-----
	- The word list file should be a text file, each line is a word.
	- The word list file should be UTF-8 encoded.
	- The word list file should not contain any blank line.
	- The word list file should not contain any special characters.
	- The word list file should not contain any Chinese characters.

	"""	
	
	with open(file, "r") as f:
		words=f.readlines()
	wordlist=[]
	for i,w in enumerate(tqdm(words,desc=f"fetch progress")):
		word=FreeDictAPI(w.strip())
		if word is not None:
			wordlist.append(word)
		if i//10==0:
			time.sleep(1)

	model = _get_model(model_id, model_name)
	deck = genanki.Deck(deck_id, deck_name)
	make_package(wordlist, deck, model,savename)