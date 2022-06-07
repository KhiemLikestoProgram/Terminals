@Echo off

IF [%1] EQU [] (
    echo Usage: run { {.filetypes} or {file} } [arguments...]
    exit
)
IF %1 EQU .html (
    cd /d "D:\Programming\My programs\html\"
    start chrome "http://localhost:8000" & python -m http.server
    exit
)
IF %1 EQU .python (
    GOTO :python
)
IF %1 EQU .py (
    GOTO :python
)
@REM This is Files
IF %1 EQU txt (
    cd /d "C:\Users\pc\OneDrive\Documents\"
    code %2
    exit
)
IF %1 EQU img (
    cd /d "C:\Users\pc\OneDrive\Pictures\"
    mspaint %2
    exit
)
IF %1 EQU snd (
    cd /d "C:\Users\pc\OneDrive\Music\"
    start /d "C:\Program Files (x86)\Windows Media Player" wmplayer.exe %2
    exit
)
IF %1 EQU vid (
    cd /d "C:\Users\pc\OneDrive\Videos"
    start /d "C:\Program Files (x86)\Windows Media Player" wmplayer.exe %2
    exit
)

:python
python "D:\Programming\My programs\python\%2.py"
exit