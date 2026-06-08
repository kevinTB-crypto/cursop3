from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(video_id):

    transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

    for transcript in transcript_list:
        print(
            transcript.language,
            transcript.language_code,
            transcript.is_generated
        )

    transcript = transcript_list.find_transcript(["es", "en"])

    data = transcript.fetch()

    text = " ".join([x["text"] for x in data])

    return text