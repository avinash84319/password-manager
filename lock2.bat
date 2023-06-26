cls

@ECHO OFF

title Folder cache

if EXIST "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}" goto UNLOCK

if NOT EXIST cache goto MDLOCKER

goto LOCK

:LOCK

attrib -h -s "cache"

ren cache "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}"

attrib +h +s "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}"

goto End

:UNLOCK

attrib -h -s "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}"

ren "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}" cache

attrib +h +s cache

goto End

:MDLOCKER

md cache

goto End

:End