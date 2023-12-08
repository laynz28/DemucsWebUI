import os
import gradio as gr
from scipy.io.wavfile import write


def inference(audio):
  os.makedirs("out", exist_ok=True)
  write('test.wav', audio[0], audio[1])
  os.system("python3 -m demucs.separate -n htdemucs --two-stems=vocals -d cpu test.wav -o out")
  return "./out/htdemucs/test/vocals.wav","./out/htdemucs/test/no_vocals.wav"
    
title = "Ilaria UVR 💖"
description = "Drag and drop an audio file to easily separate it! [Join AI Hub Discord Server](https://discord.gg/aihub).</p>"
article = "Made with 💖 by Ilaria"

examples=[['test.mp3']]
gr.Interface(
    inference, 
    gr.Audio(type="numpy", label="Song"),
    [gr.Audio(type="filepath", label="Vocals"),gr.Audio(type="filepath", label="Instrumentals")],
    title=title,
    description=description,
    article=article,
    examples=examples
    ).launch()