# All evolution leads to scraping the ground

![asd](https://user-images.githubusercontent.com/67875325/225191557-c014bd6d-df3e-4bfa-af37-2f404947a561.gif)

If you want to make cool looking moving robots, you've come to the slightly right place. I got the moving robots, but cool is subjective. Here, in this README, I'll walk you through the steps to create some robots like the ones above. 

First, all information for setting up the bots was found in the reddit ludobots instructions starting here:

https://www.reddit.com/r/ludobots/wiki/installation/

and Neural Network for robots gotten from pyrosim:
https://github.com/jbongard/pyrosim

Going through the steps above will get you to a good starting point of how to create a ludobot (blue and green blocks connected by joints) as well as using the neural network provided. 

Now, the first thing to do is figure out how you want to generate your robot. How many links do you want to make? How do you want to connect the joints together? What orientations do you need? 
For me, I decided to do a random amount of links, with a 50 percent chance of each link becoming a sensor value. Each link will create a joint connected to the previous link, and sensor links will cause the joint to move in a different direction when the link is touching the ground. Whenever a link is about to be created, I first create an imaginary link at a random face from all of my links. If the imaginary link is overlapping with an existing link, then I choose another face. When the imaginary link doesn't overlap, I create that link and report it to my brain if my new link is a sensor. The brain will keep track of the sensor links when they touch the ground, and change the joint's direction. Lastly, I also change the width, height, and length of the links to bring more variety to my robots. Here is a more visualized diagram of my body and brain generation:
![Generation](https://user-images.githubusercontent.com/67875325/225188446-026ad2f0-0445-4bb5-a8eb-dd5837be0d7c.jpg)

Now, how do we figure out if the robot is moving? We need to use a fitness function, which is covered in ludobots, but it is some numerical value that can be compared to figure out which is better. For me, I have it as the distance between the root link and the position (0,0,0). 
To make the robot evolve, we need to mutate the robot and use the fitness function on it. For my mutation, I have two options. One, add a new link to the robot. Two, change an existing non-sensor link to a sensor. This allows variety that can impact the fitness function. Here is a visualized diagram of the mutation:
![Mutation](https://user-images.githubusercontent.com/67875325/225189030-d7454f8c-6dd8-4c3c-9f23-f7820bbe5b4f.jpg)

After mutating, we need to now see if it's actually better. We compare the mutated fitness function and the initial fitness function, and then whichever one has the better fitness function will be used as the base for the mutation next time. Now, this will be very slow if we want to run it many times. To combat this, we will use parallel hill climbing, also mentioned in ludobots. For this, we run multiple instances of our program, each with an initial robot. The comparisons, mutations, and continuations will happen on each of them, and at the very end, we will take the highest fitness from the different robots as our best version. Here is a visualized diagram: 
![phc](https://user-images.githubusercontent.com/67875325/225189846-3dd6803f-9c1f-497c-b635-ff5a670ae40e.jpg)

With this, I was able to run multiple simulations and run 10 populations for 500 generations 10 times, making it a total of 50,000 simulations. Plotting the best fitness for each simulation resulted in this graph:
![Figure_1](https://user-images.githubusercontent.com/67875325/225190247-d6f5c23c-4c80-428b-8b06-47a6def714d4.png)
Some interesting notes while running are that most movement comes from a link scraping the ground to push the robot along. Also because of my fitness function, sometimes the robot will fall over to attempt to "move" the root link.

To run my version, run the search.py program. In constants.py, you can change the numberOfGenerations and populationSize (parallel) to have longer or shorter evolutions.

For footage of my robots, check https://www.youtube.com/watch?v=h7Gf_g5aqw8.
Now, you too can attempt to make your own evolving robot with your own version of mutations. Have fun!
