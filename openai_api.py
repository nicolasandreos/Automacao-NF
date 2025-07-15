import requests

API_KEY = "<SUA CHAVE AQUI>"
URL = "https://openrouter.ai/api/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "HTTP-Referer": "https://meuprojeto.com",  # Pode ser fictício
    "X-Title": "Automação NF"
}

def gerar_resposta(prompt: str, modelo: str = "openai/gpt-4o") -> dict:
    data = {
        "model": modelo,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 1000  # <- adicionado para limitar o custo
    }

    try:
        response = requests.post(URL, headers=HEADERS, json=data)
        response.raise_for_status()
        resultado = response.json()
        return {"resposta": resultado["choices"][0]["message"]["content"]}
    except Exception as e:
        return {"resposta": str(e)}
    