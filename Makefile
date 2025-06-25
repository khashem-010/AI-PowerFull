PLUGIN = AI-PowerFull
include $(TOPDIR)/rules.mk

PKG_NAME := enigma2-plugin-extensions-ai-powerfull
PKG_VERSION := 1.0
PKG_RELEASE := 1

include $(INCLUDE_DIR)/package.mk

define Package/$(PKG_NAME)
  SECTION := multimedia
  CATEGORY := Multimedia
  TITLE := AI-PowerFull Translator
  DEPENDS := +python3-requests
endef

define Package/$(PKG_NAME)/install
    $(INSTALL_DIR) $(1)/usr/lib/enigma2/python/Plugins/Extensions/$(PLUGIN)
    cp -r $(PKG_BUILD_DIR)/src/* $(1)/usr/lib/enigma2/python/Plugins/Extensions/$(PLUGIN)/
endef

$(eval $(call BuildPackage,$(PKG_NAME)))
