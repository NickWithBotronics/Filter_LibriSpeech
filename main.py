import os
from pydub import AudioSegment

# Prompt user for the speaker type, first file name and starting segment number
speaker = input("Enter speaker (e.g., Man speaking, Woman speaking): ")
first_file = input("Enter the name of the first audio file (e.g., 1624-142933-0000.flac): ")
segment_counter = int(input("Enter the starting segment number (e.g., 18 for segment_018.wav): "))

# Extracting the base name from the first file to get the pattern
base_name = "-".join(first_file.split('-')[:-1])  # e.g., "1624-142933"

# Load text data
text_file_name = f"{base_name}.trans.txt"
with open(text_file_name, 'r') as file:
    text_data = file.readlines()

# Split the lines into a dictionary for easy lookup
text_dict = {}
for line in text_data:
    key, value = line.split(maxsplit=1)
    text_dict[key] = value.strip()

# Process audio
folder_path = os.path.dirname(os.path.abspath(first_file))
audio_files = [f for f in os.listdir(folder_path) if f.startswith(base_name) and f.endswith('.flac')]
audio_files.sort()  # to ensure they're processed in order

combined_audio = AudioSegment.empty()
current_text = ""
output_folder = folder_path  # change to where you want the results if different

for file in audio_files:
    current_audio = AudioSegment.from_file(os.path.join(folder_path, file), format="flac")
    combined_audio += current_audio
    current_text += " " + text_dict[file.split('.')[0]]

    # Check if the combined audio is >= 30 seconds
    if len(combined_audio) >= 30000:  # 30000 milliseconds = 30 seconds
        # Export audio
        output_audio_path = os.path.join(output_folder, f"segment_{segment_counter:03}.wav")
        combined_audio.export(output_audio_path, format="wav")
        # Write text
        with open(os.path.join(output_folder, f"segment_{segment_counter:03}.txt"), 'w') as txt_file:
            txt_file.write(f"{speaker}: {current_text.strip()}")
        # Reset for next segment
        combined_audio = AudioSegment.empty()
        current_text = ""
        segment_counter += 1

# Handle any remaining audio/text that didn't make the last 30-second segment
if len(combined_audio) > 0:
    output_audio_path = os.path.join(output_folder, f"segment_{segment_counter:03}.wav")
    combined_audio.export(output_audio_path, format="wav")
    with open(os.path.join(output_folder, f"segment_{segment_counter:03}.txt"), 'w') as txt_file:
        txt_file.write(f"{speaker}: {current_text.strip()}")

print("Processing complete!")
