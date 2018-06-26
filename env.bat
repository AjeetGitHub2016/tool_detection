echo off
set PATH=C:\Users\npuri\AppData\Local\Continuum\miniconda3;%PATH%
set PATH=C:\tree\dependencies\opencv\build\bin;%PATH%
set PATH=c:\users\npuri\appdata\local\programs\python\python35\Scripts;%PATH%
set PATH="C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v9.0";%PATH%
set PATH="C:\tree\dependencies\graphviz-2.38\release\bin";%PATH%
REM set PATH=C:\tree\dependencies\cudnn-9.0-windows10-x64-v7.1\cuda\bin;%PATH%

set CUDA_HOME="C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v9.0"
set CUDA_PATH="C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v9.0"

C:\Users\npuri\AppData\Local\Continuum\miniconda3\Scripts\activate.bat
REM C:\Users\npuri\AppData\Local\Continuum\miniconda3\Scripts\activate.bat tool_detection 

REM activate tool_detection

REM %windir%\System32\cmd.exe "/K" C:\Users\npuri\AppData\Local\Continuum\miniconda3\Scripts\activate.bat C:\Users\npuri\AppData\Local\Continuum\miniconda3

