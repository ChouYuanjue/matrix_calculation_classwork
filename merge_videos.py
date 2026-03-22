from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.compositing.CompositeVideoClip import concatenate_videoclips
import pathlib

base = pathlib.Path('media/videos/manim/1080p60')
files = [
    base / 'ConceptErasureFull.mp4',
    base / 'SpectralClusteringDeepDive.mp4',
    base / 'SemanticLogOddsPro.mp4',
]
for f in files:
    if not f.exists():
        raise FileNotFoundError(f"Missing input file: {f}")

clips = [VideoFileClip(str(f)) for f in files]
final = concatenate_videoclips(clips, method='compose')
out = base / 'manim.mp4'
final.write_videofile(str(out), codec='libx264', audio_codec='aac')
for c in clips:
    c.close()
final.close()
