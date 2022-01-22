# -*- mode: python ; coding: utf-8 -*-
# 该文件将同时同时打出【单个可执行文件】和【免安装绿色文件夹】 详情见https://blog.csdn.net/qq_20265805/article/details/105108726


block_cipher = None

# datas标签为外置文件扩展设置
a = Analysis(['D:\\Python\\InfobarTool\\data\\InfobarTool.pyw'],
             pathex=[],
             binaries=[],
             datas=[('D:\\Python\\InfobarTool\\data\\resources\\images\\*', '.\\resources\\images')],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

#######!!!注意点1：加载自己的资源文件#####################
#a.datas += (('D:\\Python\\InfobarTool\\data\\resources\\*','.\\resources'))
#####################################################


pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

# 打包单个可执行文件
#exe1 = EXE(pyz,
#          a.scripts,
#          a.binaries,
#          a.zipfiles,
#          a.datas,
#          [],
#          name='InfobarTool',
#          debug=False,
#          bootloader_ignore_signals=False,
#          strip=False,
#          upx=True,
#          upx_exclude=[],
#          runtime_tmpdir=None,
#          console=False,
#          disable_windowed_traceback=False,
#          target_arch=None,
#          codesign_identity=None,
#          entitlements_file=None , version='file_version_info.txt', icon='D:\\Python\\InfobarTool\\data\\resources\\images\\logo.ico')

# 打包成多文件执行
exe2 = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='InfobarTool',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None , version='file_version_info.txt', icon='D:\\Python\\InfobarTool\\data\\resources\\images\\logo.ico')

# 打包成多文件执行语句2
coll = COLLECT(exe2,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='InfobarTool')