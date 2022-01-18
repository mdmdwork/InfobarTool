@echo off
cmd /k pyinstaller -F -w -i logo.ico D:\Python\InfobarTool\data\InfobarTool.pyw --version-file=file_version_info.txt --upx-dir=D:\Python\Dabao_tool\upx\upx-3.96-win32 --workpath D:\Python\InfobarTool\pack\tmp --distpath D:\Python\InfobarTool\pack


单文件版：
pyinstaller -F -w -i logo.ico InfobarTool.pyw

多文件版：
pyinstaller -w -i logo.ico InfobarTool.pyw

多文件版+UPX加壳
pyinstaller -w -i logo.ico InfobarTool.pyw --upx-dir=D:\Python\Dabao_tool\upx\upx-3.96-win32

多文件版+版本信息+UPX加壳
pyinstaller -w -i logo.ico --version-file=file_version_info.txt InfobarTool.pyw --upx-dir=D:\Python\Dabao_tool\upx\upx-3.96-win32

单文件版+版本信息+UPX加壳
cmd /k pyinstaller -F -w -i logo.ico D:\Python\InfobarTool\data\InfobarTool.pyw --version-file=file_version_info.txt  --upx-dir=D:\Python\Dabao_tool\upx\upx-3.96-win32


选项参数
-h    显示帮助信息
-v    显示版本号
–distpath    指定打包后的程序存放目录，默认存放在当前目录下的dist目录
–workpath    为输出的所有临时文件指定存放目录
-c    显示命令行窗口
-w    不显示命令行窗口
-D    生成结果是一个包含exe程序的目录，所有第三方依赖库和其他资源和exe程序位于同一目录下
-F    生成结果是一个exe程序，所有第三方依赖库和其他资源都被打包进该exe程序中
-i    为生成的程序指定一个icon图标
-n    指定生成的.exe和.spec文件名

