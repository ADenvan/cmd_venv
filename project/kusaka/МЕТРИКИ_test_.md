# Какие языковые наборы тесто
нужны помимо английского / русский

# Допустимые пороговые значения метрик в тестах голосовых систем

На основе индустриальных стандартов и рекомендаций ведущих платформ для тестирования голосовых ИИ-агентов, вот рекомендуемые целевые значения по каждому параметру:

---

## 🕐 LATENCY (Задержка)

| Метрика | Отлично | Приемлемо | Критично |
|---------|---------|-----------|----------|
| **Time to First Audio (TTFA), P50** | <1.3 с | 1.3–1.7 с | >1.7 с |
| **TTFA, P95** | <3.5 с | 3.5–5.0 с | >6.0 с |
| **End-to-end (стриминг)** | 500–800 мс | 800–1500 мс | >1500 мс |
| **Компонент: STT** | <200 мс | 200–500 мс | >500 мс |
| **Компонент: LLM (TTFT)** | <300 мс | 300–800 мс | >1 с |
| **Компонент: TTS (TTFB)** | <150 мс | 150–400 мс | >400 мс |


## 📊 WER / CER (Точность распознавания)

| Метрика | Отлично | Приемлемо | Критично | Примечание |
|---------|---------|-----------|----------|------------|
| **WER (английский, чистый аудио)** | <5% | 5–10% | >15% | Базовый бенчмарк |
| **WER (с шумом/акцентами)** | <8% | 8–12% | >20% | Реальные условия |
| **WER (медицина/финансы)** | <3% | 3–7% | >10% | Критичные домены |
| **CER (имена, номера)** | <2% | 2–5% | >8% | Для entity extraction |
| **WER по языкам** | Зависит от языка | См. таблицу ниже | — | [[20]] |

### WER-бенчмарки по языкам (приёмлемые значения):
| Язык | Отлично | Приемлемо |
|------|---------|-----------|
| Английский (US) | <5% | <10% |
| Английский (индийский) | <8% | <15% |
| Испанский | <7% | <14% |
| Немецкий | <7% | <12% |
| Хинди | <12% | <18% |
| Мандарин | <10% | <18% |


---

## 🔊 MOS (Mean Opinion Score — качество синтеза речи)

| Оценка | Качество | Описание | Применение |
|--------|----------|----------|------------|
| **4.3–5.0** | Отличное | Практически неотличимо от человека | Premium-продукты |
| **3.8–4.2** | Хорошее | Естественное, допустимые артефакты | Большинство production-кейсов |
| **3.0–3.7** | Удовлетворительное | Заметно искусственное, но понятное | Внутренние инструменты |
| **<3.0** | Плохое | Роботизированное, раздражающее | Не рекомендуется к выпуску |

📌 **Методология:** Оценка проводится по стандарту ITU-T P.800 с участием человеческих респондентов. Для автоматизации используются метрики типа MOSNet или VQM, но они не заменяют субъективную оценку полностью.

---

## 🗣️ Barge-in (Обработка прерываний)

| Метрика | Целевое значение | Критичный порог | Описание |
|---------|------------------|-----------------|----------|
| **Detection Rate** | >95% | <85% | Точность обнаружения прерывания |
| **Recovery Rate** | >90% | <75% | Успешное восстановление контекста после прерывания |
| **False Positive Rate** | <5% | >15% | Ложные срабатывания на шум/паузы |
| **Turn-taking latency** | 200–500 мс | >1 с | Время реакции на прерывание |

📌 **Тестирование barge-in должно включать:**
- Прерывания в середине предложения
- Наложение речи (overlapping speech)
- Шумовые условия (10–20 дБ SNR)
- Разные акценты и темп речи.

---

## 🔧 Практические рекомендации для тестов

1. **Измеряйте end-to-end**, а не только инференс модели — пользователь ощущает полную задержку от конца речи до начала ответа.
2. **Тестируйте на реальных данных**: акценты, фоновый шум, плохое качество связи, телефонное аудио (8 кГц).
3. **Используйте перцентили (P50/P95/P99)**, а не только средние значения — пользователи запоминают худшие случаи.
4. **Сочетайте метрики**: низкий WER + высокая задержка = плохой UX; высокая точность + плохой barge-in = раздражение.
5. **Регрессионное тестирование**: автоматизируйте прогон тестов при каждом изменении промптов или моделей.

---

# Есть ли готовые тестовые наборы.
Ответ нет нужно использовать открытые датасеты (LibriSpeech и т. п.)

# Сколько одновременных сессий
Две сессий планирую поддерживать в нагрузочках (пороги concurrency)

