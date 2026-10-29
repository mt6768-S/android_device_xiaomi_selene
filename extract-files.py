#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)

from extract_utils.fixups_lib import (
    lib_fixup_remove,
    lib_fixups,
    lib_fixups_user_type,
)

from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

import extract_utils.tools
extract_utils.tools.DEFAULT_PATCHELF_VERSION = '0_17_2'

namespace_imports = [
    'device/xiaomi/selene',
    'hardware/google/interfaces',
    'hardware/google/pixel/pixelstats',
    'hardware/google/pixel/power-libperfmgr',
    'hardware/google/pixel/thermal',
    'hardware/lineage/interfaces/power-libperfmgr',
    'hardware/mediatek',
    'hardware/mediatek/libmtkperf_client',
    'hardware/mediatek/libaedv',
    'hardware/xiaomi',
]

blob_fixups: blob_fixups_user_type = {
    ('vendor/lib64/libalLDC.so', 'vendor/lib64/libalhLDC.so'): blob_fixup()
       .clear_symbol_version('AHardwareBuffer_allocate')
       .clear_symbol_version('AHardwareBuffer_describe')
       .clear_symbol_version('AHardwareBuffer_lock')
       .clear_symbol_version('AHardwareBuffer_release')
       .clear_symbol_version('AHardwareBuffer_unlock'),
    'vendor/lib64/hw/vulkan.mt6765.so' : blob_fixup()
        .clear_symbol_version('__aeabi_memcpy')
        .clear_symbol_version('__aeabi_memset')
        .clear_symbol_version('__gnu_Unwind_Find_exidx'),
    ('vendor/bin/hw/camerahalserver', 'vendor/lib64/libmtkcam_stdutils.so', 'vendor/lib64/hw/android.hardware.camera.provider@2.6-impl-mediatek.so', 'vendor/lib64/hw/vendor.mediatek.hardware.pq@2.13-impl.so'): blob_fixup()
        .replace_needed('libutils.so', 'libutils-v32.so'),
    'vendor/bin/hw/mtkfusionrild' : blob_fixup()
        .add_needed('libutils-v32.so'),
    'vendor/bin/hw/android.hardware.media.c2@1.2-mediatek-64b': blob_fixup()
        .replace_needed('libavservices_minijail_vendor.so', 'libavservices_minijail.so')
        .replace_needed('libcodec2_hidl@1.0.so', 'libcodec2_hidl@1.0-v31.so')
        .replace_needed('libcodec2_hidl@1.1.so', 'libcodec2_hidl@1.1-v31.so')
        .replace_needed('libcodec2_hidl@1.2.so', 'libcodec2_hidl@1.2-v31.so')
        .replace_needed('libcodec2_vndk.so', 'libcodec2_vndk-v31.so'),
    'vendor/lib64/libcodec2_hidl@1.0-v31.so': blob_fixup()
        .replace_needed('libstagefright_bufferqueue_helper.so', 'libstagefright_bufferqueue_helper-v31.so')
        .replace_needed('libcodec2_hidl_plugin.so', 'libcodec2_hidl_plugin-v31.so')
        .replace_needed('libcodec2_vndk.so', 'libcodec2_vndk-v31.so')
        .replace_needed('libui.so', 'libui-v32.so')
        .add_needed('libbase_shim.so'),
    'vendor/lib64/libcodec2_hidl@1.1-v31.so': blob_fixup()
        .replace_needed('libstagefright_bufferqueue_helper.so', 'libstagefright_bufferqueue_helper-v31.so')
        .replace_needed('libcodec2_hidl@1.0.so', 'libcodec2_hidl@1.0-v31.so')
        .replace_needed('libcodec2_hidl_plugin.so', 'libcodec2_hidl_plugin-v31.so')
        .replace_needed('libcodec2_vndk.so', 'libcodec2_vndk-v31.so')
        .replace_needed('libui.so', 'libui-v32.so')
        .add_needed('libbase_shim.so'),
    'vendor/lib64/libcodec2_hidl@1.2-v31.so': blob_fixup()
        .replace_needed('libstagefright_bufferqueue_helper.so', 'libstagefright_bufferqueue_helper-v31.so')
        .replace_needed('libcodec2_hidl@1.0.so', 'libcodec2_hidl@1.0-v31.so')
        .replace_needed('libcodec2_hidl@1.1.so', 'libcodec2_hidl@1.1-v31.so')
        .replace_needed('libcodec2_hidl_plugin.so', 'libcodec2_hidl_plugin-v31.so')
        .replace_needed('libcodec2_vndk.so', 'libcodec2_vndk-v31.so')
        .replace_needed('libui.so', 'libui-v32.so')
        .add_needed('libbase_shim.so'),
    'vendor/lib64/libcodec2_hidl_plugin-v31.so': blob_fixup()
        .replace_needed('libcodec2_vndk.so', 'libcodec2_vndk-v31.so'),
    ('vendor/lib64/libcodec2_mtk_c2store.so', 'vendor/lib64/libcodec2_vpp_qt_plugin.so', 'vendor/lib64/libcodec2_vpp_rs_plugin.so'): blob_fixup()
        .replace_needed('libcodec2_soft_common.so', 'libcodec2_soft_common-v31.so')
        .replace_needed('libcodec2_vndk.so', 'libcodec2_vndk-v31.so')
        .replace_needed('libstagefright_foundation.so', 'libstagefright_foundation-v33.so')
        .replace_needed('libsfplugin_ccodec_utils.so', 'libsfplugin_ccodec_utils-v31.so'),
    ('vendor/lib64/libcodec2_mtk_vdec.so', 'vendor/lib64/libcodec2_mtk_venc.so'): blob_fixup()
        .replace_needed('libcodec2_soft_common.so', 'libcodec2_soft_common-v31.so')
        .replace_needed('libcodec2_vndk.so', 'libcodec2_vndk-v31.so')
        .replace_needed('libformatter.so', 'libformatter_mtk.so')
        .replace_needed('libstagefright_foundation.so', 'libstagefright_foundation-v33.so')
        .replace_needed('libsfplugin_ccodec_utils.so', 'libsfplugin_ccodec_utils-v31.so')
        .replace_needed('libui.so', 'libui-v32.so'),
    'vendor/lib64/libcodec2_soft_common-v31.so': blob_fixup()
        .replace_needed('libcodec2_vndk.so', 'libcodec2_vndk-v31.so')
        .replace_needed('libstagefright_foundation.so', 'libstagefright_foundation-v33.so')
        .replace_needed('libsfplugin_ccodec_utils.so', 'libsfplugin_ccodec_utils-v31.so'),
    'vendor/lib64/libcodec2_vndk-v31.so': blob_fixup()
        .replace_needed('libui.so', 'libui-v32.so')
        .replace_needed('libstagefright_foundation.so', 'libstagefright_foundation-v33.so'),
    'vendor/lib64/libsfplugin_ccodec_utils-v31.so': blob_fixup()
        .replace_needed('libcodec2_vndk.so', 'libcodec2_vndk-v31.so'),
    'vendor/lib64/hw/vendor.mediatek.hardware.pq@2.13-impl.so': blob_fixup()
        .replace_needed('libtinyxml.so', 'libtinyxml-v34.so'),
    'vendor/lib64/libmnl_mtk.so' : blob_fixup()
        .add_needed('libcutils.so'),
    'vendor/bin/mnld' : blob_fixup()
        .replace_needed('libsensorndkbridge.so', 'android.hardware.sensors@1.0-convert-shared.so')
        .replace_needed('libmnl.so', 'libmnl_mtk.so'),
    ('vendor/lib64/libaalservice.so', 'vendor/lib64/libcam.utils.sensorprovider.so', 'vendor/lib64/hw/vendor.mediatek.hardware.pq@2.13-impl.so'): blob_fixup()
        .replace_needed('libsensorndkbridge.so', 'android.hardware.sensors@1.0-convert-shared.so'),
    ('vendor/bin/hw/android.hardware.gnss-service.mediatek', 'vendor/lib64/hw/android.hardware.gnss-impl-mediatek.so'): blob_fixup()
        .replace_needed('android.hardware.gnss-V1-ndk_platform.so', 'android.hardware.gnss-V1-ndk.so'),
    'vendor/bin/hw/android.hardware.memtrack-service.mediatek' : blob_fixup()
        .replace_needed('android.hardware.memtrack-V1-ndk_platform.so', 'android.hardware.memtrack-V1-ndk.so'),
    'vendor/lib/hw/audio.primary.mt6768.so' : blob_fixup()
        .replace_needed('libalsautils.so', 'libalsautils-v31.so'),
    'vendor/lib64/hw/hwcomposer.mt6768.so' : blob_fixup()
        .add_needed('libprocessgroup_shim.so'),
    'vendor/lib64/libgoodixhwfingerprint.so' : blob_fixup()
        .replace_needed('libvendor.goodix.hardware.biometrics.fingerprint@2.1.so', 'vendor.goodix.hardware.biometrics.fingerprint@2.1.so'),
    'vendor/lib64/libvendor.goodix.hardware.biometrics.fingerprint@2.1.so' : blob_fixup()
        .replace_needed('libhidlbase.so', 'libhidlbase-v32.so'),
    ('vendor/lib64/libSQLiteModule_VER_ALL.so', 'vendor/lib64/lib3a.flash.so', 'vendor/lib/libteei_daemon_vfs.so', 'vendor/lib64/libteei_daemon_vfs.so'): blob_fixup()
        .add_needed('liblog.so'),
    ('vendor/lib/libnvram.so', 'vendor/lib64/libnvram.so', 'vendor/lib64/libsysenv.so'): blob_fixup()
        .add_needed('libbase_shim.so'),
    'vendor/lib64/libgf_hal.so': blob_fixup()
        .binary_regex_replace(
            b'\x00\x14\xa0\x83\x5f\xb8\xfd\x7b\x43\xa9\xff\x03\x01\x91\xc0\x03\x5f\xd6\xff\x83\x01\xd1\xfd\x7b\x05\xa9\xfd\x43\x01\x91',
            b'\x00\x14\xa0\x83\x5f\xb8\xfd\x7b\x43\xa9\xff\x03\x01\x91\xc0\x03\x5f\xd6\x00\x00\xe0\xd2\xc0\x03\x5f\xd6\xfd\x43\x01\x91',
        ),
    'vendor/etc/vintf/manifest/manifest_media_c2_V1_2_default.xml': blob_fixup()
        .regex_replace('1.1', '1.2'),
}  # fmt: skip

module = ExtractUtilsModule(
    'selene',
    'xiaomi',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
    add_firmware_proprietary_file=False,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
