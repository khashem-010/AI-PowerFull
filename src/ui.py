from Screens.Screen import Screen
from Components.ConfigList import ConfigListScreen
from Components.config import config

class AIPowerFullSetupScreen(Screen, ConfigListScreen):
    skin = """
    <screen position="center,center" size="800,600" title="AI-PowerFull Settings">
        <widget name="config" position="50,50" size="700,500" />
    </screen>
    """

    def __init__(self, session):
        Screen.__init__(self, session)
        self.setup_title = "AI-PowerFull Settings"
        self.createConfigList()

    def createConfigList(self):
        from Components.config import getConfigListEntry
        self["config"].list = [
            getConfigListEntry("API Key", config.plugins.AIPowerFull.api_key)
        ]
