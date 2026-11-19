# Способ 2: Python-скрипт
import asyncio
import json
import websockets
SESSION_ID = "20260421T165703Z"  # ваш session_id
async def chat():
    uri = f"ws://localhost:8000/ws/chat/{SESSION_ID}"
    async with websockets.connect(uri) as ws:
        print("Подключено! Введите сообщение (или 'выход' для завершения):\n")

        # Задача приёма ответов
        async def receive():
            async for msg in ws:
                data = json.loads(msg)
                if data["type"] == "assistant_token":
                    print(data["content"], end="", flush=True)
                elif data["type"] == "assistant_done":
                    print(f"\n{'─'*40}")
                elif data["type"] == "generation_cancelled":
                    print("\n[отменено]")
                elif data["type"] == "error":
                    print(f"\nОшибка: {data['message']}")
        recv_task = asyncio.create_task(receive())

        # Цикл ввода
        while True:
            text = await asyncio.to_thread(input, "Вы: ")
            if text.strip().lower() in ("выход", "quit", "exit"):
                break
            await ws.send(json.dumps({"type": "user_text", "content": text}))

        recv_task.cancel()
asyncio.run(chat())
# pip install websockets
# python chat.py