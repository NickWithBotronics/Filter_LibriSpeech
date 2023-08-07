# Filter_LibriSpeech
 Filtering LibriSpeech dataset can be a hard task this is a script that will help you 
Audio File Processor
This script is designed to process a dataset of .flac audio files from audiobooks and generate combined audio segments of a minimum of 30 seconds each in .wav format. For each audio segment, it creates a corresponding text segment, detailing the words spoken. The processed files are saved in a user-defined format.

How It Works:
User Input:
The user provides:

The type of speaker (e.g., "Man speaking", "Woman speaking").
The name of the first audio file in the dataset. The script automatically deduces the naming pattern for the subsequent files.

If you want to continue the segment enter the number you left off on or enter 0 to start saving the files from 0

Text Data Loading:
Based on the provided first audio file, the script identifies and loads the associated transcript text file. This file contains mappings of file names to the spoken content.

Audio File Processing:
The audio files are sequentially combined until a cumulative duration of at least 30 seconds is reached for each segment.

Segment Generation:
Each combined audio segment is saved in .wav format. A corresponding text file is also generated, which describes the content of the audio segment with the provided speaker type.

Completion:
After processing all files, the script informs the user that the operation is complete.
