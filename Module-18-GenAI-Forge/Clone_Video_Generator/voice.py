import subprocess

# Paths to files
ref_audio = "ref1.wav"
input_audio = "input_gpt_script.wav"
output_audio = "cloned_output.wav"

# Device (use 'cpu' or 'cuda' if you have a GPU)
device = "cpu"

# Run the command
command = [
    "python", "-m", "openvoice_cli", "single",
    "-i", input_audio,
    "-r", ref_audio,
    "-o", output_audio,
    "-d", device
]

# Execute it
try:
    subprocess.run(command, check=True)
    print("✅ Voice cloning complete. Output saved to", output_audio)
except subprocess.CalledProcessError as e:
    print("❌ Failed to run openvoice-cli:", e)
