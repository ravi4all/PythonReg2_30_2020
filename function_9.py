def playerHealth():
    health = 56
    life_remaining = 2
    return health, life_remaining

def enemyHealth():
    health = 80
    life_remaining = 1
    return health, life_remaining

def game():
    p_health = playerHealth()
    e_health = enemyHealth()
    if p_health < e_health:
        print("Your health is low")
    else:
        print("You can win...")



game()