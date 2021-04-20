# Activity 12: Fast Arrays
![GitHub Classroom Workflow](../../workflows/GitHub%20Classroom%20Workflow/badge.svg?branch=main) ![Points badge](../../blob/badges/.github/badges/points.svg)


https://asu-compmethodsphysics-phy494.github.io/ASU-PHY494//2021/04/08/15_PDEs/

## Problem

Solve the
[Exercise](https://nbviewer.jupyter.org/github/ASU-CompMethodsPhysics-PHY494/PHY494-resources/blob/master/15_PDEs/numpy_arrays.ipynb#Exercise):

Use numpy arrays to calculate for a vector `b` (numpy array) of length `N`

```
y[i] = 0.5 * (b[i−1] + b[i+1])
```

and set 
```
y[0] = y[N−1] = end
```
where `end` is a number.


Write a function `avg_neighbors(b, end=100)` that takes `b` as input
and returns `y` as output. Add your code to the file `exercise.py`.



