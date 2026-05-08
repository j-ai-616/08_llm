# OpenAI API 호출을 한 파일에 모아둔다.
# 화면(app.py)에서는 세부 API 문법을 몰라도 함수만 호출하도록 분리한다.

import json
import tempfile
from pathlib import Path
from typing import Dict, Generator

from openai import OpenAI

from config import DEFAULT_MODEL, STT_MODEL, TTS_MODEL, TTS_VOICE, MODERATION_MODEL, AUDIO_DIR

client = OpenAI()


# 브라우저에서 녹음된 음성을 STT 모델로 보내 텍스트로 변환한다.
def transcribe_audio(audio_file) -> str:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
        temp_audio.write(audio_file.getvalue())
        temp_audio_path = temp_audio.name

    try:
        # TODO: 여기에 코드 작성
        pass
    finally:
        Path(temp_audio_path).unlink(missing_ok=True)


# 사용자 입력이 안전한지 확인한다.
# 실제 서비스에서는 LLM 호출 전후에 안전 검사를 두는 것이 좋다.
def is_flagged(text: str) -> bool:
    if not text.strip():
        return False

    # TODO: 여기에 코드 작성
    pass


# Structured Outputs로 학습 노트를 JSON 구조로 생성한다.
# JSON으로 받으면 화면에서 제목, 요약, 핵심 개념 등을 항목별로 안정적으로 출력할 수 있다.
def generate_study_note(transcript: str) -> Dict:
    schema = {
        "type": "object",
        "additionalProperties": False,
        "properties": {
            "title": {"type": "string"},
            "summary": {"type": "string"},
            "key_points": {
                "type": "array",
                "items": {"type": "string"},
            },
            "confusing_points": {
                "type": "array",
                "items": {"type": "string"},
            },
            "review_questions": {
                "type": "array",
                "items": {"type": "string"},
            },
            "next_actions": {
                "type": "array",
                "items": {"type": "string"},
            },
        },
        "required": [
            "title",
            "summary",
            "key_points",
            "confusing_points",
            "review_questions",
            "next_actions",
        ],
    }

    # TODO: 여기에 코드 작성
    pass


# 생성된 노트를 바탕으로 짧은 복습 설명을 Streaming으로 만든다.
# Streaming은 긴 답변을 한 번에 기다리지 않고 화면에 점진적으로 보여줄 때 사용한다.
def stream_review_message(note: Dict) -> Generator[str, None, None]:
    # TODO: 여기에 코드 작성
    pass


# 복습 메시지를 TTS 모델로 변환해 음성 파일을 만든다.
def synthesize_speech(text: str) -> Path:
    output_path = AUDIO_DIR / "review_message.mp3"

    # TODO: 여기에 코드 작성
    pass

