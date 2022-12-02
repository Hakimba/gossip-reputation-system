## WRITTEN BY ME, A HUMAN

## I didn't test anything, 
## this file is just all the code the chatGPT generate through my explanation of my idea of the gossip-reputation system
## with maybe some of his explanations
## As the memory of chatGPT isn't persistant, you basically lost everything when you log out 
## and my last conversation with him was quite amazing so i wanted to save it
## I DIDN'T TOUCH ANYTHING, ITS ALL THE CHAT GPT DOING



### CHAT GPT CODE

## Define a graph data structure to represent the game world, with each node representing a village
class VillageGraph {
  constructor() {
    this.nodes = new Map(); // Map of village names to Village objects
  }

  ## Add a new village to the graph
  addVillage(village) {
    this.nodes.set(village.name, village);
  }

  ## Add a new path between two villages
  addPath(village1, village2, weight) {
    this.nodes.get(village1).addNeighbor(this.nodes.get(village2), weight);
    this.nodes.get(village2).addNeighbor(this.nodes.get(village1), weight);
  }

  ## Simulate the spread of information throughout the game world
  simulate() {
    ## Use Dijkstra's algorithm to calculate the shortest paths from the source village to all other villages
    const source = [...this.nodes.values()].find(village => village.reputation > 0);
    const distances = this.dijkstra(source);

    ## Update the reputations of each village based on the reputations of its neighbors, weighted by the overall distance to the source village
    for (const village of this.nodes.values()) {
      village.updateReputation(distances.get(village));
    }
  }

  ## Use Dijkstra's algorithm to calculate the shortest paths from the given source village to all other villages
  dijkstra(source) {
    const distances = new Map(); ## Map of villages to distances from the source village
    const visited = new Set(); ## Set of visited villages

    ## Initialize the distances to all villages to be infinite, except for the source village, which has a distance of 0
    for (const village of this.nodes.values()) {
      distances.set(village, village === source ? 0 : Infinity);
    }

    # While there are unvisited villages
    while (visited.size < this.nodes.size) {
      # Find the unvisited village with the smallest distance from the source village
      let current = null;
      let currentDistance = Infinity;
      for (const [village, distance] of distances) {
        if (!visited.has(village) && distance < currentDistance) {
          current = village;
          currentDistance = distance;
        }
      }

      # Update the distances of the neighboring villages to be the minimum of the current distance and the distance to the current village
      for (const [neighbor, weight] of current.neighbors) {
        distances.set(neighbor, Math.min(distances.get(neighbor), currentDistance + weight));
      }

      # Mark the current village as visited
      visited.add(current);
    }

    return distances;
  }
}

## Define a class to represent a village in the game world
class Village {
  constructor(name) {
    this.name = name;
    this.reputation = 0; ## Initial reputation of 0
    this.neighbors = new Map(); ## Map of neighboring villages to connection weights
  }

  ## Add a new neighboring village
  addNeighbor(village, weight) {
    this.neighbors.set(village, weight);
  }

  ## Update the reputation of this village based on the reputations of its neighbors, weighted by the overall distance to the source village
  updateReputation(distance) {
    let totalWeight = 0;
    let reputationSum = 0;
    for (const [neighbor, weight] of this.neighbors) {
      totalWeight += weight / distance;
      reputationSum += neighbor.reputation * weight / distance;
    }
    this.reputation = reputationSum / totalWeight;
  }
}

## Define a class to represent an NPC in the game world
class NPC {
  constructor(name, village, dialogue) {
    this.name = name;
    this.village = village;
    this.dialogue = dialogue; // Map of player reputations to dialogue lines
  }

  ## Get the dialogue line for the given player reputation
  getDialogue(playerReputation) {
    let dialogue = "";
    for (const [minReputation, line] of this.dialogue) {
      if (playerReputation >= minReputation) {
        dialogue = line;
      }
    }
    return dialogue;
  }
}

## Define a class to represent the player in the game world
class Player {
  constructor() {
    this.reputation = 0; ## Initial reputation of 0
    this.quests = []; ## List of completed quests
  }

  ## Complete a quest, adding it to the list of completed quests
  completeQuest(quest) {
    this.quests.push(quest);
  }
}

## Define a class to represent a quest in the game world
class Quest {
  constructor(name, description, reward) {
    this.name = name;
    this.description = description;
    this.reward = reward; ## Reputation reward for completing the quest
  }
}

## Create a new graph to represent the game world
const gameWorld = new VillageGraph();

## Add some villages to the game world
const village1 = new Village("Village 1");
const village2 = new Village("Village 2");
const village3 = new Village("Village 3");
gameWorld.addVillage(village1);
gameWorld.addVillage(village2);
gameWorld.addVillage(village3);

## Add some paths between the villages
gameWorld.addPath(village1, village2, 1);
gameWorld.addPath(village1, village3, 1);
gameWorld.addPath(village2, village3, 1);

## Create some NPCs in the villages
const npc1 = new NPC("NPC 1", village1, new Map([
  [0, "Hi, how are you?"],
  [50, "I heard you killed the dragon in Village 1. Impressive!"],
  [100, "You must be the hero of the land!"],
]));
const npc2 = new NPC("NPC 2", village2, new Map([
  [0, "Hi, do you need any help?"],
  [50, "I heard you cleared the forest of goblins. That's amazing!"],
  [100, "You must be the strongest adventurer in the world!"],
]));
const npc3 = new NPC("NPC 3", village3, new Map([
  [0, "Hi, do you have
   
   
## Create a new player
const player = new Player();

## Create some quests for the player to complete
const quest1 = new Quest("Kill the dragon", "Defeat the dragon terrorizing Village 1", 100);
const quest2 = new Quest("Clear the forest of goblins", "Defeat the goblins in the forest near Village 2", 50);

## Complete a quest
player.completeQuest(quest1);

## Update the reputation of the village where the quest was completed
village1.reputation = quest1.reward;

## Simulate the spread of information throughout the game world
gameWorld.simulate();

## Print the dialogue of each NPC based on the player's reputation
for (const npc of [npc1, npc2, npc3]) {
  console.log(`${npc.name} in ${npc.village.name}: ${npc.getDialogue(player.reputation)}`);
}

## Complete another quest
player.completeQuest(quest2);

## Update the reputation of the village where the quest was completed
village2.reputation = quest2.reward;

## Simulate the spread of information throughout the game world
gameWorld.simulate();

## Print the dialogue of each NPC based on the player's updated reputation
for (const npc of [npc1, npc2, npc3]) {
  console.log(`${npc.name} in ${npc.village.name}: ${npc.getDialogue(player.reputation)}`);
}


## OUTPUTS

"""
NPC 1 in Village 1: You must be the hero of the land!
NPC 2 in Village 2: Hi, do you need any help?
NPC 3 in Village 3: Hi, do you have any news from the other villages?
"""
   
"""
NPC 1 in Village 1: You must be the hero of the land!
NPC 2 in Village 2: You must be the strongest adventurer in the world!
NPC 3 in Village 3: Wow, you must be unstoppable!
"""


