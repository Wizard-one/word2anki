import genanki
import time
import genanki
import jinja2
from .type import word
from .search import FreeDictAPI
from tqdm import tqdm
from typing import Optional

def _get_model(model_id=114514,name="English")->genanki.Model:
	"""set anki model

	use `./templates/front.html` as front  template
	use `"./templates/back.css"` as back  style

	Parameters
	----------
	model_id, optional
		model id, by default 114514
	name, optional
		model name, by default "English"

	Returns
	-------
		anki model
	
	Notes
	-----
	Because Anki's templates do not support mutilevel field and list. In back, We use HTML with Jinja template instead.

	Reference
	---------

	[Anki document](https://docs.ankiweb.net/templates/fields.html)
	"""	
	back_style="""{{FrontSide}}\n{{meanings}}"""
	with open("./templates/front.html", "r") as f:
		front_style = f.read()
	with open("./templates/back.css", "r") as f:
		css = f.read()
	model = genanki.Model(
		model_id=model_id, name=name,
		fields=[
			{'name': 'word'},
			{'name': 'phonetic'},
			{'name': 'meanings'},
		],
		templates=[
			{
				'name': '卡片1',
				'qfmt': front_style,
				'afmt': back_style,
			},
		],
		css=css)
	return model

def _add_note(word: word, model: genanki.Model):
	"""transform word to anki note

	use `"./templates/back.html.jinja"` as back card template

	Parameters
	----------
	word
		word dict
	model
		anki model

	Returns
	-------
		a single anki note
	"""	
	env = jinja2.Environment(
		loader=jinja2.FileSystemLoader('./templates'),
		autoescape=jinja2.select_autoescape()
	)
	template = env.get_template("back.html.jinja")
	meanings = template.render(meanings=word['meanings'])

	my_note = genanki.Note(
		model=model,
		fields=[word['word'], word['phonetic'],meanings],
		sort_field="word"
	)
	return my_note


def make_package(words:list[word],deck:genanki.Deck,model:genanki.Model,savename:Optional[str]=None)->None:
	"""convert word list to anki package.
	
	save package to `apkg`

	Parameters
	----------
	words
		word list
	deck
		card deck
	model
		card model
	"""	
	for w in tqdm(words,desc="Packaging progress"):
		my_note = _add_note(w, model)
		deck.add_note(my_note)
	my_package = genanki.Package(deck)
	# my_package.media_files = [ f'./myaudio/{word}.mp3' for word in dic.keys()]
	if savename is None:
		savename = time.strftime("%Y-%m-%d", time.localtime())
	my_package.write_to_file(f"./{savename}.apkg")
	print(f"Save to {savename}.apkg")

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