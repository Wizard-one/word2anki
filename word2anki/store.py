import genanki
import time
import genanki
import jinja2
from .type import word
from tqdm import tqdm


def _get_model(model_id=114514,name="English"):
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


def make_package(words:list[word],deck:genanki.Deck,model:genanki.Model)->None:
	for w in tqdm(words,desc="Packaging progress"):
		my_note = _add_note(w, model)
		deck.add_note(my_note)
	my_package = genanki.Package(deck)
	# my_package.media_files = [ f'./myaudio/{word}.mp3' for word in dic.keys()]

	today = time.strftime("%Y-%m-%d", time.localtime())
	my_package.write_to_file(f"./{today}.apkg")
