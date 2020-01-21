import random
from os import system, name


def clearScreen():
    if name == 'nt':
        _= system('cls')
    else:
        _= system('clear')

clearScreen()
# ---Entities---
class Creature:
    def __init__(self, id):
        self.id = id

    speed = 1
    size = 100
    maxSize = 200
    energy = 100
    safety = 100
    growthRate = 10
    hasMated = False
class Food:
    energyValueRange = [30, 50]

FOOD_ABUNDANCE = 33
ENERGY_CONSUMPTION = 40
DAYS_BETWEEN_SEASON = 1
GENERATIONS = 10
MUTATION_SEVERITY = .2
MUTATION_CHANCE = 20

# ---Fitness---
livingCreatures = []
identificationTag = 1
while len(livingCreatures) < 10:
    livingCreatures.append(Creature(identificationTag))
    identificationTag += 1

# ---Selection---
def searchForFood(hungryBoi):
    if random.randint(0,100) > FOOD_ABUNDANCE:
        if hungryBoi.energy < hungryBoi.size:
            hungryBoi.energy += random.randint(Food.energyValueRange[0], Food.energyValueRange[1])

def cycleDay(livingCreatures):
    survivingCreatures = []
    for c in livingCreatures:
        c.energy = c.energy - ENERGY_CONSUMPTION
        if c.energy > 0:
            searchForFood(c)
            survivingCreatures.append(c)
            print("Creature", c.id, "- Speed:", c.speed, "| Size:", c.size, "| Energy:", c.energy, "| Safety:", c.safety)
        else:
            print("Creature", c.id ,"has perished...")
        
    return survivingCreatures


for i in range(0, DAYS_BETWEEN_SEASON):
    if DAYS_BETWEEN_SEASON > 1:
        print("* DAY:", i + 1, "*")
    livingCreatures = cycleDay(livingCreatures)
    i += 1

    if len(livingCreatures) <= 0:
        print("☠ ALL CREATURES HAVE PERISHED ☠")
        break

# ---Crossover---
def mutate(trait):
        mutation = 0
        mutantLikelihood = random.randint(1,101)
        if mutantLikelihood <= MUTATION_CHANCE:
            mutation = float(trait) * MUTATION_SEVERITY

        return trait + mutation

def createOffspring(male):
    for female in livingCreatures:
        if male.id != female.id and female.energy >= female.safety and female.hasMated == False:
            offspring = Creature(livingCreatures[len(livingCreatures)-1].id + 1)

            # Speed
            luck = random.randint(0,3)
            if luck == 0:
                offspring.speed = (male.speed + female.speed) / 2
            elif luck == 1:
                offspring.speed = male.speed
            elif luck == 2:
                offspring.speed = female.speed
            offspring.speed = mutate(offspring.speed)

            # Size
            luck = random.randint(0,3)
            if luck == 0:
                offspring.size = (male.size + female.size) / 2
            elif luck == 1:
                offspring.size = male.size
            elif luck == 2:
                offspring.size = female.size
            offspring.size = mutate(offspring.size)

            # Max Size
            luck = random.randint(0,3)
            if luck == 0:
                offspring.maxSize = (male.maxSize + female.maxSize) / 2
            elif luck == 1:
                offspring.maxSize = male.maxSize
            elif luck == 2:
                offspring.maxSize = female.maxSize
            offspring.maxSize = mutate(offspring.maxSize)

            # Safety
            luck = random.randint(0,3)
            if luck == 0:
                offspring.safety = (male.safety + female.safety) / 2
            elif luck == 1:
                offspring.safety = male.safety
            elif luck == 2:
                offspring.safety = female.safety
            offspring.safety = mutate(offspring.safety)

            # Growth Rate
            luck = random.randint(0,3)
            if luck == 0:
                offspring.growthRate = (male.growthRate + female.growthRate) / 2
            elif luck == 1:
                offspring.growthRate = male.growthRate
            elif luck == 2:
                offspring.growthRate = female.growthRate
            offspring.growthRate = mutate(offspring.growthRate)

            
            female.hasMated = True
            male.hasMated = True
            offspring.hasMated = True
            return offspring
        
        

for i in range(0, GENERATIONS - 1):
    if GENERATIONS > 1:
        print("==== GENERATION ", i + 2, "====*")

    for c in livingCreatures:
        if c.energy >= c.safety and c.size < c.maxSize:
            c.size += c.growthRate

        if c.energy >= c.safety and c.hasMated == False:
            baby = createOffspring(c)
            if baby:
                livingCreatures.append(baby)

    for c in livingCreatures:
        c.hasMated = False

    if GENERATIONS > 1:
        livingCreatures = cycleDay(livingCreatures)

        if len(livingCreatures) <= 0:
            print("☠ ALL CREATURES HAVE PERISHED ☠")
            break
# ---Mutation---
