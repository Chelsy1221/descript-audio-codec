import wave

wav_file = '/Users/tuyingqian/Documents/Job/iflytek/TTS/descript-audio-codec/assets/input/zhaowei-08.wav'

with wave.open(wav_file, 'r') as wav:
    sample_rate = wav.getframerate()
    print(f"The sample rate is: {sample_rate} Hz")
