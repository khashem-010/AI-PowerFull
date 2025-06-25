from Plugins.Plugin import PluginDescriptor
from Components.config import config, ConfigSubsection, ConfigText

config.plugins.AIPowerFull = ConfigSubsection()
config.plugins.AIPowerFull.api_key = ConfigText(default="", fixed_size=False)

def main(session, **kwargs):
    from .ui import AIPowerFullSetupScreen
    session.open(AIPowerFullSetupScreen)

def Plugins(**kwargs):
    return PluginDescriptor(
        name="AI-PowerFull",
        description="AI Subtitle Translator",
        where=PluginDescriptor.WHERE_PLUGINMENU,
        fnc=main,
        icon="plugin.png"
    )
