#
# Copyright (C) 2026 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#
# PixelOS (seventeen / A17) urun makefile'i -- selene.
# Kaynak: lineage_selene.mk (lineage-23.2) + PixelOS custom_sweet.mk konvansiyonu.
#
# Ad "custom_<cihaz>" OLMAK ZORUNDA: PixelOS'un tum device tree'leri
# (sweet, alioth, garnet @ seventeen) bu adi kullaniyor ve
# vendor/custom/config/*.mk buna gore kurulu.
# Lunch hedefi:  custom_selene-cp1a-userdebug
#   (cp1a = A17 r1 surum yapilandirmasi; A16 bp1a idi. AOSP
#    platform/build/release @ android-17.0.0_r1 icinden dogrulandi.)
#

# Inherit from those products. Most specific first.
# selene 64-bit-only: BoardConfig'de ZYGOTE_FORCE_64 := true
$(call inherit-product, $(SRC_TARGET_DIR)/product/core_64_bit_only.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/full_base_telephony.mk)

# Inherit from selene device
$(call inherit-product, device/xiaomi/selene/device.mk)

# Inherit some common PixelOS stuff.
# NOT: vendor/custom/config/common_full_phone.mk zaten kendi icinde
# vendor/lineage/config/common_full_phone.mk cagiriyor -- ikisini birden
# inherit ETME.
# Go Edition denemesi icin bu satiri common_full_go_phone.mk ile degistir
# (vendor/custom/config/ altinda MEVCUT, dogrulandi 2026-09-06).
$(call inherit-product, vendor/custom/config/common_full_phone.mk)

# vendor/custom/config/common.mk bunu istiyor; verilmezse
# "TARGET_SCREEN_WIDTH is undefined, assuming 1080p" uyarisi basiyor.
# selene paneli 1080x2340.
TARGET_SCREEN_WIDTH := 1080

PRODUCT_NAME := custom_selene
PRODUCT_DEVICE := selene
PRODUCT_BRAND := Xiaomi
PRODUCT_MODEL := Redmi 10
PRODUCT_MANUFACTURER := xiaomi

PRODUCT_SYSTEM_NAME := selene_global
PRODUCT_SYSTEM_DEVICE := selene

PRODUCT_GMS_CLIENTID_BASE := android-xiaomi

# DIKKAT: upstream lineage_selene.mk'de BuildFingerprint satirinin sonunda
# ters bolu YOKTU. Sonuc: SystemModel/SystemName/ProductModel/DeviceProduct
# PRODUCT_BUILD_PROP_OVERRIDES'a hic girmiyor, bunun yerine "SystemModel" adli
# bir make degiskeni tanimlaniyordu. Burada duzeltildi.
PRODUCT_BUILD_PROP_OVERRIDES += \
    BuildDesc="selene-user 13 TP1A.220624.014 V14.0.8.0.TKUINXM release-keys" \
    BuildFingerprint=Redmi/selene/selene:12/TP1A.220624.014/V14.0.8.0.TKUINXM:user/release-keys \
    SystemModel=$(PRODUCT_SYSTEM_DEVICE) \
    SystemName=$(PRODUCT_SYSTEM_NAME) \
    ProductModel=$(PRODUCT_SYSTEM_DEVICE) \
    DeviceProduct=$(PRODUCT_SYSTEM_NAME)
