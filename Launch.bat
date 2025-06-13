@echo off
COLOR 0A

:menu
echo.
echo   ==============================
echo    SISTEMA DE SINCRONIZACION USB
echo   ==============================
echo.
echo   1) Sincronizar Local a Extraible
echo   2) Sincronizar Extraible a Local
echo   3) Salir
echo.
set /p opcion="   Seleccione una opcion [1-3]: "

if "%opcion%"=="1" goto pctoremote
if "%opcion%"=="2" goto remotetopc
if "%opcion%"=="3" exit /b

echo ¡Opcion invalida! Use 1, 2 o 3.
pause
goto menu

:pctoremote ::Opcion 1
echo.
echo [ Sincronizando de Local a Extraible... ]
python ./code/pctoremote.py
goto fin

:remotetopc ::Opcion 2
echo.
echo [ Sincronizando de Extraible a Local... ]
python ./code/remotetopc.py
goto fin

:fin
echo.
echo Operacion completada. Presione una tecla para continuar...
pause >nul
goto menu