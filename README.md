# bonemat_automation
This script automates all operations in Bonemat, including importing DICOM and Ansys CDB file, bonemat operation, and exporting Ansys CDB file.

## About
 The automation is achieved by sending key inputs and click commands using `pyautomation` module.
 You can find the processes of this script in the following youtube link.

* [youtube link - bonemat_automation](https://youtu.be/gvDLe5PDxNw)

## Installing modules
Following modules are required for this script.

```
pip install keyboard
pip install pyautogui
pip install pygetwindow
pip install pyocr
pip install Pillow
```

This script uses OCR for click actions. Please install following OCR module.
* [Link - Tesseract installer for Windows](https://github.com/UB-Mannheim/tesseract/wiki)

## Running
Specify the .exe paths of Bonemat and tesseract

```
bonemat_exe = r"C:\Program Files\BIC Software\Bonemat\bin\Bonemat.exe"
pyocr.tesseract.TESSERACT_CMD = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

Next, provide the following file paths
```
# import data of DICOM and .CDB
path_ctfolder = r"C:\Users\bio1\CTDate\DICOM"
path_cdb = r"C:\Users\bio1\mesh_data.cdb"

# calibration file for converting HU to E in bonemat operation
path_calib = r"C:\Users\bio1\calibration.xml"

# export .cdb file.
# If you want to change the file name, modify the part of "bonemat_mesh".
path_output = r"C:\Users\bio1\bonemat_mesh.cdb"
```
**In large data files, following key input may start before the loading is complete.**
<br>Adjust the load time according to the file size.
```
laodtime_ct = 2
laodtime_cdb = 4
caltime_calib = 3
```

`press_ok_in_calib = 22` is the number of times of "tab" key input to move to "OK" from "open configuration file" in calibration window.
Adjust this value according to your calibration method.
`ex_gap = 20`  is Elasticity Gap value


