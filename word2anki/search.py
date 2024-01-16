import requests
from .type import word,meaning,definition
from loguru import logger
from typing import Optional

def _get_phonetic(word: word)->str:
	"""Get phonetic from word.

	FreeDictAPI some word lack phonetic, so we need to get it from phonetics.	

	Parameters
	----------
	word
		single word

	Returns
	-------
	phonetic
		phonetic of word
	"""	
	phonetic = word.get('phonetic', None)
	if phonetic is not None:
		return phonetic
	for p in word['phonetics']:
		if p.get('text', None) is not None:
			return p['text']

	return " "

def checker(search_word,res:dict)->Optional[word]:
	"""check FreeDictAPI respons

	lack field word will log and return None.
	
	Parameters
	----------
	search_word
		search word
	res
		respons

	Returns
	-------
		_description_
	"""	
	for k in word.__required_keys__:
		if k not in res:
			logger.info(f"{search_word} lack {k}")
			return None
	for k in meaning.__required_keys__:
		for m in res['meanings']:
			if k not in m:
				logger.info(f"{search_word}'s {m}  lack {k}")
				return None
	phonetic=_get_phonetic(res)
	w:word=res.copy()
	w['phonetic']=phonetic
	return w



def FreeDictAPI(word:str)->Optional[word]:
	"""fetch word from FreeDictAPI.
	
	lack field word will log and return None.
	
	Parameters
	----------
	word
		single word

	Returns
	-------
		word dict
	"""	
	url=f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
	header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}	 
	res=requests.get(url,headers=header,timeout=10)
	return checker(word,res.json()[0])

def _get_mp3(word):
	api = f'http://dict.youdao.com/dictvoice?audio={word}'
	header = {
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
	res = requests.get(api, headers=header, timeout=10)
	filepath = f"./myaudio/{word}.mp3"
	try:
		with open(filepath, 'wb') as file:
			file.write(res.content)
	except:
		return (f'{word}单词没找到音频')

if __name__ == "__main__":
	print(FreeDictAPI("monopoly"))