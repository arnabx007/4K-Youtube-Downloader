from pytube import YouTube 
from pytube.cli import on_progress
import os
import ffmpeg


output_dir = r'C:\Users\Arnab\Downloads\videos/'
print(output_dir)

def download_video(url, 
                   audio=True,  
                   output_path=None):
    
    try: 
        video = YouTube(url, on_progress_callback= on_progress) 
    except: 
        print("Connection Error")
        
    '''Print some information about the video'''
    print('\nVideo Title:', video.title)
    print('Uploaded by:', video.author)
    print('Video Length:', round(video.length/60, 2), 'minutes\n')
    
    cleaned_title =  video.title.replace('|', '').replace('/', '').replace('\\', '')\
                            .replace('\"', '').replace('?', '')\
                            .replace('*', '').replace(':', '')
    
    # Get all the videos streams
    video_streams = video.streams.filter(type='video',
                                        progressive=False).order_by('resolution').desc()
    
    # Show the available resolutions
    for i,s in enumerate(video_streams):
        print(f'{i}. {s.resolution},{s.fps}fps')
    
    # Ask for the index of the resolution to be downloaded
    index = int(input('Enter the number of the resolution you want to download: '))
    
    '''Download audio first'''
    if audio==True:
        audio_streams = video.streams.filter(only_audio=True)

        download_stream = audio_streams[0].download(output_path, 
                                              filename=video.author+'_'+cleaned_title+'.mp3', 
                                              max_retries=1)

        mp4 = os.path.abspath(download_stream)
        base, ext = os.path.splitext(mp4)
        os.rename(mp4, base+'.mp3')
        print('Audio Download Complete')
        
    
    '''Now download the video'''
    print('Filesize:', video_streams[index].filesize/1000000, 'MB')

    print('Now downloading ---', video.title)

    download_stream = video_streams[index].download(output_path=output_path, 
                                          filename=video.author+'_'+cleaned_title+'.mp4', 
                                          max_retries=1)
    
    print('Video Download Complete')


def merge(remove=True):
    '''get the files inside temp directory'''
    temp_files = os.listdir(temp_output_dir)
    audio_filepath = os.path.join(temp_output_dir, temp_files[0])
    video_filepath = os.path.join(temp_output_dir, temp_files[1])

    '''ffmpeg to merge audio and video
    Check if the video has already been merged'''
    if temp_files[1] not in os.listdir(output_dir):
        print('Merging...')
        video = ffmpeg.input(video_filepath)
        audio = ffmpeg.input(audio_filepath)

        out = ffmpeg.output(audio, 
                            video, 
                            output_dir+temp_files[1], 
                            vcodec='copy', 
                            acodec='aac', 
                            strict='experimental')

        out.global_args('-loglevel', 'quiet').run()
        print('Merging Cmplete')
    else:
        print('Video already exists')
        
    if remove:
        os.remove(audio_filepath)
        os.remove(video_filepath)



def main():
    # link of the video to be downloaded 
    url = input('Enter the link: \n')

    download_video(url, audio=True, output_path=temp_output_dir)
    merge(remove=True)

    print(f'\nVideo saved at {output_dir}\n')


if __name__=='__main__':

    # Create a temporary directory inside download directory to store mp3 and mp4 files seperately
    if 'temp' not in os.listdir(output_dir):
        os.mkdir(output_dir+'temp')
        temp_output_dir =  output_dir+'temp/'
    else:
        temp_output_dir =  output_dir+'temp/'

        
    main()