import os
#paths
ffmpeg_path = "E:\\ffmpeg.exe"
root_folder = "E:\\cursos"
intro_file = "E:\\Logo.mp4"
logo_file = "E:\\logo.png"

#time for trimming
trim_duration = 3
#gpu device
gpu_device = 0
#ffmpeg commands
trim_cmd = f'{ffmpeg_path} -y -hwaccel_device {gpu_device} -i "{{input}}" -ss {trim_duration} -c copy "{{output}}"'
export_audio_cmd = f'{ffmpeg_path} -y -hwaccel_device {gpu_device} -i "{{input}}" -ss {trim_duration} -vn -acodec copy "{{output}}"'
extract_audio_cmd = f'{ffmpeg_path} -y -hwaccel_device {gpu_device} -i "{{input}}" -vn -acodec copy "{{output}}"'
merge_audio_cmd = f'{ffmpeg_path} -y -hwaccel_device {gpu_device} -i "{{input1}}" -i "{{input2}}" -filter_complex amix=inputs=2:duration=first:dropout_transition=2 "{{output}}"'
merge_video_cmd = f'{ffmpeg_path} -y -hwaccel_device {gpu_device} -i "{{input1}}" -i "{{input2}}" -i {logo_file} -filter_complex "[0:v]scale=1920:1080[v0];[1:v]scale=1920:1080[v1];[v0][0:a][v1][1:a]concat=n=2:v=1:a=1[v2];[v2][2]overlay=W-w-44:H-h-40" -preset:v medium -b:v 1500k -maxrate:v 2000k -bufsize:v 3000k -c:v h264_nvenc -pix_fmt yuv420p -profile:v high -strict -2 "{{output}}"'
#creating array
mp4_files = []
#do loop
for root, dirs, files in os.walk(root_folder):
    for filename in files:
        if filename.endswith('.mp4') and not filename.startswith('edited_'):
            mp4_files.append(os.path.join(root, filename))

#editing
for mp4_file in mp4_files:
    trimmed_file = os.path.splitext(mp4_file)[0] + "_trimming.mp4"
    trim_cmd_exec = trim_cmd.format(input=mp4_file, output=trimmed_file)
    os.system(trim_cmd_exec)

    trimmed_audio_file = os.path.splitext(mp4_file)[0] + "_trimmed_audio.m4a"
    export_audio_cmd_exec = export_audio_cmd.format(input=trimmed_file, output=trimmed_audio_file)
    os.system(export_audio_cmd_exec)
    
    intro_audio_file = os.path.splitext(intro_file)[0] + ".m4a"
    extract_audio_cmd_exec = extract_audio_cmd.format(input=os.path.join(root_folder, intro_file), output=intro_audio_file)
    os.system(extract_audio_cmd_exec)
    
    merged_audio_file = os.path.splitext(mp4_file)[0] + "_merged_audio.m4a"
    merge_audio_cmd_exec = merge_audio_cmd.format(input1=intro_audio_file, input2=trimmed_audio_file, output=merged_audio_file)
    os.system(merge_audio_cmd_exec)
    
    merged_video_file = os.path.splitext(mp4_file)[0] + "_completo.mp4"
    merge_video_cmd_exec = merge_video_cmd.format(input1=os.path.join(root_folder, intro_file), input2=trimmed_file, output=merged_video_file)
    os.system(merge_video_cmd_exec)
    #remove data
    os.remove(merged_audio_file)
    os.remove(intro_audio_file)
    os.remove(trimmed_audio_file)
    os.remove(trimmed_file)
    os.remove(mp4_file)

    

    
