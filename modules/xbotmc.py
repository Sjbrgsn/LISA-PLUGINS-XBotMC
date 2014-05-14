# -*- coding: UTF-8 -*-
from lisa.server.plugins.IPlugin import IPlugin
import gettext
import inspect
import os
import requests
import json

class XBotMC(IPlugin):
    def __init__(self):
        super(XBotMC, self).__init__()
        self.configuration_plugin = self.mongo.lisa.plugins.find_one({"name": "XBotMC"})
        self.path = os.path.realpath(os.path.abspath(os.path.join(os.path.split(
            inspect.getfile(inspect.currentframe()))[0],os.path.normpath("../lang/"))))
        self._ = translation = gettext.translation(domain='xbotmc',
                                                   localedir=self.path,
                                                   languages=[self.configuration_lisa['lang']]).ugettext

    def xbotmcTest(self, jsonInput):
        url = "http://localhost:8080/jsonrpc"
        headers = {'content-type': 'application/json'}

        payload = {
            "method": "GUI.ShowNotification",
            "params": {
                "title": "Hello, World!",
                "message": "This is amaizing!",
            },
            "jsonrpc": "2.0",
            "id": 0,
        }
        response = requests.post(
            url, data=json.dumps(payload), headers=headers).json()

        return {"plugin": "XBotMC",
                "method": "sayHello",
                "body": self._('Hello. How are you ?')
        }
