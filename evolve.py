import random

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
class Food:
    energyValue = 50

FOOD_ABUNDANCE = 50
ENERGY_CONSUMPTION = 50
DAYS_BETWEEN_SEASON = 1
GENERATIONS = 10
MUTATION_SEVERITY = .1
MUTATION_CHANCE = 10

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
            hungryBoi.energy += Food.energyValue

def cycleDay(livingCreatures):
    survivingCreatures = []
    for c in livingCreatures:
        c.energy = c.energy - ENERGY_CONSUMPTION
        if c.energy > 0:
            searchForFood(c)
            survivingCreatures.append(c)
            print(c.id, c.speed, c.size, c.energy)
        else:
            print("A creature has perished...")
        
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
            mutation = trait
            mutation = mutation * MUTATION_SEVERITY

        return trait + mutation

def findMate(male):
    for female in livingCreatures:
        if male.id != female.id and female.energy >= female.safety:
            offspring = Creature(livingCreatures[len(livingCreatures)-1].id + 1)

            # Speed
            luck = random.randint(0,3)
            if luck == 0:
                offspring.speed = (male.speed * female.speed) / 2
            elif luck == 1:
                offspring.speed = male.speed
            elif luck == 2:
                offspring.speed = female.speed
            offspring.speed = mutate(offspring.speed)

            # Size
            luck = random.randint(0,3)
            if luck == 0:
                offspring.size = (male.size * female.size) / 2
            elif luck == 1:
                offspring.size = male.size
            elif luck == 2:
                offspring.size = female.size
            offspring.size = mutate(offspring.size)

            # Max Size
            luck = random.randint(1,101)
            if luck == 0:
                offspring.maxSize = (male.maxSize * female.maxSize) / 2
            elif luck == 1:
                offspring.maxSize = male.maxSize
            elif luck == 2:
                offspring.maxSize = female.maxSize
            offspring.maxSize = mutate(offspring.maxSize)

            # Safety
            luck = random.randint(0,3)
            if luck == 0:
                offspring.safety = (male.safety * female.safety) / 2
            elif luck == 1:
                offspring.safety = male.safety
            elif luck == 2:
                offspring.safety = female.safety
            offspring.safety = mutate(offspring.safety)

            # Growth Rate
            luck = random.randint(0,3)
            if luck == 0:
                offspring.growthRate = (male.growthRate * female.growthRate) / 2
            elif luck == 1:
                offspring.growthRate = male.growthRate
            elif luck == 2:
                offspring.growthRate = female.growthRate
            offspring.growthRate = mutate(offspring.growthRate)

            livingCreatures.append(offspring)

for c in livingCreatures:
    if c.energy >= c.safety and c.size < c.maxSize:
        c.size += c.growthRate

    if c.energy >= c.safety:
        findMate(c)

for c in livingCreatures:
    print(c.id, c.speed, c.size, c.energy)

# ---Mutation---
