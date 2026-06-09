import whisper
import yt_dlp
import tempfile
import os


def transcribe_file(file_path):

    model = whisper.load_model("base")

    result = model.transcribe(
        file_path,
        language="es"
    )

    return result["text"]


def transcribe_youtube(url):

    temp_dir = tempfile.mkdtemp()

    output_file = os.path.join(
        temp_dir,
        "audio.%(ext)s"
    )

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": output_file,
        "quiet": True
    }

    with yt_dlp.YoutubeDL(
        ydl_opts
    ) as ydl:

        info = ydl.extract_info(
            url,
            download=True
        )

        downloaded_file = ydl.prepare_filename(
            info
        )

    return transcribe_file(
        downloaded_file
    )