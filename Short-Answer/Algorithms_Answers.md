#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I
```
a)  a = 0
    while (a < n * n * n):
      a = a + n * n
```

a) The runtime complexity here is O(n). The loop checks if 'a' is less than n^3 and then adds n^2 with each iteration. It would take n times to iterate through the loop entirely. 

```
b)  sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
```

b) I originally thought this was O(n**2) as theres 2 loops and one is nested. However, the j *=2 implies a logarithmic running time, since every time the inner loop doubles, j doubles. So maybe O(nlogn)?

```
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```

c) Also a little tricky, but this function is being called recursively n (or bunnies) times before
reaching the base case, so I believe its just O(n). 

## Exercise II

Binary search is the first option that came to mind when assessing the problem. Say the building has 100 floors, instead of dropping an egg from each floor, you could just start at the middle floor. This way, if the egg breaks, you know that no floor above that floor would be safe to drop the egg. You also know that that middle floor isnt safe, so you'd set the floor below it to the new top floor and repeat the process, drastically cutting out floor possibilites (and broken eggs) until you find your breaking point. 

```
def binary_search(floors, breaking_point):
    bottom_floor = 0
    top_floor = len(floors) - 1
    # Loop through the floors
    while bottom_floor <= top_floor:
        # Start your search at the middle floor
        mid = (top_floor + bottom_floor) // 2
        # If the egg breaks, you know you don't need to check higher
        if breaking_point <= floors[mid]:
            # You can eliminate all the floors above
            top_floor = mid
        # If the egg doesn't break, no need to check lower
        if breaking_point > floors[mid]:
            # Eliminate all lower floors, including the middle floor where you started,
            # and re-check using the floors above
            bottom_floor = mid + 1 
```