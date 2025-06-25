from Plugins.Plugin import PluginDescriptor
from Components.config import config, ConfigSubsection, ConfigText, ConfigYesNo
from Screens.Screen import Screen
from Components.ActionMap import ActionMap
from Components.Label import Label
from .ai_engine import AIEngine
from .utils.helpers import get_logger

# Initialize logger
logger = get_logger()

# Configuration setup
config.plugins.AIPowerFull = ConfigSubsection()
config.plugins.AIPowerFull.enabled = ConfigYesNo(default=True)
config.plugins.AIPowerFull.api_key = ConfigText(default="", fixed_size=False)
config.plugins.AIPowerFull.target_lang = ConfigText(default="ar")

class AIPowerFullScreen(Screen):
    skin = """
    <screen position="center,center" size="800,600" title="AI-PowerFull">
        <widget name="status" position="50,50" size="700,500" font="Regular;28"/>
        <ePixmap position="300,550" pixmap="buttons/red.png" size="140,40"/>
        <widget source="key_red" render="Label" position="300,550" size="140,40" 
               font="Regular;24" halign="center" valign="center"/>
    </screen>"""

    def __init__(self, session):
        Screen.__init__(self, session)
        self["status"] = Label(_("Initializing AI Engine..."))
        self["key_red"] = Label(_("Close"))
        self["actions"] = ActionMap(["ColorActions"], {
            "red": self.close
        })
        self.engine = AIEngine()
        self.onFirstExecBegin.append(self.start_translation)

    def start_translation(self):
        try:
            result = self.engine.translate("Hello world", config.plugins.AIPowerFull.target_lang.value)
            self["status"].setText(_(f"Translation: {result}"))
        except Exception as e:
            logger.error(f"Translation failed: {str(e)}")
            self["status"].setText(_("Error - Check logs"))

def main(session, **kwargs):
    session.open(AIPowerFullScreen)

def Plugins(**kwargs):
    return PluginDescriptor(
        name="AI-PowerFull",
        description="AI Subtitle Translator",
        where=PluginDescriptor.WHERE_PLUGINMENU,
        fnc=main,
        icon="plugin.png"
    )
