@echo off
:用spec文件打包
cmd /k pyinstaller --clean InfobarTool_all.spec --workpath D:\Python\InfobarTool\pack\tmp --distpath D:\Python\InfobarTool\pack --upx-dir=D:\Python\upx\upx-3.96-win32
:直接打包
:cmd /k pyinstaller -F -w -i D:\Python\InfobarTool\data\resources\images\logo.ico D:\Python\InfobarTool\data\InfobarTool.pyw --version-file=file_version_info.txt --upx-dir=D:\Python\upx\upx-3.96-win32 --workpath D:\Python\InfobarTool\pack\tmp --distpath D:\Python\InfobarTool\pack

单文件版：
pyinstaller -F -w -i logo.ico InfobarTool.pyw

多文件版：
pyinstaller -w -i logo.ico InfobarTool.pyw

多文件版+UPX加壳
pyinstaller -w -i logo.ico InfobarTool.pyw

多文件版+版本信息+UPX加壳
pyinstaller -w -i logo.ico --version-file=file_version_info.txt InfobarTool.pyw

单文件版+版本信息+UPX加壳
pyinstaller -F -w -i D:\Python\InfobarTool\data\resources\images\logo.ico D:\Python\InfobarTool\data\InfobarTool.pyw --version-file=file_version_info.txt --workpath D:\Python\InfobarTool\pack\tmp --distpath D:\Python\InfobarTool\pack

参数	   说明
-F	   产生单个的可执行文件
-i	   为生成的程序指定一个icon图标
-D	   产生一个目录（包含多个文件）作为可执行程序
-a	   不包含 Unicode 字符集支持
-d	   debug 版本的可执行文件
-w	   指定程序运行时不显示命令行窗口（仅对 Windows 有效）
-c	   指定使用命令行窗口运行程序（仅对 Windows 有效）
-p	   设置 Python 导入模块的路径（和设置 PYTHONPATH 环境变量的作用相似）。也可使用路径分隔符（Windows 使用分号，Linux 使用冒号）来分隔多个路径
-n	   指定项目（产生的 spec）名字。如果省略该选项，那么第一个脚本的主文件名将作为 spec 的名字
-o	   指定 spec 文件的生成目录。如果没有指定，则默认使用当前目录来生成 spec 文件
–-distpath	指定打包后的程序存放目录，默认存放在当前目录下的dist目录
–-workpath	为输出的所有临时文件指定存放目录
--version-file=file_version_info.txt	指定版本文件所在路径
--upx-dir=D:\Python\upx\upx-3.96-win32	指定upx使用目录

