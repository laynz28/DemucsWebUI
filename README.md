
[![Static Badge](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Space-s?labelColor=YELLOW&color=FFEA00)](https://huggingface.co/spaces/TheStinger/Ilaria_UVR) 


<p align="center">
  <h1> DECMUS WEBUI </h1>
</p>

🎉 Welcome to DECMUS WEBUI! 🎉  
  
This project leverages various libraries and modules to create a Graphical User Interface (GUI) for vocals and instrumentals separation.  
It's primarily designed for use with HuggingFace Spaces. 🤗   


## 🌟 Features 🌟

DECMUS WEBUI offers a range of features, including:

- 🎤 **Audio Separation**:  
The heart of DECMUS WEBUI is the demucs module, which performs the heavy lifting of separating the vocal and instrumental tracks from an audio file.  
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
- - **TheStingerX** - For original creator of Ilaria-UVR

## 🤝 Contributing 🤝

Interested in contributing to this project? Ilaria is always looking for collaborators.  
Feel free to open a pull request on Hugging Face.

## 📄 License 📄

This project is released under the `MIT` license.  
For more details, please check the license file.  
For further questions feel free to contact [Laynz2](github.com/laynz28).
