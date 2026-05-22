from os import getenv

import aiohttp
import requests
from fastapi import HTTPException

EXCHANGE_RATE_API_KEY = getenv('EXCHANGE_RATE_API_KEY')


def sync_converter(from_currency: str, to_currency: str, price: float):
    url = f'https://v6.exchangerate-api.com/v6/{EXCHANGE_RATE_API_KEY}/pair/{from_currency}/{to_currency}'

    try:
        response = requests.get(url=url)
    except Exception as error:
        raise HTTPException(status_code=400, detail=str(error))

    data = response.json()

    if "conversion_rate" not in data:
        raise HTTPException(
            status_code=400, detail=f'Erro na conversão: {data.get("result", "Desconhecido")}')

    exchange_rate = float(data["conversion_rate"])
    return price * exchange_rate


async def async_converter(from_currency: str, to_currency: str, price: float):
    url = f'https://v6.exchangerate-api.com/v6/{EXCHANGE_RATE_API_KEY}/pair/{from_currency}/{to_currency}'

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url) as response:
                data = await response.json()
    except Exception as error:
        raise HTTPException(status_code=400, detail=str(error))

    if "conversion_rate" not in data:
        raise HTTPException(
            status_code=400, detail=f'Erro na conversão: {data.get("result", "Desconhecido")}')

    exchange_rate = float(data["conversion_rate"])
    
    return {to_currency: price * exchange_rate}


