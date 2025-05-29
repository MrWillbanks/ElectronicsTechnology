import random
import time

repeat = 'y'
ready = input("Are you ready??? (y/n)")
students = ["Matt", "Sam B.", "Ashlyn", "Maddy", "Nick", "Izzy", "Jason", "Anthony", "Jeremy", "Will", "Sam K.", "Karl", "Jacob", "Wyatt", "Jack", "Autumn"]
outcomes = ["finds a rock, and decides to skip it across water hitting a fish, the fish knocked unconscious falls onto a landmine under water causing a large rock to fly out of the water hitting a tree knocking it over on them.",
"gets warped out of space and time like the imposter in Among Us.",
"succumbs to stage 4 dysentery.",
"finds a tennis racket.",
"finds a native tribe.",
"gets decapitated by Notch.",
"broke their leg.",
"has died to a usb keyboard.",
"gets shanked by a plastic spork.",
"gets yeeted out of existence.",
"gets spaghettified.",
"dies first from something stupid.",
"attacks another player with an empty can of Monster.",
"attacks player two with a Goldfish.",
"finds a white can of Monster and gains super powers.",
"dies attempting to read Dr. Seuss.",
"gets too close to the lake and gets swallowed by a giant fish.",
"didn't lock out tag out and gets got by player two crushing them with a machine.",
"dies by a colored pen tip going into a sewer drain from drawing a technical drawing by hand, causing a pipe to explode, resulting in a flood on the third floor.",
"is under the popcorn ceiling when it crushes on itself.",
"goes to HVAC.",
"succumbs to a fidget spinner.",
"gets beaten by a Monster can.",
"tiktock dances to death.",
"believes they can fly.",
"eats the school lunch beans.",
"gets attacked with comically large wire strippers.",
"fails their OSHA training",
"flies a drone into Jacob's head",
"stands on a chair",
"fails their ladder safety training",
"flies a drone illegally",
"goes to the car show",
"does the pie eating contest on Field Day",
"runs a mile on Field Day",
"wears the wrong color to Field Day",
"wins Attendance Buddies",
"teams up with another player",
"develops scoliosis.",
" receives their Hogwarts letter.",
"is killed by Voldemort.",
"finds a lightsaber and kills Player 2.",
"discovers how to leave the matrix (automatic win)",
"is sucked into a blackhole.",
"dies during childbirth.",
"passes a kidney stone so forcefully that it becomes a projectile and kills Player 2.",
"hooks up with Fiona so Shrek, Lord Farquaad, and Prince Charming team up to brutally murder them.",
"is eaten by Jeffrey Dahmer after he spawns in.",
"and Player 2 team up.",
"develops scoliosis.",
"receives their Hogwarts letter.",
"is killed by Voldemort.",
"finds a lightsaber and kills Player 2.",
"discovers how to leave the matrix (automatic win).",
"is sucked into a blackhole.",
"dies during childbirth.",
"passes a kidney stone so forcefully that it becomes a projectile and kills Player 2.",
"hooks up with Fiona so Shrek, Lord Farquaad, and Prince Charming team up to brutally murder them.",
"Jeffery Dahmer spawns in and eats them.",
"finds the orb and is killed by Malgosha.",
"dies from 3rd degree internal burns after eating lava chicken.",
"looked the enderman in the eyes.",
"is slain by Steve after they killed Dennis.",
"tried to swim in lava.",
"accidentally summoned the wither.",
"commits homicide on Player 2.",
"commits a murder-suicide on Player 2.",
"puts an electrolytic capacitor in backwards and dies from the explosion.",
"didn't calculate the current and gets shocked, and dies from ventricular fibrillation.",
"gets killed by player2 by being bludgeoned to death with a Walkman.",
    "finds a cassette tape of 'Purple Rain' by Prince, CRT TV falls on their head.",
    "hears The Who and dies from shock, eats the Norwich Tech School lunch hamburger and dies.",
    "drinks out of 1978 McDonald's Garfield mug, dies of radiation sickness from cadmium in the paint.",
    "can't believe it's not butter! (dies immediately).",
    "forces player2 Imagine Dragons, player2 dies immediately.",
    "can hear the Green Goblin mask speaking to him.",
    "dies at the hands of the divine.",
    "is diagnosed with Fetal Alcohol Syndrome.",
    "finds a vaporizing gun at the cornucopia, kills player2 and player3.",
    "spontaneously combusts, but player2 inhales his ashes and also dies.",
    "gets hit by tar and feathers.",
    "gets diagnosed with Mono.",
    "dies of boredom after watching an end of cycle presentation.",
    "gets crushed by the Pixar lamp.",
    "smashes guitar on stage after hitting the solo, player2 gets hit by shrapnel from said guitar and dies.",
    "releases toxic gas from his digestive tract, 3 players in vicinity die (player2, player3, player4).",
    "chugs 6 litres of water, dies from water poisoning.",
    "attempts to invent a flying suit to fly like a bird and proceeds to fall to their death.",
    "slips on a banana peel thrown out of player2's Mario Kart.",
    "in an attempt to prove the windows were truly unbreakable, jumps against the glass; the window doesn't break but the frame does, plummets 24 stories to his death.",
    "attempts to throw player2 off a balcony, but player2 catches the power lines and swings onto a nearby balcony. Seeing this, jumps after them, misses the power lines, and plummets to their death."]
day = 1
suspense = 3

if(ready == "y"):
    print("Good luck...\n")
else:
    print("I don't care. Good luck...\n")
time.sleep(suspense)

while repeat == 'y':
    
    for i in students:
        assigned_outcome = random.choice(outcomes)
        print(f"Selected student: {i} {assigned_outcome}")
        
    eliminate = random.choice(students)
    if len(students) > 1:
        print(f"\n{eliminate} did not survive\n")
    elif len(students) == 1:
        print(f"\n{eliminate} IS THE WINNER\n")
    day += 1
    students.remove(eliminate)
    
    input(f"Type 'y' to see who survives Day {day}...")
    time.sleep(suspense)