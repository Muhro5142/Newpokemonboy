from random import randint
import requests

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
        
        self.img = self.get_img()
        self.name = self.get_name()
        self.power = self.get_power()

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
        abilities = self.get_power()  # Call get_power to fetch the abilities
        return f"Имя: {self.name}\Умения: {abilities}\n"


    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img
    

