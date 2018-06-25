reg add "HKEY_CURRENT_USER\Control Panel\Desktop" /v ForegroundFlashCount /t reg_dword /d 3 /f
reg add "HKEY_CURRENT_USER\Control Panel\Desktop" /v ForegroundLockTimeout /t reg_dword /d 0 /f

PAUSE ON