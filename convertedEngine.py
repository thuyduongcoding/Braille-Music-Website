from music21 import *
import os
import subprocess

"""
Converting image file to musicXML
"""
def convert_to_mxl(image_path, mxl_folder):
    try:
        # script_dir = os.path.dirname(os.path.abspath(__file__))
        audiveris_path = os.path.join("audiveris", "build", "distributions", "Audiveris-5.3-beta",
                                      "bin", "Audiveris.bat")
        
        command = f"{audiveris_path} -batch -sheets 1 -export -output {mxl_folder} {image_path}"
        # print(image_path)
        print(command)
        subprocess.run(command)
        print("Audiveris invocation successful.")

        # Choose the most recent musicXML file
        mxl_extension = '.mxl'

        for filename in os.listdir(mxl_folder):
            if filename.endswith(mxl_extension):
                mxl_path = os.path.join(mxl_folder, filename)
                break
                
    except subprocess.CalledProcessError as e:
        print("Error invoking Audiveris.")
        print(f"Return code: {e.returncode}")
        print(f"Output: {e.output}")
  
    return mxl_path

"""
Converting musicXML file to braille file
"""
def convert_to_braille(mxl_path):
    c = converter.parse(mxl_path)
    # c.show("braille")
    c.write('braille', fp='output/sheet.txt')