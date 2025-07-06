from moviepy.editor import TextClip, CompositeVideoClip, ColorClip
import uuid

def generate_reel(prompt: str):
    filename = f"{uuid.uuid4()}.mp4"
    clip = TextClip(prompt, fontsize=70, color='white', size=(720, 1280)).set_duration(5).set_position('center')
    background = ColorClip(size=(720, 1280), color=(0, 0, 0), duration=5)
    final = CompositeVideoClip([background, clip])
    final.write_videofile(f"static/{filename}", fps=24)
    return filename