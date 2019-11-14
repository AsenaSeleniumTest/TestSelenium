$upfile = WinGetHandle("Open")
WinActivate($upfile)
ControlFocus($upfile,"","Edit")
;command to send the path to the edittext area in the window
ControlSetText($upfile,"","[CLASS:Edit]","C:\Users\Uziel.Buendia.nscorp\Desktop\Projects\Ligthning\ACE2.0\DataSets\Data Set_619F.bdgr")
ControlClick($upfile,"","[CLASS:Button;INSTANCE:1]")
