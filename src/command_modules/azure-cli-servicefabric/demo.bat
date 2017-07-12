
@ECHO OFF

set /p token="Press Enter to create service"
@ECHO ON

@ECHO OFF
call F:\azurecli\env\Scripts\activate.bat

ECHO ON
call az sbz application create --app-name sbzdemo1 --compose-file @f:\test\compose-file.json


set /p token="Press Enter to update service"

@ECHO ON
call az sbz application update --app-name sbzdemo1 --instance 3
