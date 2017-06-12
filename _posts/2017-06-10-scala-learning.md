---
published: false
---


## Install Scala


```
brew install scala
```

Refer to [this tutorial](https://www.jetbrains.com/help/idea/creating-and-running-your-scala-application.html) on setting up scala development environment on IntelliJ, which is my favourite. 


## Week 1

- Call-by-name
    - Apply the function to unreduced arguments
    - `square(3) + square(2+2)`
- Call-by-value
    - Reduce function arguments to value before rewriting the function application
- If CBV evaluation of an expression terminates, then CBV evaluation terminates
    - the other direction is not true
    - `def first(x: Int, y: Int) = x`
- Scala normally uses call-by-value
    - `=>` uses call-by-name
- `def` is by name
- `val` is by value

- Exercises

```
def and(x: Boolean, y: => Boolean) = if (x) y else false

def or(x: Boolean, y: => Boolean) = if (x) true else y
```

- Square roots with Newton's method
    
```scala

def sqrtIter(guess: Double, x: Double): Double = 
    if(isGoodEnough(guess, x)) guess
    else sqrtIter(improve(guess, x), x)

def improve(guess: Double, x: Double) = 
    (guess + x / guess) / 2
    
def isGoodEnough(guess: Double, x: Double) =
    abs(guess * guess - x) < 0.001

```

The above `isGoodEnough` is not precise for small numbers because it is likely that the programme will end before enough due to 0.001. Also, it does not terminate for large numbers because float calculation makes the difference large than 0.001.

The revised version is as below

```
def isGoodEnough(guess: Double, x: Double) =
    abs(guess * guess - x) / x < 0.001
```

- Block
    - {}
    - last element is an expression that defines its value
    - definitions inside a block are 
        - only visible from within the block
        - shadow definitions of the same name outside the block
    - Lexical scope

- Tail recursion
    - If a function calls itself as its last action, the function's stack frame can be reused
    - iterative processes
    
```
def factorial(n: Int): Int = {
    def loop(acc: Int, n: Int): Int = 
        if (n ==0) acc
        else loop(acc * n, n -1)
    
    loop(1, n)
}

```