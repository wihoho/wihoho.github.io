---
layout: post
title: Scala Learning Notes
---

## Install Scala


```
brew install scala
```

Refer to [this tutorial](https://www.jetbrains.com/help/idea/creating-and-running-your-scala-application.html) on setting up scala development environment on IntelliJ, which is my favourite. 


## Week 1 - Functions and Evaluations

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

```scala
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

```scala
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
    
```scala
def factorial(n: Int): Int = {
    def loop(acc: Int, n: Int): Int = 
        if (n ==0) acc
        else loop(acc * n, n -1)
    
    loop(1, n)
}

```

- My own solutions to exercises
```scala
package recfun

object Main {
  def main(args: Array[String]) {
    println("Pascal's Triangle")
    for (row <- 0 to 10) {
      for (col <- 0 to row)
        print(pascal(col, row) + " ")
      println()
    }
  }

  /**
    * Exercise 1
    */
  def pascal(c: Int, r: Int): Int =
    if (c == 0 && r == 0) 1
    else if (r < 0 || c < 0 || c > r) 0
    else pascal(c - 1, r - 1) + pascal(c, r - 1)

  /**
    * Exercise 2
    */
  def balance(chars: List[Char]): Boolean = {
    def helper(chars: List[Char], left: Int): Boolean =
      if (chars.isEmpty && left == 0) return true
      else {
        var cur = chars.head
        if (cur == '(') {
          return helper(chars.tail, left + 1);
        } else if (cur == ')') {
          if (left <= 0) {
            return false
          } else {
            return helper(chars.tail, left - 1);
          }
        } else {
          return helper(chars.tail, left);
        }
      }

    helper(chars, 0)
  }

  /**
    * Exercise 3
    */
  def countChange(money: Int, coins: List[Int]): Int = {
    if (money == 0) 1
    else if (money < 0 ) 0
    else if (coins.isEmpty) 0
    else {
      countChange(money - coins.head, coins) + countChange(money, coins.tail)
    }
  }
}

```

## Week 2 - Higher order functions

* Higher order functions
    * take other functions as parameters or that return functions as results

```scala
def sum(f: Int => Int, a:Int, b:Int): Int = 
    if (a > b) 0
    else f(a) + sum(f, a + 1, b)
```

* Anonymous function
    
```scala
(x: Int) => x * x * x
```

* Currying
    * evaluation of a function that takes multiple arguments => a sequence of functions, each with a single argument

* Scala syntax summary
    * Type
        * numeric, boolean, string, function..
    * Expression
        * identifier, literal, function, operator, selection, conditional expression, block, anonymous function
    * Definition
        * function & value

* Class and Object
```scala
class Rational(x: Int, y: Int) {
  def numer = x
  def denom = y
  
  // method
  def add(r: Rational) =
      new Rational(numer * r.denom + r.numer * denom,
                   denom * r.denom)
                   
  // self reference
  def less(that: Rational) =
      numer * that.denom < that.numer * denom
        
  def max(that: Rational) =
      if (this.less(that)) that else this
}
```

* Precondition
    * `require(y > 0, ”denominator must be positive”)`
    * enforce a precondition on the caller of a function

* Assertion
    * `assert(x >= 0)`
    * check the code of the function itself
    
* Constructor
    * primary 
    * auxiliary

## Week 3 - Data and abstraction

* Abstract class
    * missing an implementation

```scala
 abstract class IntSet {
    def incl(x: Int): IntSet
    def contains(x: Int): Boolean
}
```

* Class extensions

```scala
class Empty extends IntSet {
  def contains(x: Int): Boolean = false
  def incl(x: Int): IntSet = new NonEmpty(x, new Empty, new Empty)
}

class NonEmpty(elem: Int, left: IntSet, right: IntSet) extends IntSet {
  def contains(x: Int): Boolean =
    if (x < elem) left contains x
    else if (x > elem) right contains x
    else true
    
  def incl(x: Int): IntSet =
    if (x < elem) new NonEmpty(elem, left incl x, right)
    else if (x > elem) new NonEmpty(elem, left, right incl x) else this
}
```

* Object definitions
```scala
object Empty extends IntSet {
  def contains(x: Int): Boolean = false
  def incl(x: Int): IntSet = new NonEmpty(x, Empty, Empty)
}
```

* Dynamic binding
    * invoked by a method call depends on the runtime type of the object

* Packages and imports
    
```scala
package progfun.examples
import week3.Rational
```

* Automatic imports
    * scala, java.lang, scala.Predef
    
* Polymorphism
    * syntax
        * value parameter
        * type parameter
    * two principal forms
        * subtyping
        * generics
   
    
```scala
package week4

trait List[T]
class Cons[T](val head: T, val tail: List[T]) extends List[T]
class Nil[T] extends List[T]
```

## Week 4 - Types and Pattern Matching

* Type bounds
    * S <: T means S is a subtype of T
    * S >: T means S is supertype of T
    * mixed bounds
        * [S >: NonEmpty <: IntSet]
        
* Covariance
    * subtyping relationship varies with the type paramter
    * A <: B leads to List[A] <: List[B]

* Liskov Substitution principle
    * If A <: B, then everything one can to do with a value of type B one should also be able to do with a value of type A
    
* Variance
    * covariant: C[+A]
    * contravariant: C[-A]
    * nonvariant: C[A]
    * checking rule
        * covariant type can only appear in method results
        * contravariant can only appear in method paramters
        * invariant type can appear anywhere
        
* Function trait 

```scala
package scala

trait Function[-T, +U] {
  def apply(x: T): U
}
```

* Pattern match
    * case class `case class Number`
        * implicitly defines companion objects with `apply`
            * `Number(1)` instead of `new Number(1)`
    * generalization of `switch` from C/Java        

```scala
def eval(e: Expr): Int = e match {
    case Number(n) => n
    case Sum(e1, e2) => eval(e1) + eval(e2)
}
```

## Week 5 - Lists
* List
    * immutable, recursive, homogeneous
    * List(), Nil
    * head, tail, isEmpty
    * p :: ps
    * xs.length, xs.last, xs.init, xs take n, xs drop n, xs(n)
    * xs ++ ys, xs.reverse, xs updated (n, x), xs indexOf x, xs contains x
    
* Merge sort

```scala
def msort(xs: List[Int]) : List[Int] = {
  val n = xs.length / 2
  if(n == 0) xs
  else {
    def merge(xs: List[Int], ys: List[Int]) = ???
    val (fst, snd) = xs splitAt n
    merge(msort(fst), msort(snd))
  }
}

def merge(xs: List[Int], ys: List[Int]) =
    (xs, ys) match  {
      case (Nil, ys) => ys
      case (xs, Nil) => ys
      case (x1::y1, x2::y2) => {
        if(x1 < x2) x1::merge(y1, ys)
        else x2::merge(xs, y2)
      }
    }
```

* Pair and Tuple

* Implicit parameters
    * `def msort[T](xs: List[T])(implicit ord: Ordering)`

* Map
    * `xs map (x => x * factor)`
* Filter
    * `xs filter (x => x > 0)`
    * filterNot
    * partition
    * takeWhile
    * dropWhile
    * span
    
```scala
def pack[T](xs: List[T]): List[List[T]] = xs math {
  case Nil => Nil
  case x :: xs1 => 
    val (first, rest) = xs span (y=>y==x)
    first::pack(rest)
}

def encode[T](xs: List[T]): List[(T, Int)] =
    pack(xs) map (ys => (ys.head, ys.length))
```

* ReduceLeft
    * sum = `(0::xs) reduceLeft ((x,y)=>x+y)`

* FoldLeft
    * `(xs foldLeft 0)(_ + _)`
    * `(xs foldLeft 1)(_ * _)`

```scala
def reverse[a](xs: List[T]): List[T] =
    (xs foldLeft List[T]())((xs, x) => x::xs)
```

* ReduceRight and FoldRight

## Week 6 - Collections
* Vector
    * backed by a little endian bit-mapped vector trie with a branching factor of 32
    * balanced access patterns than List

* Collection hierarchy
    * Iterable
        * Seq
            * String
            * Array
            * List
            * Vector
            * Range
                * `1 to 10 by 3`
        * Set
        * Map
    
* More `Seq` operations
    * xs exists p, xs forall p, xs zip ys, xs.unzip, xs.flatMap f, xs.sum, xs.product, xs.max, xs.min

* For-expression
    * `for ( s ) yield e`
    * s is a seuqnce of generators and filters
    * `(for ((x,y) <- xs zip ys) yield x * y).sum`

* Set
    * `val fruit = Set(”apple”, ”banana”, ”pear”)`
    * unordered, no duplicate, `contains`

* Map
    * `val cap1 = capitalOfCountry withDefaultValue "unknown""`
    
* sorted and GroupBy
    * `fruit sortWith (_.length < _.length)`
    * `fruit groupBy (_.head)`