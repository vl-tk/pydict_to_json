import sublime
import sublime_plugin
import json


class pytojsonCommand(sublime_plugin.TextCommand):
	""" converts python dict to json and beautifies it.
	"""
	def run(self, edit):
		for selection in self.view.sel():
			text = self.view.substr(selection)
			try:
				text = eval(text)
				if type(text) == dict:
					_dict = dict(text)
				elif type(text) == list:
					_dict = text
				replace_text = json.dumps(_dict, sort_keys=True, indent=4)
			except Exception as e:
				print(e)
			else:
				self.view.replace(edit, selection, replace_text)
