import CheckCredits
import Config
import toCSV

CHANNEL_ID_LIST = ["UCiWatT8PZJkw7W8K8j6eGsA", "UCcmLksNmHmp4gZmZCA1-DHA", "UCYpT6g8KlLla4Nyzz6UUtkA",
                   "UC3v9Y9VNDyVy1TMr0dUoaMQ", "UCySwejnZVKetHGKS9K5B_fg", "UCFrVi-E_Na2syIPK6e6Trbg",
                   "UCfbTjeLbY49IrOPf3TiwMZQ", "UCA_NIJLe2dNnL4J8M3wrsig"]

if __name__ == "__main__":
    print("Program Started")
    for channel_id in CHANNEL_ID_LIST:
        videos_list, channel_name = CheckCredits.checkVideos(CheckCredits.getResponse(
            api_key=Config.API_KEY,
            channel_id=channel_id
        )
        )

        toCSV.convertToCSV(videos_list, channel_name)
    print("Finished!!")
