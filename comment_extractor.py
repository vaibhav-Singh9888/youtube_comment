import os
import csv

from dotenv import load_dotenv

load_dotenv()
from googleapiclient.discovery import build

apiKey = os.getenv("API_KEY")
youtube = build("youtube", "v3", developerKey=apiKey)


def comment_threads(channelID):

    comments_list = []

    request = youtube.commentThreads().list(
        part="id,replies,snippet",
        videoId=channelID,
    )
    response = request.execute()
    comments_list.extend(process_comments(response["items"]))

    while response.get("nextPageToken", None):
        request = youtube.commentThreads().list(
            part="id,replies,snippet",
            videoId=channelID,
            pageToken=response["nextPageToken"],
        )
        response = request.execute()
        comments_list.extend(process_comments(response["items"]))

    return comments_list


comments = []


def process_comments(response_items):

    for res in response_items:

        if "replies" in res.keys():
            for reply in res["replies"]["comments"]:
                comment = reply["snippet"]
                comment["commentId"] = reply["id"]
                comments.append(comment)
        else:
            comment = {}
            comment["snippet"] = res["snippet"]["topLevelComment"]["snippet"]
            comment["snippet"]["parentId"] = None
            comment["snippet"]["commentId"] = res["snippet"]["topLevelComment"]["id"]

            comments.append(comment["snippet"])

        make_csv(comments)

    return comments


def make_csv(comment):
    header = comments[0].keys()

    filename = f"comments_dataset.csv"

    with open(filename, "w", encoding="utf8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=header, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(comments)


def main():
    comment_threads("kX3nB4PpJko")


if (__name__) == "__main__":
    main()
