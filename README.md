# High Performance project
## Parallel processing

Through the simultaneous execution of several data processing operations, parallel processing helps computer systems operate with greater efficiency. But how does it work? In this project, we will discuss in detail how it works and what it does. 

First of all, what is it? Well, It is a computer technique known as parallel processing that occurs when several central processing units (CPUs) carry out several streams of calculations or data processing activities at the same time.

When a task is divided into multiple processors, it can reduce the amount of time that a program takes to execute. Parallel processing is possible with multi-core processors, which are often seen in modern computers and any device that has more than one CPU.

Multi-core processors are integrated circuit (IC) systems containing two or more CPUs for increased speed, reduced power consumption, and more efficient management of multiple tasks. Some computers contain as many as twelve cores, but most only have two or four. Parallel processing is commonly used to accomplish intricate processes and computations.

Let’s introduce the Monte Carlo Simulation, also known as the Monte Carlo method. This is a statistical technique used to estimate the possible outcomes of an uncertain event, it predicts a range of values versus a set of fixed input values to forecast a set of outcomes. In other words, for every variable that has intrinsic uncertainty, a Monte Carlo Simulation uses a probability distribution, like a uniform or normal distribution, to develop a model of potential outcomes.

But why is it important in this context? For starters, this is a great way to demonstrate how Parallel Processing works, by making use of its capabilities to accelerate the Monte Carlo Method. Parallel processing drastically cuts down on the amount of time needed to finish a Monte Carlo simulation by splitting up the calculations across several cores or processors, especially when working with complicated models or big datasets.

Some important tools that need to be mentioned are ‘cProfile’ and ‘%timeit’ are used in this project; they are both tools used in Python for performance analysis, profiling, and benchmarking.

‘cProfile’ provides deterministic profiling of Python programs. A profile is a set of statistics that describes how often and for how long various parts of the program are executed. These statistics can be then formatted into reports. On the other hand ‘timeit’ provides a simple way to time small bits of a Python code. They are very useful to get a quick estimate of the performance on a specific line or block of code.
