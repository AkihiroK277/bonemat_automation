# -*- coding: utf-8 -*-
import subprocess

# path of the automate_bm.py
py_file = r"C:\Users\bio1\Desktop\ct_fem\2_script_mpchg_fracSim\2_script\bonemat_automation\automate_bm.py"
py_exe = r"C:\Users\bio1\Desktop\py_mech\.venv\Scripts\python.exe"

bonemat_exe = r"C:\Program Files\BIC Software\Bonemat\bin\Bonemat.exe"  # .exe path of bonemat
pyocr_tesseract_TESSERACT_CMD = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # .exe path of tesseract

path_ctfolder = r"C:\Users\bio1\Desktop\ct_fem\6_script_test\volume"  # folder path of ct images
path_cdb = r"C:\Users\bio1\Desktop\ct_fem\6_script_test\1_1mm\mesh_data.cdb"  # path of .cdb
# path of mesh_data.cdb after analysis
path_cd_cdb = ExtAPI.DataModel.Project.Model.Analyses[0].WorkingDir + "mesh_data.cdb"
arg_cdb_path = path_cdb

path_calib = r"C:\Users\bio1\Desktop\ct_fem\6_script_test\calibration_files\calibration.xml"  # path of CT calibration file
path_output = r"C:\Users\bio1\Desktop\ct_fem\6_script_test\result\bonemat_mesh.cdb" 

args = [bonemat_exe, pyocr_tesseract_TESSERACT_CMD, path_ctfolder, arg_cdb_path, path_calib, path_output]

subprocess.Popen([py_exe, py_file] + args, shell=True)

