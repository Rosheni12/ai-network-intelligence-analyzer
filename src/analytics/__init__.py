def __init__(self, dataset_path):
    self.df = pd.read_csv(dataset_path)

    anomaly_file = "data/processed/anomaly_results.csv"

    if os.path.exists(anomaly_file):
        self.anomaly_df = pd.read_csv(anomaly_file)
    else:
        self.anomaly_df = None