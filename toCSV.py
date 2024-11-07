import pandas as pd


def convertToCSV(details_map_list, channel_name):
    df = pd.DataFrame(details_map_list)
    df.to_csv(f"{channel_name}_RPM_studio_credit_checks.csv")
