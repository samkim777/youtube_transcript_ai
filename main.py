from youtube_transcript_api import YouTubeTranscriptApi

video_id = '682dDcNcCNM'
transcript = YouTubeTranscriptApi.get_transcript(video_id)
script = []
# Grab all the texts 
for dialogue in transcript:
  script.append(dialogue['text'])



# Filter out any descriptive words like [Music] or [Applause]
filtered_text = []
for sentence in script:
  filtered_text.append(sentence.replace("'",'"'))

dialogue = []
for string in filtered_text:
    if string not in ['[Music]', '[Applause]']:
        dialogue.append(string)



print(" ".join(dialogue))