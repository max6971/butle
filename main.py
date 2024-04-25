import random


class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self, other):
        """ Наносит удар другому герою, уменьшая его здоровье """
        if random.random() > 0.2:  # 80% шанс попадания
            other.health -= self.attack_power
            print(f"{self.name} успешно атакует {other.name} и наносит {self.attack_power} урона.")
        else:
            print(f"{self.name} промахивается по {other.name}.")

    def is_alive(self):
        """ Проверяет, жив ли герой """
        return self.health > 0


class Game:
    def __init__(self, player_name):
        self.player = Hero(player_name)
        self.computer = Hero("Компьютер")

    def start(self):
        """ Запускает игру """
        turn = 0
        while self.player.is_alive() and self.computer.is_alive():
            print(f"\nРаунд {turn + 1}")
            if turn % 2 == 0:  # Ход игрока
                self.player.attack(self.computer)
            else:  # Ход компьютера
                self.computer.attack(self.player)

            print(f"Здоровье {self.player.name}: {self.player.health}")
            print(f"Здоровье {self.computer.name}: {self.computer.health}")
            turn += 1

        if self.player.is_alive():
            print(f"\nПобедил {self.player.name}!")
        else:
            print(f"\nПобедил {self.computer.name}!")


# Запуск игры
player_name = input("Введите имя игрока: ")
game = Game(player_name)
game.start()