# между LangGraph и Edge-TTS/ASR и какие форматы сообщений критичны
Да, при интеграции **LangGraph** с **Edge-TTS** (или Azure Neural TTS) и **ASR** (Azure Speech/Whisper и т.п.) вам потребуется спроектировать явные контракты-адаптеры. LangGraph сам по себе не навязывает форматы общения с внешними сервисами, но для стабильной работы голосового пайплайна необходимы чёткие интерфейсы на уровне: схемы состояния, протоколов обмена, стриминга и обработки ошибок.

Ниже разбор по слоям.

---

## 🔌 1. Какие контракты необходимы?

| Уровень контракта | Зачем нужен | Что покрывает |
|-------------------|-------------|---------------|
| **State Schema Contract** | LangGraph работает с TypedDict/Pydantic. Без явной схемы состояние быстро деградирует. | Поля для аудио-чанков, текста, метаданных, флагов endpointing, latency-метрик, истории |
| **Adapter Node Contract** | Узлы LangGraph должны быть идемпотентными, async-ready и детерминированными. | Вход/выход узла, таймауты, retry-политика, fallback-логика |
| **Streaming Contract** | Голосовой UX требует chunk-by-chunk передачи без блокировок. | Sequence ID, chunk boundaries, `is_final`, backpressure, interrupt signal |
| **Error & Fallback Contract** | Сетевые сбои, лимиты API, невалидный аудио | Коды ошибок, circuit breaker, деградация к оффлайн-TTS/ASR, логирование |
| **Barge-in / Interrupt Contract** | Пользователь может перебить систему в любой момент | Signal `INTERRUPT`, audio drain, state rollback, context preservation |

---

## 📦 2. Критичные форматы сообщений

### 🔹 Аудио (ASR вход / TTS выход)
| Параметр | Критичное значение | Почему |
|----------|-------------------|--------|
| **Формат** | `audio/x-wav` или `audio/pcm` | Без заголовков, raw PCM проще стримить |
| **Sample Rate** | `16000 Hz` | Стандарт для большинства ASR/TTS моделей |
| **Bit Depth** | `16-bit` (signed integer) | Минимальный порог качества |
| **Каналы** | `Mono (1)` | Стерео не поддерживается большинством voice API |
| **Endianness** | `Little-endian` | Требование Azure/Whisper/edge-tts |

> ⚠️ Не храните полные аудио-файлы в `state`. Используйте `bytes`-чанки или внешние ссылки (S3/Redis), иначе память узла взорвётся после 3-5 реплик.

---

### 🔹 JSON / State Schema (LangGraph ↔ Узлы TTS/ASR)
Пример критичной схемы состояния (Pydantic):

```python
from pydantic import BaseModel, Field
from typing import List, Optional, Literal

class AudioChunk(BaseModel):
    sequence_id: int
    data: bytes  # или base64-строка, если сериализация в JSON
    sample_rate: int = 16000
    is_final: bool = False
    language: str = "ru-RU"

class ASRResult(BaseModel):
    text: str
    confidence: float
    word_timestamps: Optional[List[dict]] = None
    is_interim: bool = True  # False = final endpoint
    latency_ms: int

class TTSRequest(BaseModel):
    text: str
    voice_id: str
    ssml: Optional[str] = None
    streaming: bool = True
    interrupt_signal: bool = False

class TTSResponse(BaseModel):
    chunks: List[AudioChunk]
    total_duration_ms: int
    latency_ttfa_ms: int
    error: Optional[str] = None

class VoiceAgentState(BaseModel):
    user_audio_stream: List[AudioChunk] = Field(default_factory=list)
    asr_result: Optional[ASRResult] = None
    llm_response: str = ""
    tts_chunks: List[AudioChunk] = Field(default_factory=list)
    conversation_history: List[dict] = Field(default_factory=list)
    barge_in_active: bool = False
    metrics: dict = Field(default_factory=dict)
```

> 🔑 **Критичные поля**: `is_final`, `sequence_id`, `interrupt_signal`, `latency_ms`, `confidence`. Без них невозможны корректный endpointing, barge-in и мониторинг SLA.

---

### 🔹 Протоколы обмена (Streaming & Sync)
| Сценарий | Рекомендуемый формат | Примечание |
|----------|---------------------|------------|
| **ASR стриминг** | AsyncGenerator → `ASRResult(is_interim=True/False)` | Используйте Azure Speech SDK WebSocket или `vosk`/`whisper.cpp` streaming |
| **TTS стриминг** | AsyncGenerator → `AudioChunk` | `edge-tts` поддерживает `streaming=True`, но требует парсинга chunk-by-chunk |
| **Barge-in interrupt** | Signal: `{"type": "INTERRUPT", "seq_id": N}` | Должен прерывать TTS генератор и сбрасывать буфер воспроизведения |
| **Fallback** | JSON `{"status": "fallback", "source": "local_tts", "error": "..."}` | Критично для production |

