# bonemat_automation
This program automate all operations in Bonemat, including importing DICOM and .CDB, bonemat operation, and exporting .cdb.

## About
 The automation is conducted by sending key input and click commands using `pyautomation` module.
 You can see how to use this script at the following youtube link.

[youtube link - bonemat_automation](hogehoge)

## Installing modules
You need to install following modules.

```
pip install keyboard
pip install pyautogui
pip install pygetwindow
pip install pyocr
pip install Pillow
```

This script also uses OCR for click action. Please install following OCR module.
* [Link - Tesseract installer for Windows](https://github.com/UB-Mannheim/tesseract/wiki)

## Running
Please input .exe paths of Bonemat and tesseract

```
bonemat_exe = r"C:\Program Files\BIC Software\Bonemat\bin\Bonemat.exe"
pyocr.tesseract.TESSERACT_CMD = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

please input following file paths
```
# importing data of DICOM and .CDB
path_ctfolder = r"C:\Users\bio1\CTDate\DICOM"
path_cdb = r"C:\Users\bio1\mesh_data.cdb"

# calibration file for converting HU to E in bonemat operation
path_calib = r"C:\Users\bio1\calibration.xml"

# exporting .cdb file. If you want to change the file name, you can modify the part of "bonemat_mesh".
path_output = r"C:\Users\bio1\bonemat_mesh.cdb"
```
**In large files size data, following process may start before loading is complete.**
<br>please change the load time depending on its file size.
```
laodtime_ct = 2
laodtime_cdb = 4
caltime_calib = 3
```

`press_ok_in_calib = 22` is the press count "tab" to move to "OK" from "open configuration file" in calibration window.
please change the value depending on the calibration method.
`ex_gap = 20`  is Elasticity Gap value


