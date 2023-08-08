import wave
import os

def get_wav_duration(file_path):
    """Return the duration of a WAV file in seconds."""
    with wave.open(file_path, 'rb') as wf:
        frames = wf.getnframes()
        rate = wf.getframerate()
        duration = frames / float(rate)
        return duration

def get_file_size(file_path):
    """Return the size of a file in bytes."""
    return os.path.getsize(file_path)

def get_total_duration_and_size(directory):
    """Return the total duration and size of all WAV files in a directory."""
    total_duration = 0.0
    total_size = 0
    for foldername, subfolders, filenames in os.walk(directory):
        for filename in filenames:
            if filename.lower().endswith('.wav'):
                file_path = os.path.join(foldername, filename)
                try:
                    total_duration += get_wav_duration(file_path)
                    total_size += get_file_size(file_path)
                except:
                    print(f"Error reading {file_path}. Skipping...")
    return total_duration, total_size

if __name__ == '__main__':
    dir_path = input("Enter the directory path to search for WAV files: ")
    total_seconds, total_bytes = get_total_duration_and_size(dir_path)
    
    # Convert durations
    minutes, seconds = divmod(total_seconds, 60)
    hours, minutes = divmod(minutes, 60)
    
    # Convert sizes
    total_megabytes = total_bytes / (1024 * 1024)  # MB
    total_gigabytes = total_bytes / (1024 * 1024 * 1024)  # GB
    
    print(f"Total duration of WAV files: {hours:.0f} hours, {minutes:.0f} minutes, {seconds:.2f} seconds.")
    print(f"Total size of WAV files: {total_gigabytes:.2f} GB ({total_megabytes:.2f} MB)")

