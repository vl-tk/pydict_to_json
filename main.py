import json
from collections import OrderedDict

import sublime_plugin


class PydictToJsonCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for selection in self.view.sel():
            text = self.view.substr(selection)
            try:
                text = eval(text)
                if type(text) == dict:
                    _dict = OrderedDict(text)
                elif type(text) == list:
                    _dict = text
                replace_text = json.dumps(_dict, indent=4)
            except Exception as e:
                print(e)
            else:
                self.view.replace(edit, selection, replace_text)
