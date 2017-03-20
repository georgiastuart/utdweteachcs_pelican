# Operators and Truth Values

In this section we'll discuss

2. Arithmetic operators
3. Truth values and relational operators

**Note:** the demonstrations in this page will only be done in Trinket. However,
there are similar blocks that work much the same in Scratch.

## Arithmetic operators

*Arithmetic operators*{: class="definition" }
will look very similar from math class! Addition,
subtraction, multiplication, and division in Scratch, Trinket Blocks, and
Python 3 work the same way as you would expect in math class.

In future weeks, we will discuss operations on
*integers*{: class="definition" } and
*floating point numbers*{: class="definition" }
(numbers that a computer can store) in greater detail. For now, just remember
that there is rounding occurring that you may or may not notice (just like
on a calculator).

### Using the basic arithmetic operators in Trinket blocks

{!content/pages/modules/module_01/html_partials/arithmetic_trinket.html!}

#### Test it out

{!content/pages/modules/module_01/html_partials/basic_arithmetic_trinket_embed.html!}

### Other arithmetic operators

In addition to the four basic operators, we can use the
*integer division operator*{: class="definition" } and the
*modulus operator*{: class="definition" }.

#### Integer division

The *integer division operator*{: class="definition" } (denoted `//`) is division where the
remainder is discarded, i.e. the *integer* number of times one number goes
into another.

For example,

```python
10 // 2 == 5
```

Since 2 goes into 10 five times. However,

```python
10 // 3 == 3
```

Since 3 only goes into 10 three times before we need a decimal. If the second
number is bigger than the first, then

```python
10 // 11 == 0
```

Since 11 does not divide 10 a whole number of times at all.

#### Modulus operator

The *modulus operator*{: class="definition" } (denoted `%`) is the remainder operator.
The modulus returns what's left over when you divide one number by another.

**note:** here we discuss only positive integers with the modulus operator.

For example,

```python
10 % 2 == 0
```

Since 2 divides 10 with no remainder leftover. However,

```python
10 % 3 == 1
```

Since 3 divides 10 with 1 left over. If the second number is greater than
the first then

```python
10 % 11 == 10
```

Since 11 does not divide 10 at all, thus 10 is left over.

#### Trinket Testing

The following trinket is set up for you to play with integer division and modulus.

{!content/pages/modules/module_01/html_partials/modulus_trinket_embed.html!}

## Truth Values and Relational Operators

In addition to the *number*{: class="definition" } and *text*{: class="definition" }
types of values we've discussed so far, there are *boolean*{: class="definition" }
types that can take one of two values. In this case, we have *true*{: class="definition" }
 and *false*{: class="definition" }.

A *relational operator*{: class="definition" } examines the relationship between
two values and returns whether than relation is true or false.

For example, Trinket blocks (and Python) defines equals, not equals, less than, less than or equals to,
greater than, and greater than or equals to.

<img class="img-responsive" src="/images/module-01/relational-operators.gif"></img>

In future weeks we'll discuss the rules for combining truth values in different ways
(important to the *discrete math*{: class="definition" } portion of the
certification exam)!

## Knowledge Check

Please complete each knowledge check before moving on.

[Knowledge Check: Variables](https://utdallas.qualtrics.com/jfe/form/SV_39v6ZVaAhHZHuE5){: class="btn btn-success btn-lg btn-knowledge" role="button" target="_blank" }
{: class="text-center" }






