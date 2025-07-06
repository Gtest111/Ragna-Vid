# import os
# from yt_dlp import YoutubeDL

# def download_audio(url: str, output_path: str = "cache/audio/audio.mp3") -> str:
#     os.makedirs(os.path.dirname(output_path), exist_ok=True)

#     ydl_opts = {
#         'format': 'bestaudio/best',
#         'outtmpl': output_path,
#         'ffmpeg_location': 'C:/ffmpeg-7.1.1-essentials_build/bin',  # 🛠️ Set here
#         'postprocessors': [{
#             'key': 'FFmpegExtractAudio',
#             'preferredcodec': 'mp3',
#             'preferredquality': '192',
#         }],
#         'quiet': True,
#         'noplaylist': True
#     }

#     try:
#         with YoutubeDL(ydl_opts) as ydl:
#             ydl.download([url])
#         return output_path
#     except Exception as e:
#         print(f"[Error] Failed to download audio: {e}")
#         return None


import os
import hashlib
from yt_dlp import YoutubeDL

def download_audio(url: str, cache_dir: str = "cache/audio") -> str:
    os.makedirs(cache_dir, exist_ok=True)

    # Generate a unique filename based on URL hash
    video_hash = hashlib.md5(url.encode()).hexdigest()[:8]
    output_base = os.path.join(cache_dir, video_hash)
    output_path = f"{output_base}.mp3"

    # Remove existing stale audio
    if os.path.exists(output_path):
        print(f"🧹 Removing old cached audio: {output_path}")
        os.remove(output_path)

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f"{output_base}.%(ext)s",  # will be converted to .mp3
        'ffmpeg_location': 'C:/ffmpeg-7.1.1-essentials_build/bin',  # ✔️ your ffmpeg path
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': True,
        'noplaylist': True
    }

    try:
        print(f"⬇️ Downloading audio for: {url}")
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        # Validate saved file
        if os.path.exists(output_path) and os.path.getsize(output_path) > 10_000:
            print(f"✅ Audio downloaded: {output_path}")
            return output_path
        else:
            print(f"❌ Download failed or file too small: {output_path}")
            return None

    except Exception as e:
        print(f"❌ Exception during download: {e}")
        return None
