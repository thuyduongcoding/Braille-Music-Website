import subprocess
import convertedEngine

def convert(image_file, mxl_path = 'mxl', output_path='output'):
    try:
        # Converting image to musicXML file
        mxl_file_path = convertedEngine.convert_to_mxl(image_file, mxl_path)

        # Converting musicXML file to Braille format (.brf)
        # subprocess.run(["python", "convertedEngine.py", "convert_to_braille(mxl_file)"], 
                    #    stdout=open(output_path + "/sheet.brf", "w"))
        convertedEngine.convert_to_braille(mxl_file_path)
                
    except subprocess.CalledProcessError as e:
        print("Error invoking Audiveris.")
        print(f"Return code: {e.returncode}")
        print(f"Output: {e.output}")

# convert('./input/image.png')
