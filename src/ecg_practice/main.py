from ecg_practice.ecg import interpret_ecg, Rhythm, STSegment
from ecg_practice.models.ecg_data import ECGData

if __name__ == '__main__':
    data = ECGData(
        heart_rate=175,
        rhythm=Rhythm.REGULAR,
        st_segment=STSegment.NORMAL,
        q_wave=False,
    )

    result = interpret_ecg(data)

    print(result)
