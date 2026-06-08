from youtube_transcript_api import YouTubeTranscriptApi


def get_transcript(video_id):

    api = YouTubeTranscriptApi()

    transcript_list = api.list(video_id)

    transcript = transcript_list.find_transcript(["es", "en"])

    data = transcript.fetch()

    text = " ".join(
        item.text if hasattr(item, "text") else item["text"]
        for item in data
    )

    return text