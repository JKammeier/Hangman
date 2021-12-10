import pygame
#from pygame.locals import
import random

pygame.init()
pygame.font.init()
clock = pygame.time.Clock()

# window
windowW = 800
windowH = 500

# colors
colorBackground = (50, 50, 50)

words = ["Actor", "Gold", "Painting", "Advertisement", "Grass", "Parrot", "Afternoon", "Greece", "Pencil", "Airport", "Guitar", "Piano", "Ambulance", "Hair", "Pillow", "Animal", "Hamburger", "Pizza", "Answer", "Helicopter", "Planet", "Apple", "Helmet", "Plastic", "Army", "Holiday", "Portugal", "Australia", "Honey", "Potato", "Balloon", "Horse", "Queen", "Banana", "Hospital", "Quill", "Battery", "House", "Rain", "Beach", "Hydrogen", "Rainbow", "Beard", "Ice", "Raincoat", "Bed", "Insect", "Refrigerator", "Belgium", "Insurance", "Restaurant", "Boy", "Iron", "River", "Branch", "Island", "Rocket", "Breakfast", "Jackal", "Room", "Brother", "Jelly", "Rose", "Camera", "Jewellery", "Russia", "Candle", "Jordan", "Sandwich", "Car", "Juice", "School", "Caravan", "Kangaroo", "Scooter", "Carpet", "King", "Shampoo", "Cartoon", "Kitchen", "Shoe", "China", "Kite", "Soccer", "Church", "Knife", "Spoon", "Crayon", "Lamp", "Stone", "Crowd", "Lawyer", "Sugar", "Daughter", "Leather", "Sweden", "Death", "Library", "Teacher", "Denmark", "Lighter", "Telephone", "Diamond", "Lion", "Television", "Dinner", "Lizard", "Tent", "Disease", "Lock", "Thailand", "Doctor", "London", "Tomato", "Dog", "Lunch", "Toothbrush", "Dream", "Machine", "Traffic", "Dress", "Magazine", "Train", "Easter", "Magician", "Truck", "Egg", "Manchester", "Uganda", "Eggplant", "Market", "Umbrella", "Egypt", "Match", "Van", "Microphone", "Vase", "Energy", "Monkey", "Vegetable", "Engine", "Morning", "Vulture", "England", "Motorcycle", "Wall", "Evening", "Nail", "Whale", "Eye", "Napkin", "Window", "Family", "Needle", "Wire", "Finland", "Nest", "Xylophone", "Fish", "Nigeria", "Yacht", "Flag", "Night", "Yak", "Flower", "Notebook", "Zebra", "Football", "Ocean", "Zoo", "Forest", "Oil", "Garden", "Fountain", "Orange", "Gas", "France", "Oxygen", "Girl", "Furniture", "Oyster", "Glass", "Garage", "Ghost"]

mainFont = pygame.font.SysFont('sans-serif', 18)

window = pygame.display.set_mode((windowW, windowH))
pygame.display.set_caption("Hangman")

running = True

while running:
    window.fill(colorBackground)
    for event in pygame.event.get():
        if event == pygame.QUIT:
            pygame.font.quit()
            pygame.quit()
            quit()

    pygame.display.update()
    clock.tick(60)


def getRandomWord():
    return words[round(random.random() * len(words))]


def getCharSpot(char, word):
    if char in word:
        res = []
        for i in range(len(word)):
            if char == word[i]:
                res.append(i)
        return res
    else:
        return -1

