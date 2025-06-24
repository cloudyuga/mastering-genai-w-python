# 🔊 Wav2Lip Voice Cloning Instructions

## 🎥 Video Preparation

1. Capture your video using the webcam (no audio required):
    ```bash
    python webcam.py
    ```

2. This will generate a file named `input_video.mp4`.

3. Place the `input_video.mp4` file in the `/Wav2Lip` folder — it will be used by `inference.py`.

---

## 🎙️ Audio Preparation

1. Generate audio from GPT-generated text using:
    ```bash
    python input.py
    ```
    This will create `input_gpt_script.wav`.

2. Record your voice using your system’s audio recorder and save it as `ref.wav`.

3. Use this reference file to clone your voice with the generated script audio:
    ```bash
    python voice.py
    ```
    This creates the final `cloned_output.wav`.

---

## 📦 Setup Wav2Lip

1. Clone the Wav2Lip repository:
    ```bash
    git clone https://github.com/Rudrabha/Wav2Lip
    ```

2. Install dependencies:
    ```bash
    pip install -r ./Wav2Lip/requirements.txt
    ```

3. Download the face detection model `s3fd.pth` from [this link](https://www.adrianbulat.com/downloads/python-fan/s3fd-619a316812.pth) and place it inside:
    ```
    Wav2Lip/face_detection/detection/sfd/
    ```

    > ✅ Make sure to rename the downloaded file as:
    ```
    s3fd.pth
    ```

---

## 🚀 Run Inference

Run the following command to generate the final video with synchronized lip movement and cloned voice:

```bash
python inference.py --checkpoint_path checkpoints/wav2lip.pth --face input_video.mp4 --audio cloned_output.wav
```
---

## 🎉 Output
Your first cloned video will be saved as:
Wav2Lip/results/result_voice.mp4

#### Enjoy your AI-generated lip-synced video!

