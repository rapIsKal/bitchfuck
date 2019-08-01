from pydub import AudioSegment
import os
from datetime import datetime


def log(message, logfile):
    message = str(datetime.now()) + ' > ' + message
    print(message)
    logfile.write(message + '\n')

def rename(name, logfile):
    for i in ' 0123456789':
        name = name.replace(i, '')
		
    log('Audio combined file name changed to ' + name, logfile)
    return name

def process(source_directory, destination_directory, logfile):
    for dirname in os.listdir(source_directory):
        path = os.path.join(source_directory, dirname)
        
        if os.path.isdir(path):
            log('Iterating through directory ' + dirname, logfile)
            # NotADirectoryError
            if dirname.endswith('.wav'):
                log('Dirname {} is valid. To be processed.'.format(dirname), logfile)
                combined = AudioSegment.empty()
                log('Creating an empty audio file', logfile)
                for audio_file in os.listdir(os.path.abspath(os.path.join(os.sep, source_directory, dirname))):
                    log('Processing audio file ' + audio_file, logfile)
                    if audio_file.endswith('.wav'):
                        audio_file = AudioSegment.from_wav(os.path.abspath(os.path.join(os.sep, source_directory, dirname, audio_file)))
                    elif audio_files.ednswith('.mp3'):
                        audio_file = AudioSegment.from_mp3(os.path.abspath(os.path.join(os.sep, source_directory, dirname, audio_files)))
                        
                    log('Joining this audio file into main audio file', logfile)
                    combined += audio_file
            
                filename = rename(dirname, logfile)
            
                log('Saving the new combined audio file to ' + filename, logfile)
                combined.export(os.path.join(destination_directory, filename), format='wav')
                log('Iteration through '+ dirname + ' is over \n\n', logfile)
    log('Process end, files saved in destination directory', logfile)

    
def main():
    source_directory = input('Enter the source directory > ')
    destination_directory = input('Enter the destination directory > ')
    
    with open('audiojoiner.log', 'a') as f:
        process(source_directory, destination_directory, f)
        
if __name__=='__main__':
    main()
