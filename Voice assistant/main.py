import speech_recognition
import subprocess, platform, os
import random

# ----------------------------------------------------------------------------------------

sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5

commands_dict = {
	'commands': {
		'greeting'   : ['привет', 'приветик', 'привет бот', 'приветствую', 'бот'],
		'create_task': ['добавить задачу', 'создать задачу', 'добавить запись', 'создать запись', 'добавь задачу', 'создай задачу', 'заметка'],
		'play_music' : ['включи музыку', 'музыка', 'дискотека', 'включи музон'],
	}
}

# ----------------------------------------------------------------------------------------

def listen_command():
	'''The function will return the recorgnized command'''
	
	try:
		with speech_recognition.Microphone() as mic:
			sr.adjust_for_ambient_noise(source=mic, duration=0.5)
			audio = sr.listen(source=mic)
			query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
		return query
	except speech_recognition.UnknownValueError:
		return 'Damn... Я вас не понимаю! :|'

# ----------------------------------------------------------------------------------------

def greeting():
	'''Greeting function'''
	
	return 'Привет кожаный мешок!'

# ----------------------------------------------------------------------------------------

def create_task():
	'''Create a todo task'''
	
	print('Что добавить в список дел?')
	
	query = listen_command()
	
	with open('todo-list.txt', 'a') as file:
		file.write(' - {0}\n'.format(query))
		
	return 'Задача {0} добавлена в todo-list!'.format(query)

# ----------------------------------------------------------------------------------------

def play_music():
	'''Play a random mp3 file'''
	
	files = os.listdir('music')
	random_file = 'music/{0}'.format(random.choice(files))
	# os.system('xdg.open {0}'.format(random_file))
	
	if platform.system() == 'Linux':
		subprocess.call(('xdg-open', random_file))
	elif platform.system() == 'Windows':
		os.startfile(random_file)

	return 'Приятного прослушивания "{0}" 🔊'.format(random_file.split("/")[-1])

# ----------------------------------------------------------------------------------------

def main():
	query = listen_command()

	for k, v in commands_dict['commands'].items():
		if query in v:
			print(globals()[k]())

# ----------------------------------------------------------------------------------------

if __name__ == '__main__':
	main()
	
