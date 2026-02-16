class AnomalyDetector:
    def __init__(self,values,statistics_calculator):
        self.values = values
        self.stats = statistics_calculator

    def z_score(self,value):
        mean_value = self.stats.mean()
        std_dev = self.stats.standard_deviation()

        return (value - mean_value) / std_dev

    def detect_anomalies(self):
        results = []

        for value in self.values:
            z = self.z_score(value)

            if abs(z) > 3:
                results.append((value,"ANOMALY",z))
            elif abs(z) > 2:
                results.append((value,"WARNING",z))
            else:
                results.append((value,"NORMAL",z))
        return results