# bulk_pyedit
Bulk python video editor with ffmpeg and hardware aceleration


"As I found myself needing to modify multiple video files scattered across different subfolders within a main directory, with the additional task of adding a logo and intro video, I decided to create a Python script to automate the process and save time."

The code automates the process of modifying video files by trimming them, adding an intro video and a logo, and merging them together into a final video file. It uses the FFmpeg library to perform these operations. The paths for FFmpeg, the root folder containing the video files, the intro video, and the logo are defined at the beginning of the code.

The code then creates an array of all the .mp4 files in the root folder and its subfolders that do not already have "edited_" in their filename. It then performs the following operations on each of the video files in the array:

Trims the video file by the specified duration using the "trim_cmd" command and saves the trimmed video as a new file.
Exports the audio from the trimmed video using the "export_audio_cmd" command and saves it as a new file.
Extracts the audio from the intro video using the "extract_audio_cmd" command and saves it as a new file.
Merges the intro audio and trimmed audio using the "merge_audio_cmd" command and saves the merged audio as a new file.
Merges the intro video, trimmed video, and logo using the "merge_video_cmd" command and saves the merged video as a new file.
Removes the intermediate files that were created during the process.
Overall, the code saves time by automating the process of modifying multiple video files and creating a final version with an intro and logo.