---

## 🛠 3. Практические рекомендации для LangGraph

1. **Разделяйте state и media**
   Храните в `state` только метаданные и ссылки на аудио. Сами чанки передавайте через async queues или external storage.

2. **Используйте `interrupt_before` / `interrupt_after`**
   LangGraph поддерживает прерывания на уровне графа. Привяжите сигнал barge-in к `interrupt_before="tts_node"`.

3. **Явно объявляйте контракты узлов**
   ```python
   @node
   async def asr_node(state: VoiceAgentState) -> dict:
       # Валидация входных данных
       if not state.user_audio_stream:
           return {"asr_result": None, "error": "empty_audio"}
       # Вызов ASR adapter
       result = await asr_adapter.transcribe(state.user_audio_stream)
       return {"asr_result": result}
   ```

4. **Стриминг в LangGraph**
   LangGraph пока не имеет встроенного `yield` в узлах. Для стриминга используйте:
   - `langgraph.checkpoint` + внешний WebSocket
   - `langgraph.func` с async generators (экспериментально)
   - Отдельный `StreamingGateway`-узел, который читает queue и пушит клиенту

5. **Контроль latency**
   Замеряйте `TTFA` на границе `llm_node → tts_node`. Если `>1.5s`, активируйте `fallback_tts` или сокращайте `max_tokens`.

---

## 📌 Итог: что обязательно реализовать

| Контракт | Формат | Критичность |
|----------|--------|-------------|
| State Schema | Pydantic/TypedDict с `sequence_id`, `is_final`, `interrupt_signal` | 🔴 Высокая |
| Audio I/O | PCM 16kHz/16bit/mono, chunked | 🔴 Высокая |
| ASR Output | JSON с `confidence`, `word_timestamps`, `is_interim` | 🟠 Средняя |
| TTS Input | Текст/SSML + `streaming=True` | 🔴 Высокая |
| Interrupt Signal | JSON `{"type":"INTERRUPT","seq_id":N}` | 🔴 Высокая |
| Error/Fallback | Стандартизированные коды + circuit breaker | 🟠 Средняя |


# Какие инструменты наблюдения
Для production-системы голосового ИИ на базе LangGraph + ASR/TTS рекомендуется единый OpenTelemetry-стек с экспортом в специализированные бэкенды. LangGraph и LangChain официально поддерживают OTel, что делает его обязательным фундаментом.
Ниже архитектурная карта: что, зачем и как инструментировать в вашем контексте.

Для production-системы голосового ИИ на базе **LangGraph + ASR/TTS** рекомендуется **единый OpenTelemetry-стек** с экспортом в специализированные бэкенды. LangGraph и LangChain официально поддерживают OTel, что делает его обязательным фундаментом.

Ниже архитектурная карта: что, зачем и как инструментировать в вашем контексте.

---

## 🧩 Рекомендуемый стек наблюдения

| Инструмент | Роль в пайплайне | Что собирает | Рекомендация |
|------------|------------------|--------------|--------------|
| **OpenTelemetry (Python SDK)** | Единый слой инструментации | Метрики, трассы, логи | 🔴 Обязательно. Стандарт де-факто, нативная поддержка LangGraph |
| **Prometheus** | Хранение метрик + алертинг | Latency-перцентили, WER/CER, ошибки, barge-in-счётчики | 🔴 Обязательно. Идеален для SLO/SLA мониторинга |
| **Jaeger / Tempo** | Распределённая трассировка | End-to-end задержки по узлам, блокировки в стриминге, rollback barge-in | 🟠 Jaeger (классика) или **Tempo** (дешевле, Grafana-native) |
| **ELK (Elastic) или Loki** | Логи и события | Транскрипты, fallback-события, MOS-фидбэк, ошибки адаптеров | 🟠 **Loki** предпочтительнее для cloud-native. ELK если уже есть в инфраструктуре |

> 💡 **Почему не выбирать один?** Голосовой пайплайн генерирует разнородные данные: метрики (для SLO), трассы (для отладки задержек), логи/события (для аудита транскриптов и barge-in). OTel Collector агрегирует всё в едином формате и маршрутизирует.

---

## 📊 Что именно мониторить (привязка к вашим параметрам)

### 1. `LATENCY`
| Тип | OTel-инструмент | Атрибуты / Метрики |
|-----|----------------|-------------------|
| **Time to First Audio (TTFA)** | Histogram `voice.ttfa.duration` | `p50, p95, p99`, `voice`, `lang`, `model` |
| **Компонентные задержки** | Spans: `asr.transcribe`, `llm.generate`, `tts.synthesize` | `duration`, `chunk_count`, `is_streaming` |
| **Turn-taking / Barge-in recovery** | Histogram `voice.bargein.recovery_latency` | `interrupt_at_sec`, `context_restored`, `false_positive` |

