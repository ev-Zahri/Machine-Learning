"""
API Service (FastAPI Router) untuk SkillAlign AI.

Router terpisah yang bisa di-include ke main FastAPI app.
Menyediakan endpoint /predict dan /predict/batch.
"""

import logging
from typing import List, Optional

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# Router instance
router = APIRouter(prefix="/api/v1", tags=["prediction"])


# ==========================================
# Request / Response Schemas
# ==========================================

class SinglePredictionRequest(BaseModel):
    """Request body untuk single prediction."""
    cv_text: str = Field(
        ...,
        min_length=50,
        max_length=10000,
        description="Teks CV pengguna (minimal 50 karakter)"
    )
    job_description: str = Field(
        ...,
        min_length=30,
        max_length=10000,
        description="Teks deskripsi lowongan kerja"
    )
    user_id: Optional[str] = Field(
        None,
        description="ID pengguna (opsional)"
    )

    model_config = {
        "json_schema_extra": {
            "examples": [{
                "cv_text": (
                    "Experienced Data Scientist with 3 years of experience "
                    "in Python, Machine Learning, TensorFlow, and data analysis."
                ),
                "job_description": (
                    "Looking for a Data Scientist with strong Python skills, "
                    "experience in ML frameworks and data visualization."
                ),
                "user_id": "user_123"
            }]
        }
    }


class BatchPredictionRequest(BaseModel):
    """Request body untuk batch prediction."""
    cv_text: str = Field(
        ...,
        min_length=50,
        max_length=10000,
        description="Teks CV pengguna"
    )
    job_descriptions: List[str] = Field(
        ...,
        min_length=1,
        max_length=50,
        description="List of job descriptions (max 50)"
    )
    user_id: Optional[str] = None


class PredictionResponse(BaseModel):
    """Response body untuk single prediction."""
    matching_score: float = Field(
        ...,
        ge=0.0,
        le=1.0,
        description="Skor matching 0-1"
    )
    confidence: str = Field(
        ...,
        description="Confidence level: High/Medium/Low"
    )
    recommendation: str = Field(
        ...,
        description="Recommendation text"
    )
    inference_time_ms: float = Field(
        ...,
        description="Waktu inferensi (ms)"
    )


class BatchPredictionItem(BaseModel):
    """Satu item hasil batch prediction, sudah diurutkan berdasarkan skor."""
    rank: int = Field(
        ...,
        description="Peringkat job (1 = paling cocok)"
    )
    job_index: int = Field(
        ...,
        description="Posisi job dalam array input (0-based), untuk tracing di Backend"
    )
    matching_score: float = Field(
        ...,
        ge=0.0,
        le=1.0,
        description="Skor kecocokan CV-Job (0.0-1.0)"
    )
    confidence: str = Field(
        ...,
        description="Confidence level: High / Medium / Low"
    )
    recommendation: str = Field(
        ...,
        description="Recommendation text"
    )
    inference_time_ms: float = Field(
        ...,
        description="Waktu inferensi (ms)"
    )


class BatchPredictionResponse(BaseModel):
    """Response body untuk batch prediction, diurutkan dari skor tertinggi."""
    results: List[BatchPredictionItem]
    total_items: int
    total_time_ms: float


# ==========================================
# Dependency: Predictor instance
# Akan di-set dari main.py saat startup
# ==========================================
_predictor = None


def set_predictor(predictor) -> None:
    """Set predictor instance (dipanggil dari main.py startup)."""
    global _predictor
    _predictor = predictor


def get_predictor():
    """Get predictor instance."""
    if _predictor is None:
        raise HTTPException(
            status_code=503,
            detail="Model belum loaded. Coba lagi nanti."
        )
    return _predictor


# ==========================================
# Endpoints
# ==========================================

@router.post(
    "/predict",
    response_model=PredictionResponse,
    summary="Predict CV-Job Matching Score",
    description="Prediksi skor kecocokan antara CV dan satu job description."
)
async def predict_single(request: SinglePredictionRequest):
    """
    Predict matching score antara CV dan Job Description.

    - **cv_text**: Teks CV pengguna (hasil ekstraksi PDF)
    - **job_description**: Deskripsi lowongan kerja
    - **user_id**: ID pengguna (opsional, untuk tracking)

    Returns matching score (0-1), confidence level, dan recommendation.
    """
    predictor = get_predictor()

    try:
        result = predictor.predict(
            cv_text=request.cv_text,
            job_description=request.job_description
        )

        return PredictionResponse(
            matching_score=result.matching_score,
            confidence=result.confidence,
            recommendation=result.recommendation,
            inference_time_ms=result.inference_time_ms
        )

    except Exception as e:
        logger.error(f"Prediction error: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed: {str(e)}"
        )


@router.post(
    "/predict/batch",
    response_model=BatchPredictionResponse,
    summary="Batch Predict CV-Job Matching",
    description="Prediksi skor kecocokan CV terhadap multiple job descriptions."
)
async def predict_batch(request: BatchPredictionRequest):
    """
    Batch prediction: satu CV terhadap multiple job descriptions.

    Berguna untuk ranking jobs yang paling cocok dengan CV pengguna.
    Maksimum 50 job descriptions per request.
    """
    predictor = get_predictor()

    try:
        cv_texts = [request.cv_text] * len(request.job_descriptions)
        raw_results = predictor.predict_batch(
            cv_texts=cv_texts,
            job_descriptions=request.job_descriptions
        )

        total_time = sum(r.inference_time_ms for r in raw_results)

        # Gabungkan hasil dengan job_index asli, lalu urutkan berdasarkan skor
        indexed = [
            {
                "job_index": i,
                "result": r
            }
            for i, r in enumerate(raw_results)
        ]
        indexed.sort(key=lambda x: x["result"].matching_score, reverse=True)

        # Buat response dengan rank yang jelas
        ranked_results = [
            BatchPredictionItem(
                rank=rank + 1,                          # 1-based rank
                job_index=item["job_index"],            # posisi di input array
                matching_score=item["result"].matching_score,
                confidence=item["result"].confidence,
                recommendation=item["result"].recommendation,
                inference_time_ms=item["result"].inference_time_ms
            )
            for rank, item in enumerate(indexed)
        ]

        return BatchPredictionResponse(
            results=ranked_results,
            total_items=len(ranked_results),
            total_time_ms=round(total_time, 2)
        )

    except Exception as e:
        logger.error(f"Batch prediction error: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Batch prediction failed: {str(e)}"
        )
