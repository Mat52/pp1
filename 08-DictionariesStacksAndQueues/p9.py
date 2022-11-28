mobilephone = {
    "marka": "Xiaomi",
    "model": "Redmi Note 9 Pro",
    "używany": True,
    "numery": ["654321234","534212345"],
    "rozmiar":"6 cali",
    "cena" : 999

}

mobile = mobilephone.items()

for i in mobile:
    print(f'{i[0]} - {i[1]}')