### 2. `WER / CER`
| Тип | OTel-инструмент | Атрибуты / Метрики |
|-----|----------------|-------------------|
| **WER по сессии** | Gauge `voice.asr.wer` | `lang`, `noise_db`, `domain`, `model_version` |
| **Entity-specific CER** | Histogram `voice.asr.cer_entity` | `entity_type` (phone, name, amount), `confidence` |
| **Семантическая точность** | Counter `voice.asr.semantic_error` | `critical_keyword_missed: true/false` |

> ⚠️ WER/CER не считаются в реальном времени. Агрегируйте постфактум (batch-валидация) или используйте эталонные тестовые наборы. В production пушьте метрику раз в N сессий или при смене модели.

### 3. `MOS`
| Тип | OTel-инstrument | Атрибуты / Метрики |
|-----|----------------|-------------------|
| **Субъективный MOS** | Histogram `voice.tts.mos_user` | `voice_id`, `prompt_length`, `session_id` |
| **Автоматический MOSNet/VQM** | Gauge `voice.tts.mos_predicted` | `artifact_score`, `prosody_score` |
| **Feedback loop** | Event Log `voice.feedback.mos` | `rating: 1-5`, `comment`, `trace_id` |

### 4. `Barge-in`
| Тип | OTel-инструмент | Атрибуты / Метрики |
|-----|----------------|-------------------|
| **Detection rate** | Counter `voice.bargein.detected` / `missed` | `overlapping: true/false`, `snr_db` |
| **False positives** | Counter `voice.bargein.false_positive` | `triggered_on: silence/noise/music` |
| **State recovery** | Span `voice.bargein.recovery` | `context_rolled_back: bool`, `llm_reprompted: bool` |

---

## 🔌 Интеграция с LangGraph

LangGraph поддерживает OTel через `langchain_core.tracers` и `opentelemetry-instrumentation-langgraph`.

```python
from opentelemetry import trace, metrics
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.metrics import MeterProvider
from langgraph.graph import StateGraph

# Инициализация
trace.set_tracer_provider(TracerProvider())
meter = metrics.get_meter_provider().get_meter("voice_agent")

# Кастомные метрики
ttfa_hist = meter.create_histogram("voice.ttfa.duration")
wer_gauge = meter.create_gauge("voice.asr.wer")
bargein_counter = meter.create_counter("voice.bargein.detected")

# Пример узла с инструментацией
@node
async def tts_node(state: VoiceAgentState):
    span = trace.get_tracer(__name__).start_span("tts.synthesize")
    span.set_attribute("text_length", len(state.llm_response))
    span.set_attribute("streaming", True)

    try:
        async for chunk in tts_adapter.stream(state.llm_response):
            ttfa_hist.record(chunk.latency_ms, attributes={"voice": state.voice_id})
            yield chunk
        span.set_status(trace.StatusCode.OK)
    except Exception as e:
        span.record_exception(e)
        span.set_status(trace.StatusCode.ERROR, str(e))
        raise
    finally:
        span.end()
```

> 🔑 **Важно**: LangGraph автоматически прокидывает `trace_id` и `span_id` в контекст. Используйте их в логах адаптеров ASR/TTS, чтобы связывать аудио-события с трассами.

---

## 🗃️ Архитектура сбора данных

```
[LangGraph Nodes] → OTel Python SDK (metrics/traces/logs)
        ↓
[OTel Collector] (docker/k8s)
   ├─ exporters/prometheus → Prometheus → Grafana (SLO-дашборды)
   ├─ exporters/otlp/jaeger → Jaeger/Tempo (анализ задержек, barge-in)
   └─ exporters/otlp/logs → Loki или ELK (транскрипты, fallback, MOS)
```

### 📉 Сэмплирование и стоимость
- **Трассы**: 10–20% для стриминговых сессий (иначе >10k spans/min на 100 RPS)
- **Логи**: Включайте `trace_id`, отключайте сырые аудио-чанки. Храните 7–14 дней.
- **Метрики**: Агрегируйте по 15s/1m окнам. WER/CER обновляйте пакетно, не в real-time.

---

## ✅ Что выбрать на старте?

| Этап | Минимальный стек | Расширенный |
|------|------------------|-------------|
| **MVP / 1-2 инженера** | OTel → Prometheus + Grafana + JSON-логи в файл/CloudWatch | — |
| **Production / SLO** | OTel → Prometheus + Loki + Tempo (все в Grafana) | ELK вместо Loki если нужен полнотекстовый поиск по транскриптам |
| **Enterprise / Compliance** | + Jaeger (W3C Trace Context), + AlertManager, + MOS-фидбэк pipeline | |

---