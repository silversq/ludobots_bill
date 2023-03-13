import os
from parallelhillclimber import PARALLEL_HILL_CLIMBER
import numpy
import matplotlib.pyplot as plt

two = [1.2500980711661482, 1.7768963437693066, 2.311185498439899, 2.7269479181874208, 2.7269479181874208, 2.7269479181874208, 2.7269479181874208, 3.3613230177868, 3.3613230177868, 3.3613230177868, 3.3613230177868, 3.3613230177868, 3.3613230177868, 3.3613230177868, 3.3613230177868, 5.492625560841994, 5.492625560841994, 5.492625560841994, 5.508107418057576, 5.508107418057576, 7.817731714420855, 7.817731714420855, 7.817731714420855, 7.817731714420855, 7.817731714420855, 7.817731714420855, 7.817731714420855, 7.817731714420855, 7.817731714420855, 7.817731714420855, 7.817731714420855, 7.817731714420855, 7.817731714420855, 7.817731714420855, 7.817731714420855, 7.817731714420855, 7.817731714420855, 7.817731714420855, 7.817731714420855, 7.817731714420855, 7.817731714420855, 7.817731714420855, 7.817731714420855, 7.817731714420855, 7.817731714420855, 7.817731714420855, 7.817731714420855, 7.817731714420855, 7.817731714420855, 7.817731714420855, 7.817731714420855, 7.817731714420855, 7.817731714420855, 7.817731714420855, 
7.817731714420855, 7.817731714420855, 7.817731714420855, 7.817731714420855, 7.817731714420855, 7.817731714420855, 7.817731714420855, 7.817731714420855, 7.817731714420855, 7.817731714420855, 7.817731714420855, 7.817731714420855, 7.817731714420855, 7.817731714420855, 7.817731714420855, 7.817731714420855, 7.817731714420855, 7.817731714420855, 7.817731714420855, 7.817731714420855, 7.817731714420855, 7.817731714420855, 7.817731714420855, 7.817731714420855, 7.817731714420855, 7.817731714420855, 7.817731714420855, 7.817731714420855, 7.817731714420855, 7.817731714420855, 7.817731714420855, 7.817731714420855, 7.817731714420855, 7.817731714420855, 7.817731714420855, 7.817731714420855, 7.817731714420855, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 
15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 
15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 
15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 
15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106, 15.262953005695106]
one = [1.279975468039015, 1.973399356078591, 2.863548878635756, 2.863548878635756, 2.863548878635756, 2.863548878635756, 4.211701311429558, 4.211701311429558, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 
8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 8.7900585561057, 10.061419743274147, 10.061419743274147, 10.061419743274147, 10.061419743274147, 10.061419743274147, 10.061419743274147, 10.061419743274147, 10.061419743274147, 10.061419743274147, 10.061419743274147, 10.061419743274147, 10.061419743274147, 10.061419743274147, 10.061419743274147, 10.061419743274147, 10.061419743274147, 10.061419743274147, 10.061419743274147, 10.061419743274147, 10.061419743274147, 10.061419743274147, 10.061419743274147, 10.061419743274147, 10.061419743274147, 10.061419743274147, 10.061419743274147, 10.061419743274147, 10.061419743274147, 10.061419743274147, 10.061419743274147, 10.061419743274147, 10.061419743274147, 10.061419743274147, 10.061419743274147, 10.061419743274147, 10.061419743274147, 10.061419743274147, 10.061419743274147, 10.061419743274147, 10.061419743274147, 10.061419743274147, 10.061419743274147, 10.061419743274147, 10.061419743274147, 10.061419743274147, 10.061419743274147, 10.061419743274147, 10.061419743274147, 10.061419743274147, 
10.061419743274147, 10.061419743274147, 10.061419743274147, 10.061419743274147, 10.061419743274147, 10.061419743274147, 10.061419743274147, 10.061419743274147, 10.061419743274147, 10.061419743274147, 10.061419743274147, 10.061419743274147, 10.061419743274147, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 
14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 
14.472627986199896, 14.472627986199896, 14.472627986199896, 14.472627986199896, 28.904498491725676, 28.904498491725676, 28.904498491725676, 28.904498491725676, 28.904498491725676, 28.904498491725676, 28.904498491725676, 28.904498491725676, 28.904498491725676, 28.904498491725676, 28.904498491725676, 28.904498491725676, 28.904498491725676, 28.904498491725676, 28.904498491725676, 28.904498491725676, 28.904498491725676, 28.904498491725676, 28.904498491725676, 28.904498491725676, 28.904498491725676, 28.904498491725676, 28.904498491725676, 28.904498491725676, 28.904498491725676, 28.904498491725676, 28.904498491725676, 28.904498491725676, 28.904498491725676, 28.904498491725676, 28.904498491725676, 28.904498491725676, 28.904498491725676, 28.904498491725676, 28.904498491725676, 28.904498491725676, 28.904498491725676, 28.904498491725676, 28.904498491725676, 28.904498491725676, 28.904498491725676, 28.904498491725676, 28.904498491725676, 28.904498491725676, 28.904498491725676, 28.904498491725676, 28.904498491725676]
three = [2.7873080959859626, 2.7873080959859626, 3.32073326617639, 3.32073326617639, 6.2310959727837165, 6.2310959727837165, 6.2310959727837165, 6.2310959727837165, 6.2310959727837165, 6.2310959727837165, 6.2310959727837165, 6.2310959727837165, 6.2310959727837165, 6.2310959727837165, 7.179590575001648, 7.179590575001648, 14.187200062779986, 14.187200062779986, 14.187200062779986, 14.187200062779986, 14.187200062779986, 14.187200062779986, 14.187200062779986, 14.187200062779986, 14.187200062779986, 14.187200062779986, 14.187200062779986, 14.187200062779986, 14.187200062779986, 14.187200062779986, 14.187200062779986, 14.187200062779986, 14.187200062779986, 14.187200062779986, 14.187200062779986, 14.187200062779986, 14.187200062779986, 14.187200062779986, 14.187200062779986, 14.187200062779986, 14.187200062779986, 14.187200062779986, 14.187200062779986, 14.187200062779986, 14.187200062779986, 14.187200062779986, 14.187200062779986, 14.187200062779986, 14.187200062779986, 14.187200062779986, 14.187200062779986, 14.187200062779986, 14.187200062779986, 14.187200062779986, 14.187200062779986, 14.187200062779986, 14.187200062779986, 14.187200062779986, 14.187200062779986, 14.187200062779986, 14.187200062779986, 14.187200062779986, 14.187200062779986, 14.187200062779986, 14.187200062779986, 14.187200062779986, 14.187200062779986, 14.187200062779986, 14.187200062779986, 14.187200062779986, 14.187200062779986, 14.187200062779986, 14.187200062779986, 14.187200062779986, 14.187200062779986, 14.187200062779986, 14.187200062779986, 14.187200062779986, 14.187200062779986, 14.187200062779986, 14.187200062779986, 14.187200062779986, 14.187200062779986, 14.187200062779986, 14.187200062779986, 
14.187200062779986, 14.187200062779986, 14.187200062779986, 14.187200062779986, 14.187200062779986, 14.187200062779986, 14.187200062779986, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 
20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 
20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 
20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 
20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602, 20.14344797729602]
four = [4.341033733299073, 4.756370577857105, 4.756370577857105, 4.756370577857105, 4.756370577857105, 4.756370577857105, 4.756370577857105, 4.756370577857105, 6.063813285067361, 6.063813285067361, 6.063813285067361, 6.063813285067361, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 
14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 14.68417443421944, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 
21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 
21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 
21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172, 21.57125800897172]
# x = [i for i in range(0, 150)]
# plt.plot(x, [-j for j in one], label='random seed 1')
# plt.plot(x, [-j for j in two], label='random seed 2')

# plt.plot(x, [-j for j in three], label='random seed 3')
# plt.plot(x, [-j for j in four], label='random seed 4')
# plt.plot(x, [-j for j in five], label='random seed 5')
# plt.legend()
# plt.show()
phc = PARALLEL_HILL_CLIMBER()
phc.EVOLVE()
phc.Show_Best()

# for i in range(5):
#     os.system("py generate.py")
#     os.system("py simulate.py")*-     