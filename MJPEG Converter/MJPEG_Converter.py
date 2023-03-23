import ffmpeg
import os
import subprocess

def unspool_mjpeg_target(file, folder):
    stream = ffmpeg.input(file)
    stream = ffmpeg.output(stream, folder + "frame%3d.jpeg", vcodec='copy')
    ffmpeg.run(stream)

def get_all_metadata(folder, extension):
    for file in os.listdir(folder):
        if file.endswith(extension):
            get_metadata(file)

def get_metadata(file):
    return reformat_metadata(subprocess.check_output(['exiftool', file]))

def reformat_metadata(raw):
    return raw.decode('utf-8')

print(os.path.isfile("C:/Users/Tanner/Desktop/Support Exes/out.mjpeg"))

unspool_mjpeg_target("C:/Users/Tanner/Desktop/Support Exes/out.mjpeg", "C:/Users/Tanner/Desktop/Support Exes/frames")
file_location = "C:/Users/Tanner/Desktop/Support Exes/frames/frame002.jpeg"
print(get_metadata(file_location))