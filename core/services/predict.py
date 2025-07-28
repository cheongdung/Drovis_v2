# core/services/predict.py

import os
import numpy as np
from tensorflow.keras.models import load_model
from datetime import datetime
from core.services.save_analysis import save_analysis_result
from core.services.preprocess import process_pose

# config 상수 활용 (경로 하드코딩 대신)
from core.config import Config

LABELS = ["상", "중", "하"]
MODEL_PATH = os.path.join(Config.MODEL_FOLDER, "lstm_model.keras")
UPLOAD_FOLDER = Config.UPLOAD_FOLDER

# 앱 시작시 1회만 모델 로딩 (메모리 효율)
model = load_model(MODEL_PATH) if os.path.exists(MODEL_PATH) else None

def predict_from_video(video_path: str, user_id: str) -> dict:
    """
    영상 경로를 받아서 → pose npy 자동 추출 → LSTM 예측 → 결과 및 npy 경로 반환
    """
    if not os.path.isfile(video_path):
        return {"success": False, "message": f"영상 파일이 존재하지 않습니다: {video_path}"}

    # npy 경로 구성 (ex: v1.MOV → v1.pipe_norm_padd.npy)
    filename = os.path.basename(video_path)
    npy_name = os.path.splitext(filename)[0] + ".pipe_norm_padd.npy"
    npy_path = os.path.join(Config.UPLOAD_FOLDER, npy_name)

    try:
        sequence_array = process_pose(video_path)
        if sequence_array is None:
            return {"success": False, "message": "MediaPipe pose 변환 실패"}
        np.save(npy_path, sequence_array)
    except Exception as e:
        return {"success": False, "message": f"전처리 오류: {str(e)}"}

    # 예측
    if model is None:
        return {"success": False, "message": "AI 모델 파일이 없습니다."}
    try:
        sequence = np.load(npy_path)
        pred = model.predict(np.expand_dims(sequence, axis=0))
        result_index = np.argmax(pred)
        result_label = LABELS[result_index]
    except Exception as e:
        return {"success": False, "message": f"AI 예측 오류: {str(e)}"}

    # 결과 저장
    try:
        save_analysis_result(
            user_id=user_id,
            filename=filename,
            result=result_label
            # uploaded_at은 내부에서 자동으로 datetime.utcnow()로 기록
        )
    except Exception as e:
        return {"success": False, "message": f"DB 저장 오류: {str(e)}"}

    return {
        "success": True,
        "filename": filename,
        "result": result_label,
        "npy_path": npy_path
    }
