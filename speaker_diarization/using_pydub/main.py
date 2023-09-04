from pydub import AudioSegment, silence
import numpy as np

# Load audio file
audio = AudioSegment.from_wav("interview.wav")

# Split the stereo audio channels
interviewer_channel = audio.split_to_mono()[0]
candidate_channel = audio.split_to_mono()[1]

# Define a function to detect non-silent chunks
def detect_silence(audio_channel, min_silence_len=500, silence_thresh=-40):
    nonsilent_chunks = silence.detect_silence(audio_channel, min_silence_len=min_silence_len, silence_thresh=silence_thresh)
    return [(start, end) for (start, end) in nonsilent_chunks]

interviewer_times = detect_silence(interviewer_channel)
candidate_times = detect_silence(candidate_channel)

# Calculate duration for each segment in seconds
interviewer_durations = [(end - start) / 1000.0 for (start, end) in interviewer_times]
candidate_durations = [(end - start) / 1000.0 for (start, end) in candidate_times]

print("Interviewer Timestamps:", interviewer_times)
print("Interviewer Durations (in seconds):", interviewer_durations)

print("Candidate Timestamps:", candidate_times)
print("Candidate Durations (in seconds):", candidate_durations)
    