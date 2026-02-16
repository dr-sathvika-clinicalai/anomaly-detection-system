from src.patient_data import PatientData
from src.statistics_calculator import StatisticsCalculator
from src.anomaly_detector import AnomalyDetector

if __name__== "__main__":

    PATIENT_VALUES = [70,72,75,71,69,120]

    data = PatientData(values)
    stats = StatisticsCalculator(data.values)
    detector = AnomalyDetector(data.values,stats)

    print("Mean:",stats.mean())
    print("Standard Deviation",stats.standard_deviation())

results = detector.detect_anomalies()

print("\nDetection Result:")
for value,status,z in results:
    print(f"value: {value},Status: {status}, Z-score:{round(z,2)}")
