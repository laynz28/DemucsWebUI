![Ilaria AI Suite](./ilariaaisuite.png)
***
[![Static Badge](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Space-s?labelColor=YELLOW&color=FFEA00)](https://huggingface.co/spaces/TheStinger/Ilaria_UVR) [![Static Badge](https://img.shields.io/badge/%F0%9F%A4%97%20HF%20Space-Duplication-s?labelColor=YELLOW&color=FFEA00)](https://huggingface.co/spaces/TheStinger/Ilaria_UVR?duplicate=true) [![Static Badge](https://img.shields.io/badge/GitHub-Source%20Code-s?logo=GitHub)](https://github.com/TheStingerX/Ilaria-UVR) [![Static Badge](https://img.shields.io/badge/AI%20Hub-Discord%20Server-s?logo=Discord&color=%09%237289da)](https://discord.gg/aihub) [![Static Badge](https://img.shields.io/badge/Ko--Fi-s?logo=Ko-Fi&label=Support%20me%20on&labelColor=434b57&color=FF5E5B)](https://ko-fi.com/ilariaowo)
***
<p align="center">
  <h1>Ilaria UVR 💖</h1>
</p>

🎉 Welcome to Ilaria UVR! 🎉  
  
This project leverages various libraries and modules to create a Graphical User Interface (GUI) for vocals and instrumentals separation.  
It's primarily designed for use with HuggingFace Spaces. 🤗   

Ilaria UVR is part of the Ilaria AI Suite wich includes various easy and powerful tools. 💖

## 📦 Installation 📦

To use this project, clone the original Space on Hugging Face.  
Make sure you restart it time to time to keep up with the new updates.

## 🖥️ Usage 🖥️

Once the dependencies are installed automatically, Hugging Face will use app.py to start the user interface.  
From there, you can utilize the various features of the project.

## 🌟 Features 🌟

Ilaria UVR offers a range of features, including:

- 🎤 **Audio Separation**:  
The heart of Ilaria UVR is the demucs module, which performs the heavy lifting of separating the vocal and instrumental tracks from an audio file.  
This is done in the inference function, which takes an audio file as input and returns the paths of the separated vocal and instrumental tracks.

- 🖥️ **User-Friendly Web Interface**:  
The application uses the gradio module to create an intuitive web interface.  
Users can easily upload an audio file, and the application will return the separated vocal and instrumental tracks.

- 📂 **Efficient File Handling**:  
The application employs the os and scipy.io.wavfile modules for efficient file handling operations.
It creates a directory for output files if it doesn’t already exist, writes the input audio to a file, and returns the paths of the separated audio files.

- 🥇 **Voted for Best Quality**:  
This application stands out for its superior quality of audio separation.
It has been voted by users as the best among other Spaces on Hugging Face for delivering a higher quality of separation between vocal and instrumental tracks, providing a clearer and more distinct output.

- ⚡ **Fast Processing Speed**:  
Speed is another area where this application shines. It processes audio files faster than other spaces on HuggingFace, allowing users to get their separated tracks in less time.

## 🙏 Credits 🙏

- **akhaliq** - For composing the original Gradio UI

## 🤝 Contributing 🤝

Interested in contributing to this project? Ilaria is always looking for collaborators.  
Feel free to open a pull request on Hugging Face.

## 📄 License 📄

This project is released under the `INCU` license.  
For more details, please check the license file.  
For further questions feel free to contact Ilaria.
