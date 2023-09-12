from pyannote.audio import Pipeline
from pyannote.metrics.diarization import DiarizationErrorRate
import numpy as np
import pydub
import torch

diarization_pipeline = Pipeline.from_pretrained('pyannote/speaker-diarization', use_auth_token=True)

def read(f, normalized=False):
    """MP3 to numpy array"""
    a = pydub.AudioSegment.from_mp3(f)
    y = np.array(a.get_array_of_samples())
    if a.channels == 2:
        y = y.reshape((-1, 2))
    if normalized:
        return a.frame_rate, np.float32(y) / 2**15
    else:
        return a.frame_rate, y

sample_rate, np_array = read('interview.mp3')

input_tensor = torch.from_numpy(np_array).float()
outputs = diarization_pipeline(
    {"waveform": input_tensor, "sample_rate": sample_rate}
)

data = outputs.for_json()["content"]

"""
[{'segment': {'start': 0.4978125, 'end': 14.520937500000002},
  'track': 'B',
  'label': 'SPEAKER_00'},
 {'segment': {'start': 20.364687500000002, 'end': 35.3721875},
  'track': 'A',
  'label': 'SPEAKER_01'}]
"""

for i in range(1, len(timedatastamps)):
    previous_speaker, previous_end = data[i-1]["label"], data[i-1]["segment"]["end"]
    curent_speaker, current_start = data[i]["label"], data[i-1]["segment"]["start"]
    if previous_speaker != curent_speaker and (previous_end - current_start) > 5:
        print('Threshold reached, flagged for behaviour analysis')