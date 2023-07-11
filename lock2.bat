cls

@ECHO OFF

title Folder db

if EXIST "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}" goto UNLOCK

if NOT EXIST db goto MDLOCKER

goto LOCK

:LOCK

attrib -h -s "db"

ren db "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}"

attrib +h +s "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}"

goto End

:UNLOCK

attrib -h -s "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}"

ren "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}" db

attrib +h +s db

goto End

:MDLOCKER

md db

goto End

:End