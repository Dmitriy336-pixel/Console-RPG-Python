import questionary
answer = questionary.select("Тест", choices=["Первый", "Второй"]).ask()
print("Выбрано:", answer)