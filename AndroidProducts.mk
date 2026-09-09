#
# Copyright (C) 2024 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#
# Ayni device tree hem LineageOS hem PixelOS icin kullanilabilsin diye
# iki urun makefile'i de listeleniyor. Eksik olan inherit yolu
# (vendor/lineage vs vendor/custom) yalnizca lunch edilen hedefte
# degerlendirildigi icin bu guvenli.
#
# Surum yapilandirmasi (release config) -- AOSP platform/build/release
# @ android-17.0.0_r1 icinden dogrulandi (2026-09-06):
#     A16 = bp1a ... bp4a
#     A17 = cp1a, cp2a     <-- r1 icin cp1a
#

PRODUCT_MAKEFILES := \
    $(LOCAL_DIR)/lineage_selene.mk \
    $(LOCAL_DIR)/custom_selene.mk

COMMON_LUNCH_CHOICES := \
    lineage_selene-cp1a-userdebug \
    custom_selene-cp1a-userdebug
