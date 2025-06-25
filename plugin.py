from Plugins.Plugin import PluginDescriptor
from Screens.Screen import Screen
from Components.ConfigList import ConfigListScreen
from Components.config import config, ConfigSubsection, ConfigText, ConfigYesNo, ConfigSelection
from Components.ActionMap import ActionMap
from Components.Label import Label
from .ai_engine import AIEngine
from .translation_service import SubtitleTranslator
from .voice_dubbing import VoiceDubbingEngine
import threading

config.plugins.AIPowerFull = ConfigSubsection()
config.plugins.AIPowerFull.enabled = ConfigYesNo(default=True)
config.plugins.AIPowerFull.api_key = ConfigText(default="", fixed_size=False)
config.plugins.AIPowerFull.target_lang = ConfigText(default="ar")
config.plugins.AIPowerFull.voice = ConfigSelection(
    choices=[("male", "Male Voice"), ("female", "Female Voice")],
    default="male"
)

class AIPowerFullSetup(Screen, ConfigListScreen):
    skin = """
    <screen position="center,center" size="1200,700" title="AI-PowerFull Settings">
        <widget name="config" position="50,150" size="1100,450" />
        <ePixmap position="400,620" pixmap="skin/images/buttons/green.png" size="200,50" />
        <widget source="key_green" render="Label" position="400,620" size="200,50" zPosition="1" font="Regular;24" halign="center" valign="center" />
    </screen>
    """

    def __init__(self, session):
        Screen.__init__(self, session)
        self.setup_title = "AI-PowerFull Settings"
        self["actions"] = ActionMap(["SetupActions"], {
            "cancel": self.close,
            "save": self.save
        })
        self["key_green"] = Label(_("Save"))
        ConfigListScreen.__init__(self, self.createConfigList())

    def createConfigList(self):
        return [
            getConfigListEntry(_("Enable Plugin"), config.plugins.AIPowerFull.enabled),
            getConfigListEntry(_("API Key"), config.plugins.AIPowerFull.api_key),
            getConfigListEntry(_
