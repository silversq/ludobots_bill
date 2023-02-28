# 3D creature

This is a random creature generator trying to go in the -x direction. It will generate a creature containing a random number of links that have a random chance to become a sensor. Each sensor will be able to move the joints when it touches the floor. Body generation will choose from random available faces from each link. It will then check for overlaps with previously made links, and if there is no overlap, create a new link at that face. With PHC, 20 parallel creatures will be formed and mutate through 150 generations. Each mutation will either add a link or change a non-sensor link to a sensor. After the mutation, it will find the creature with the best fitness and the next mutation will be on that creature. It will repeat for all generations.

To run the program, run search.py.

All information for setting up the bots was found in the reddit ludobots instructions starting here:

https://www.reddit.com/r/ludobots/wiki/installation/

Neural Network for robots gotten from pyrosim:
https://github.com/jbongard/pyrosim

Below is a diagram containing fitness curves of the creatures with 5 different random seeds:
![Figure_1](https://user-images.githubusercontent.com/67875325/221719952-3fbce6a1-3dcf-4283-bfbd-9732da2632f7.png)

Below is a diagram illustrating the body and brain generation:

![20230227_171729](https://user-images.githubusercontent.com/67875325/221718886-d7adf3ad-2da1-4019-bfce-88c3f642dc40.jpg)
![20230227_171736](https://user-images.githubusercontent.com/67875325/221718861-43a55cf9-103a-4964-a17b-29f507aac4e6.jpg)
