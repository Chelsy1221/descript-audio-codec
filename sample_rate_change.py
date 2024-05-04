import librosa
import soundfile as sf

# Load the original audio file
y, sr = librosa.load('/Users/tuyingqian/Documents/Job/iflytek/TTS/descript-audio-codec/assets/input/zhaowei-08.wav', sr=48000)  # explicitly set original sample rate

# Resample from 48kHz to 24kHz
y_24k = librosa.resample(y, orig_sr=sr, target_sr=24000)

# Save the resampled audio
sf.write('/Users/tuyingqian/Documents/Job/iflytek/TTS/descript-audio-codec/assets/input/zhaowei-08_24k.wav', y_24k, 24000)
