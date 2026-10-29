#
# Copyright (C) 2024 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from those products. Most specific first.
$(call inherit-product, $(SRC_TARGET_DIR)/product/core_64_bit_only.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/full_base_telephony.mk)

# Inherit some common Infinity-X stuff.
$(call inherit-product, vendor/infinity/config/common_full_phone.mk)

# Infinity-X Specific Flags
INFINITY_BUILD_TYPE := UNOFFICIAL
INFINITY_MAINTAINER := "sabrinium0"
TARGET_BOOT_ANIMATION_RES := 1080
WITH_GAPPS := true
TARGET_SUPPORTS_BLUR := false

# Inherit from selene device
$(call inherit-product, device/xiaomi/selene/device.mk)

PRODUCT_DEVICE := selene
PRODUCT_NAME := infinity_selene
PRODUCT_BRAND := Xiaomi
PRODUCT_MODEL := Redmi 10
PRODUCT_MANUFACTURER := Xiaomi

PRODUCT_SYSTEM_NAME := selene_global
PRODUCT_SYSTEM_DEVICE := selene

PRODUCT_GMS_CLIENTID_BASE := android-xiaomi

PRODUCT_BUILD_PROP_OVERRIDES += \
    BuildDesc="selene-user 13 TP1A.220624.014 V14.0.7.0.TKUMIXM release-keys" \
    BuildFingerprint=Redmi/selene/selene:12/TP1A.220624.014/V14.0.7.0.TKUMIXM:user/release-keys
    SystemModel=$(PRODUCT_SYSTEM_DEVICE) \
    SystemName=$(PRODUCT_SYSTEM_NAME) \
    ProductModel=$(PRODUCT_SYSTEM_DEVICE) \
    DeviceProduct=$(PRODUCT_SYSTEM_NAME)
