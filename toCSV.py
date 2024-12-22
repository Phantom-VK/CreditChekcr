import pandas as pd


def convertToCSV(details_map_list, channel_name):
    df = pd.DataFrame(details_map_list)
    # No need to convert duration since it's already in minutes
    df.to_csv(f"{channel_name}_RPM_studio_credit_checks.csv", index=False)

