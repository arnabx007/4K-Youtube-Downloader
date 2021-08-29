# 4K-Youtube-Downloader
Download the max resolution youtube videos with audio. 

Youtube switched to separate audio/video streaming technology for higher quality formats and no longer provides direct 720p/1080p/1440p mp3 streams. Most of the youtube downloader available online can't download high resolution videos with audio. So I tried to do it with python with these two packages:-

`pytube` - library (and command-line utility) for downloading YouTube videos

`FFmpeg` - a command-line tool, designed for processing of video and audio files

Download the latest FFmpeg build from here:- https://github.com/BtbN/FFmpeg-Builds/releases and extract it.

> FFmpeg doesn’t work directly on Windows 10. You need to add a program to system path using Environment Variables. To use FFmpeg, you need first to add the bin folder containing the FFmpeg executable file to your Windows path.
>
>In the Windows search menu, type Edit the system environment variables and click Enter. This will open the system properties window.
>
>Navigate to Advanced button and click Environment Variables at the bottom of the window.
>
>In the Environment Variables window, Select the variable Path and click Edit to change the Path variable.
>
>Click New and type the path of FFmpeg folder e.g.“C:\ffmpeg\bin\” and click OK.
>
>Launch Command Prompt and type the command ffmpeg in the command prompt terminal and hit Enter to verify.


Run `pip install requirements.txt` to install the required packages.

Set the `output_dir` in the download.py script where the videos will be saved.

Run `python download.py` in command prompt to download a video. Then input the video link.
Then it will show all the available resolutions for the video. Upon selecting the desired resolution It will download the audio and video file seperately and the merge it for you and save it to the output directory. 

![alt text](https://github.com/arnabx007/4K-Youtube-Downloader/blob/master/sample.jpg "")
