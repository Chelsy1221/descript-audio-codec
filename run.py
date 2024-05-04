import dac
from audiotools import AudioSignal

# Download a model
model_path = dac.utils.download(model_type="24khz")
model = dac.DAC.load(model_path)

model.to('cpu')

# Load audio signal file
signal = AudioSignal('/app/assets/input/zhaowei-08_24k.wav')

# Encode audio signal as one long file
# (may run out of GPU memory on long files)
signal.to(model.device)

x = model.preprocess(signal.audio_data, signal.sample_rate)
z, codes, latents, _, _ = model.encode(x)

# Decode audio signal
y = model.decode(z)

# Alternatively, use the `compress` and `decompress` functions
# to compress long files.

signal = signal.cpu()
x = model.compress(signal)

# Save and load to and from disk
x.save("compressed.dac")
x = dac.DACFile.load("compressed.dac")

# Decompress it back to an AudioSignal
y = model.decompress(x)

# Write to file
y.write('/app/assets/input/output.wav')