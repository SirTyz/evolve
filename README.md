# evolve
A start at messing with genetic algorithms.

A creature has 6 traits that can be adjusted to increase or decrease evolutionary success

   * **speed:** Determines how fast a creature moves
   * **size:** Determines how much food a creature can consume
   * **maxSize:** Determines the biggest size a creature can achieve through growing
   * **energy:** How long a creature can go without eating
   * **safety:** A determining statistic to help a creature decide if it is ready to reproduce
   * **growthRate:** How much a creature's size increases when it has a surplus of food


The environment has 6 traits that can be adjusted to affect all creatures

  * **FOOD_ABUNDANCE:** Percentage chance how often a creature will find food
  * **ENERGY_CONSUMPTION:** How much energy creatures burn throughout the day
  * **DAYS_BETWEEN_SEASON:** How many days before a new generation of creatures is born
  * **GENERATIONS:** How many generations of creatures will be born before the simulation is stopped
  * **MUTATION_SEVERITY:** How strong will mutations be if they happen to a creature
  * **MUTATION_CHANCE:** Likelihood of a creature having a mutation 


[This article is](https://medium.com/sigmoid/https-medium-com-rishabh-anand-on-the-origin-of-genetic-algorithms-fc927d2e11e0) what helped me get a grasp on where I needed to start. I also got inspiration from watching [Primer](https://www.youtube.com/channel/UCKzJFdi57J53Vr_BkTfN3uQ).

