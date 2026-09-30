# Reverse

## `Unity`

### `Il2CppDumper`

需要

1. 可执行文件。`PC`平台是`GameAssembly.dll` 或 `*Assembly.dll`，移动端是`libil2cpp.so`
2. 一个`global-metadata.data`文件

最后自动生成到当前目录下。

现在可以使用`ILspy`、`dnspy`等工具打开`dll`

[Il2CppDumper Tutorial - CSDN Blog](https://blog.csdn.net/inter315/article/details/125382599)

`IDA` 随后读取`GameAssembly`（不是解包后的），然后输入从`dnspy`获得的`RVA`，可以定位到根据汇编代码生成的伪代码。

`xdbg`等工具找到运行时函数地址是根据`GameAssembly.dll`的模块地址（基地址）+`RVA`地址获得到的当前物理地址。

### `xdbg`

`Symbols`模块看基址

`CPU`模块右键`Go to` -> `Expression` 输入计算后的函数地址 （`Ctrl+G`快捷键）

#### 屏蔽异常

![](../../attachments/0f07949a3767dd09c97e8fc4c37de0b6.png)

## `IDA`

`F5` 某段汇编方法转换为`C`代码模式查看

`G` 跳转到地址

`Ctrl+ALT+K` 修改指令（`Key-Patch` -> `Patcher`）

结合`il2CppDumper`

它除了`DummyDll`文件还会生成

![Graphical user interface, text Description automatically generated](../../attachments/76edc5c6459675d8b2bdcb0126a2816b.png)

其中`ida_with_struct_py3.py`脚本可以使用`ida`运行，选择`script.json`，然后选择`il2cpp.h`头文件，运行后`IDA`将会补全函数名

![Graphical user interface, application Description automatically generated](../../attachments/65fd3bdf0ce8572a5cc835fc357c2c74.png)

对于其他语言调用动态链接库的情况，可以去`Exports`去看这个库导出了哪些方法。

![](../../attachments/Pasted%20image%2020230904114624.png)

## PE 文件格式

> 来源：原 `CTF/Reverse/PE逆向.md`（0.9KB 小文件）并入，2026-09 治理，原文件已删除。

`PE`（Portable Execute）文件被称为可移植的执行体（可执行文件），常见的可执行文件有`EXE`、`DLL`、`OCX`、`SYS`、`COM`格式文件，`PE`文件是微软`Windows`平台操作系统上的可执行程序文件。`PE`文件能被`Windows`平台的操作系统解释并执行，因此有固定的文件格式。`PE`文件格式被组织为一个线性的数据流，它由一个`MS-DOS`头部开始，接着是一个实模式的程序残余以及一个`PE`文件标志，这之后紧接着`PE`文件头和可选头部。这些之后是所有的段头部，段头部之后跟随着所有的段实体。文件的结束处是一些其它的区域，其中是一些混杂的信息，包括重分配信息、符号表信息、行号信息以及字串表数据。

`OEP` (Original Entry Point) refers to the point in the code where the program starts executing.