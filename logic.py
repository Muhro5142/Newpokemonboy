from random import randint
import datetime as dt
import requests

class Pokemon:
    pokemons = {}

    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   
        self.last_feed_time = dt.datetime.now()
        self.pokemon_number = randint(1,1000)
        
        self.img = self.get_img()
        self.name = self.get_name()
        self.abilities = self.get_power()
        self.power = randint(1,40)
        self.hp =  randint(25,100)
        
        Pokemon.pokemons[pokemon_trainer] = self

    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print(data['sprites']['other']['home']['front_default'])
            self.img =  data['sprites']['other']['home']['front_default']
        else:
            self.img = "no photo"
    

    def attack(self,enemy):
        if enemy.hp>self.power:
            enemy.hp -= self.power
            return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}"
        else:
            enemy.hp = 0
            return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}! "



    def feed(self, feed_interval = 20, hp_increase = 10 ):
        current_time = dt.datetime.now()  
        delta_time = dt.timedelta(seconds=feed_interval)  
        if (current_time - self.last_feed_time) > delta_time:
            self.hp += hp_increase
            self.last_feed_time = current_time
            return f"Здоровье покемона увеличено. Текущее здоровье: {self.hp}"
        else:
            return f"Следующее время кормления покемона: {current_time+delta_time}"  



    def get_power(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data['abilities']:  
                return data['abilities'][0]['ability']['name']  
            else:
                return "Не найдены умения в данном покемоне"
        else:
            return "- data"
        
    def get_height(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if 'height' in data:  
                return data['height']
            else:
                return "Не найдены умения в данном покемоне"
        else:
            return "- data"


    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"


    # Метод класса для получения информации
    def info(self):
        height = self.get_height()
        abilities = self.get_power()  # Call get_power to fetch the abilities
        return f"Имя: {self.name}\Умения: {abilities}\n Рост: {height} см \n Здоровье: {self.hp} единиц\n Сила:{self.power} единиц"


    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img
    

class Wizard(Pokemon):


    def feed(self, feed_interval=10, hp_increase=10):
        return super().feed(feed_interval, hp_increase)
    

    def attack(self, enemy):
        if randint(1,5) > 3:
            enemypower = enemy.power
            enemy.power = 0
            rez = super().attack(enemy)
            enemy.power = enemypower
        else:
            rez = super().attack(enemy)
        return rez


class Fighter(Pokemon):
    def attack(self, enemy):

        subPower = randint(1,40)
        if randint(1,10) > 7:
            self.power += subPower
        rez = super().attack(enemy)
        
        self.power -= subPower
        return rez
    


    def feed(self, feed_interval=20, hp_increase=20):
        return super().feed(feed_interval, hp_increase)
#Fighter can attack with more power - 1,80
#wizard can reflect attacks from his opponents
