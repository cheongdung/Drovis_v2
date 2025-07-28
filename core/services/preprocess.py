# core/services/preprocess.py
import cv2
import numpy as np
import mediapipe as mp

def process_pose(video_path, seq_len=90, detected_points=33):
    """
    입력 받은 영상 파일에서 Pose 정보 추출하여
    (seq_len, detected_points*4) 크기의 numpy 배열로 리턴
    - 영상 열기 실패 등 예외 발생시 None 반환
    """
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5)
    cap = cv2.VideoCapture(video_path)
    frames = []

    if not cap.isOpened():
        print(f"[ERROR] 영상 파일을 열 수 없습니다: {video_path}")
        return None

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        # 영상 프레임을 RGB로 변환
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(frame_rgb)
        if results.pose_landmarks:
            landmarks = results.pose_landmarks.landmark
            coords = []
            for lm in landmarks:
                coords.extend([lm.x, lm.y, lm.z, lm.visibility])
            frames.append(coords)
        else:
            frames.append([0] * detected_points * 4)
    cap.release()
    pose.close()

    frames = np.array(frames)
    # 프레임 개수 부족 시 패딩 / 많으면 자르기
    if len(frames) < seq_len:
        pad = np.zeros((seq_len - len(frames), detected_points * 4))
        frames = np.vstack([frames, pad])
    else:
        frames = frames[:seq_len]

    return frames

# 사용 예: (PyQt5에서 영상 경로를 받아 넘겼을 때)
# arr = process_pose("/path/to/user_uploaded.mov")
# if arr is not None:
#     np.save("output.pipe_norm_padd.npy", arr)
#     # 이후 LSTM 모델 inference에 활용
