from .store import _get_model,make_package
from .search import FreeDictAPI
import genanki
import time
from tqdm import tqdm

def word2anki(file:str,
			  model_id=114514,
			  model_name="English",
			  deck_id=114514,
			  deck_name="English"):
	
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
	make_package(wordlist, deck, model)