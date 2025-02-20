"""automating Bonemat operation"""
import os
import re
import subprocess
import sys

import keyboard as ky
import pyautogui as pa
import pygetwindow as gw
import pyocr
import pyocr.builders
from PIL import Image

# receive arguments from command line of Ansys Workbench
# bonemat_exe = sys.argv[1]  # path of bonemat.exe
# pyocr.tesseract.TESSERACT_CMD = sys.argv[2]  # path of tesseract.exe
# path_ctfolder = sys.argv[3]  # path of CT images folder
# path_cdb = sys.argv[4]  # path of Ansys cdb file
# path_calib = sys.argv[5]  # path of calibration file
# path_output = sys.argv[6]  # path of output cdb file

# when you run this script directly, please set the following values
# .exe path of bonemat
bonemat_exe = r"C:\Program Files\BIC Software\Bonemat\bin\Bonemat.exe"
# .exe path of tesseract
pyocr.tesseract.TESSERACT_CMD = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

path_ctfolder = r"C:\Users\bio1\Desktop\hqCT_fe_\01_model\CTDate\DICOM"
path_cdb = r"C:\Users\bio1\Desktop\hqCT_fe_\03_FE\mesh_data.cdb"
path_calib = r"C:\Users\bio1\Desktop\ct_fem\2_script_mpchg_fracSim\2_script\6_hqct_rhoToE_Morgan.xml"
path_output = r"C:\Users\bio1\Desktop\hqCT_fe_\03_FEbonemat_mesh.cdb"

# path of screenshot for OCR
dir_path = os.path.dirname(path_cdb)
screenshot_path = os.path.join(dir_path, "actwin_screenshot.png")

window_title = "Bonemat"

# please change the load time depending on its file size.
laodtime_ct = 2
laodtime_cdb = 4
caltime_calib = 3

# count of press "tab" to move to "OK" from "open configuration file" in calibration window
press_ok_in_calib = 22  # please change the press count depending on calibration method

ex_gap = "20"  # Elasticity Gap value

# US keyboard layout user may need to change: ky.write -> pa.typewrite
input_path = ky.write


def import_ct():
    # pa.sleep(0.5)
    # move to "DICOM"
    pa.press(["alt", "f"])
    pa.press("down", presses=4)
    pa.press("right", presses=2)
    pa.press("enter")
    pa.sleep(0.1)
    # open explorer
    pa.hotkey("shift", "tab")
    input_path(path_ctfolder)
    pa.press("enter")
    # load ct images
    pa.sleep(0.5)
    pa.hotkey("ctrl", "enter")
    pa.sleep(0.1)
    pa.hotkey("ctrl", "enter")
    pa.sleep(laodtime_ct)


def import_cdb():
    pa.click(click_x, click_y)
    pa.press(["tab", "home"])
    # move to "Ansys cdb File"
    pa.press(["alt", "f"])
    pa.press("down", presses=4)
    pa.press(["right", "down", "right", "down", "enter"])
    # open explorer
    pa.sleep(0.1)
    input_path(path_cdb)
    pa.press("enter")
    pa.sleep(laodtime_cdb)


def bonemat_operation():
    # move to bonemat operation
    pa.click(click_x, click_y)
    pa.press(["tab", "end"])
    pa.hotkey("ctrl", "b")
    pa.sleep(0.4)
    # open config
    pa.press("tab", presses=2)
    pa.press("enter")
    pa.sleep(0.1)
    input_path(path_calib)
    pa.press("enter")
    pa.sleep(0.3)
    # press OK
    pa.press("tab", presses=press_ok_in_calib)
    pa.press("enter")
    pa.sleep(caltime_calib)


def export_cdb():
    # move to export cdb
    pa.press(["alt", "f"])
    pa.press("down", presses=5)
    pa.press("right", presses=2)
    pa.press("down", presses=1)
    pa.press("enter")
    pa.sleep(0.1)
    # set Elasticity Gap value
    pa.press("tab", presses=3)
    pa.typewrite(ex_gap)
    pa.press("tab", presses=3)
    pa.press("enter")
    pa.sleep(0.1)
    # paste path
    input_path(path_output)
    pa.press("enter")


def bonemat_window():
    target_win = gw.getWindowsWithTitle(window_title)

    bonemat_windows = {}
    bonemat_windows_name = []
    win_num = 0
    # get bonemat window info
    for win in target_win:
        # get window containing "Bonemat"
        if re.match(window_title, win.title):
            bonemat_windows[win.title] = win_num
            # terminate the program when the same name was detected
            if win.title in bonemat_windows_name:
                pa.confirm(
                    "same name windows were detected.\n you need to close these windows")
                sys.exit()
            bonemat_windows_name.append(win.title)
        win_num += 1

    # activate bonemat window
    if bonemat_windows:
        # select window when several windows exist
        if len(bonemat_windows) > 1:
            bonemat_windows_name.append("cancel")
            window_result = pa.confirm("witch windows do you activate",
                                       buttons=bonemat_windows_name)
            if window_result == "cancel":
                sys.exit()
            selwinname = bonemat_windows[window_result]
            target_win[selwinname].activate()
        else:
            j = bonemat_windows[bonemat_windows_name[0]]
        return True, target_win[j]
    else:  # no "bonemat" window
        return False, None


def press_root_position(active_window):
    pa.sleep(0.1)
    actwin_x, actwin_y, width, height = active_window.box  # get window location
    screenshot = pa.screenshot(region=(actwin_x, actwin_y, width, height))
    screenshot.save(screenshot_path)

    # activate OCR tool
    tools = pyocr.get_available_tools()
    if tools:
        tool = tools[0]
    else:
        sys.exit()

    # run ocr
    img = Image.open(screenshot_path)
    img_g = img.convert("L")  # Gray conversion
    boxs = tool.image_to_string(img_g,
                                lang="eng",
                                builder=pyocr.builders.WordBoxBuilder(tesseract_layout=4))

    # get target_word position
    target_word = "Data"
    for box in boxs:
        if target_word in box.content:
            print("detected")
            (x, y), (w, h) = box.position
            inner_click_x = actwin_x + x + (w-x)/2
            inner_click_y = actwin_y + y + (h-y)/2
            break
    else:
        print("No detected")
        sys.exit()
    return inner_click_x, inner_click_y


# main

# find bonemat window
win_state, bmtwin = bonemat_window()

if win_state is True:  # bonemat window already exists
    result = pa.confirm("do you add CT images?", buttons=["no", "yes"])
    pa.sleep(0.1)
    bmtwin.activate()
    bmtwin.maximize()
    if result == "yes":
        import_ct()
else:  # bonemat dose not run
    # process = subprocess.Popen(bonemat_exe, shell=True)  # run bonemat
    # pa.sleep(4)
    # bmtwin = pa.getActiveWindow()
    # import_ct()
    pa.alert("please launch a Bonemat")
    sys.exit()

# get click position"Data
click_x, click_y = press_root_position(bmtwin)

import_cdb()
bonemat_operation()
export_cdb()
