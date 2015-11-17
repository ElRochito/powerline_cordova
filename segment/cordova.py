from __future__ import absolute_import
from subprocess import Popen, PIPE
from powerline.theme import requires_segment_info

import os
import sys
import subprocess
import commands
import json
from xml.dom import minidom

@requires_segment_info
def version(pl, segment_info):
    #sys.path.insert(1, '/Users/julien/.config/bin')
    #print sys.path
    try:
        if os.path.isfile("config.xml") == False:
            return None

        continents = [];
        status, cordova_version = commands.getstatusoutput("cordova --version")
        c = commands.getstatusoutput("cordova plugin list")

        json_data=open("./platforms/platforms.json").read()
        data = json.loads(json_data)
        for item in data:
            #print item
            continents.append(item)

        platforms = ', '.join(continents)
        if cordova_version != '':
            return [{
                'contents': 'V : ' + str(cordova_version) + ' | P : ' + platforms + '',
                'highlight_groups': ['version']
            }]
        else:
            return None

    except OSError as e:
        if e.errno == 2:
            pass
        else:
            raise
