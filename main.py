import threading
import CheckCredits
import Config
import toCSV

CHANNEL_ID_LIST = [
    "UCiWatT8PZJkw7W8K8j6eGsA",
    "UCcmLksNmHmp4gZmZCA1-DHA",
    "UCYpT6g8KlLla4Nyzz6UUtkA",
    "UC3v9Y9VNDyVy1TMr0dUoaMQ",
    "UCySwejnZVKetHGKS9K5B_fg",
    "UCFrVi-E_Na2syIPK6e6Trbg",
    "UCfbTjeLbY49IrOPf3TiwMZQ",
    "UCA_NIJLe2dNnL4J8M3wrsig"
]


def process_channel(channel_id):
    try:
        # getResponse now only returns videos, so we don't need to unpack two values
        videos = CheckCredits.getResponse(
            api_key=Config.API_KEY,
            channel_id=channel_id
        )
        videos_list, channel_name = CheckCredits.checkVideos(videos)
        toCSV.convertToCSV(videos_list, channel_name)
        print(f"Finished processing channel: {channel_name}")
    except Exception as e:
        print(f"Error processing channel {channel_id}: {e}")


if __name__ == "__main__":
    print("Program Started")

    threads = []
    for channel_id in CHANNEL_ID_LIST:
        thread = threading.Thread(target=process_channel, args=(channel_id,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("All channels processed. Finished!!")
