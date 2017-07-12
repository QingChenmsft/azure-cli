
@ECHO OFF

set /p token="Press Enter to create service"
@ECHO ON

@ECHO OFF
call F:\azurecli\env\Scripts\activate.bat

@ECHO ON
call az sbz application create --app-name sbzdemo --compose-file @f:\test\compose-file.json

set /p token="Press Enter to create service 2"

@ECHO ON
call az sbz application create --app-name sbzdemo3 --compose-file @f:\test\compose-file2.json --ext-file @f:\test\ext.json

set /p token="Press Enter to simulate load on service 2"

@ECHO OFF
call az sbz application update --app-name sbzdemo3
