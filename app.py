import os
import gradio as gr
from scipy.io.wavfile import write


def inference(audio):
  os.makedirs("out", exist_ok=True)
  write('test.wav', audio[0], audio[1])
  os.system("python3 -m demucs.separate -n htdemucs --two-stems=vocals -d cpu test.wav -o out")
  return "/content/htdemucs/test/vocals.wav","/content/htdemucs/test/no_vocals.wav"
    
title = "DECMUS WebUI"
description = "Drag and drop an audio file to easily separate it!.</p>"
article = "Made with 💖 by Ilaria and laynz28"

examples=[['test.mp3']]
gr.Interface(
    inference, 
    gr.Audio(type="numpy", label="Song"),
    [gr.Audio(type="filepath", label="Vocals"),gr.Audio(type="filepath", label="Instrumentals")],
    title=title,
    description=description,
    article=article,
    examples=examples
    ).launch(Share=True)
