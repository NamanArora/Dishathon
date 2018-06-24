from moviepy.editor import *
movie=VideoFileClip('speech.mp4').\
   set_audio(AudioFileClip('converted_speech.mp3'))
movie.write_videofile("new_speech.mp4",codec="mpeg4")
