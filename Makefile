# AI-PowerFull Plugin Makefile

PLUGIN_NAME = AI-PowerFull
PKG_NAME = enigma2-plugin-extensions-$(PLUGIN_NAME)
PKG_VERSION = 1.0
PKG_RELEASE = 1
PKG_ARCH = all

# Build dependencies
DEPENDS = python3-requests python3-langdetect

# Source files
SRC_DIR = src
SKIN_DIR = skin
META_DIR = meta
LOCALE_DIR = locale

include $(TOPDIR)/rules.mk

PKG_DIR = $(BUILD_DIR)/$(PKG_NAME)-$(PKG_VERSION)

define Package/$(PKG_NAME)
  SECTION = multimedia
  CATEGORY = Multimedia
  TITLE = AI-PowerFull Subtitle Translator
  MAINTAINER = YourName <your@email.com>
  DEPENDS = $(DEPENDS)
  DESCRIPTION = AI-powered subtitle translation and voice dubbing
endef

define Package/$(PKG_NAME)/description
  Real-time AI translation of DVB subtitles with Egyptian Arabic voice support.
  Requires OpenAI API key for full functionality.
endef

define Build/Prepare
    mkdir -p $(PKG_DIR)
    cp -r $(SRC_DIR)/* $(PKG_DIR)/
    cp -r $(SKIN_DIR) $(PKG_DIR)/
    cp -r $(META_DIR) $(PKG_DIR)/
    [ -d $(LOCALE_DIR) ] && cp -r $(LOCALE_DIR) $(PKG_DIR)/ || true
endef

define Package/$(PKG_NAME)/install
    $(INSTALL_DIR) $(1)/usr/lib/enigma2/python/Plugins/Extensions/$(PLUGIN_NAME)
    cp -r $(PKG_DIR)/$(SRC_DIR)/* $(1)/usr/lib/enigma2/python/Plugins/Extensions/$(PLUGIN_NAME)/
    cp -r $(PKG_DIR)/$(SKIN_DIR) $(1)/usr/lib/enigma2/python/Plugins/Extensions/$(PLUGIN_NAME)/
    cp -r $(PKG_DIR)/$(META_DIR) $(1)/usr/lib/enigma2/python/Plugins/Extensions/$(PLUGIN_NAME)/
    [ -d $(PKG_DIR)/$(LOCALE_DIR) ] && cp -r $(PKG_DIR)/$(LOCALE_DIR) $(1)/usr/lib/enigma2/python/Plugins/Extensions/$(PLUGIN_NAME)/ || true
    
    # Set executable permissions
    find $(1)/usr/lib/enigma2/python/Plugins/Extensions/$(PLUGIN_NAME) -name "*.py" -exec chmod 755 {} \;
endef

$(eval $(call BuildPackage,$(PKG_NAME)))
