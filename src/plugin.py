from Plugins.Plugin import PluginDescriptor
from Components.config import config, ConfigText

config.plugins.AIPowerFull = ConfigSubsection()
config.plugins.AIPowerFull.api_key = ConfigText(default="")

def Plugins(**kwargs):
    return PluginDescriptor(
        name="AI-PowerFull",
        description="AI Subtitle Translator",
        where=PluginDescriptor.WHERE_PLUGINMENU,
        icon="plugin.png"
    )
