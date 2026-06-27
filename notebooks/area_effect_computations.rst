Area Effect Aspect Volume Computations
======================================

The *OpenD6 Fantasy* rules define an Area of Effect aspect that applies
to magical spells and religious invocations. This aspect has a
relatively simple set of rules:

::

   Two-dimensional circle (a few centimeters thick): +1 per half-meter radius.

   Three-dimensional sphere (for explosions and 3D illusions): +5 per meter radius and +1 bonus to hit one target (bonus is applied to the same target).

   One alternate shape: +1 to area effect modifier.

   Several alternate shapes (specific one chosen at time of casting): +3 to area effect modifier.

   Fluid shape (shape may change any time during spell’s duration): +6 to area effect modifier.

We can break this rule text into two kinds of statements:

1. **Shape definitions**. Examples: 2D circle vs. 3D sphere.
2. **Modifiers**. This includes the idea of alternate shapes and fluid
   shape.

Seems simple, right?

Sadly, there are spells in the *OpenD6 Fantasy Locations*, where the
sphere definition harbors a subtle error. This was uncovered by
wrestling four four spells that have “fluid shape” modifiers. We’ll need
to take a short journey into some relatively simple math to uncover a
small piece of treasure.

It gets worse. The (unpublished) *OpenD6 Magic Guide* has a number of
shapes, and the rules for these seem to be broken. This will be a longer
journey, deep into a wilderness that involves more serious algebra. This
will yield a delightful, but, hardly useful piece of treasure. A kind of
trophy with little practical value.

OpenD6 Fantasy Locations spells
-------------------------------

Our journey begins in the the *OpenD6 Fantasy Locations* rules. There,
we will uncover four spells with the *Fluid Shape* variant of the *Area
of Effect* aspect:

-  The **Basic Shelter** spell, has an area effect difficulty of 6.

   The difficulty matches the “Fluid Shape” modifier, but the spell
   definition fails to explicitly state a shape. The spell does describe
   a volume of :math:`1.25 \times 2 \times 2 = 5` cubic meters. The
   *OpenD6 Fantasy* rules provide no definition for a rectilinear
   (“cuboid”) shape.

-  The **Improved Hut** spell, with an area effect difficulty of 11.

   This has the “Fluid Shape” modifier. But, it also seems to have an
   implied – but not stated – shape with a difficulty of 5. The spell
   describes a volume of :math:`4 \times 4 \times 2 = 32` cubic meters.

-  The **Small Long-Lasting Tower** and **Keep-in-the Air** spells have
   an area effect difficulty of 26.

   These two spells also seems to use the “Fluid Shape” with an implied
   shape that starts with a difficulty of 20. The spell describes a
   volume not to exceed 268 cubic meters.

The problem here is that the *Fluid Shape* modifier seems to require a
base shape definition. There’s no irrefutable evidence of this
requirement, since there are no examples of fluid shapes in the *OpenD6
Fantasy* rules. It is a pretty clear intent, however.

With the assumption that the *Fluid Shape* modifier (worth 6) applies to
some base shape, we have to conclude this shape is a 5 cubic meter
sphere with a difficulty of zero. The volume of a sphere is
:math:`V = \frac{4}{3} \pi r^3`. The radius for volume of 5 cubic meters
means :math:`r = \sqrt[3]{\frac{3V}{4\pi}} \approx 1.06`.

Superficially, this conclusion does not follow the rules. The rules say
“**+5 per meter radius**”: a 1m radius sphere must a cost of 5. Not
zero.

We have one of two problems: Either

-  the cost is wrong for some of these spells, or
-  the “+5 per meter radius” statement is wrong.

There are consequences to which of these problems the rules suffer from:

-  Assuming the proper rule was supposed to be **+5 per meter after the
   first; a 1m sphere has a cost of zero.**, then the **Small
   Long-Lasting Tower** and **Keep-in-the Air** spells should have a
   difficulty of 21, not 26.

-  Assuming the proper rule is **+5 per meter**, then the **Basic
   Shelter** spell difficulty needs to be 11 (not 6) and the **Improved
   Shelter** spell difficulty needs to be 16 (not 11).

When we look at other spells, *i.e.* Fantasy Apportation spell
**Carrying Wind**, we see “Area Effect (+15): 3-meter sphere”. This is
conclusive evidence the rule – as written – was correct. The two spells
(**Basic Shelter** and **Improved Shelter**) have the wrong difficulties
for their areas of effect.

[*The rules also have numerous “off-by-one” errors, many due to
rounding. This isn’t a serious problem.*]

This leads to the following table of sphere sizes and difficulty values:

.. code:: ipython3

    from IPython.display import display, Markdown
    from tabulate import tabulate
    from contextlib import redirect_stdout
    from io import StringIO

.. code:: ipython3

    from sympy import pi
    
    header = ["r (meters)", "volume (cubic meters)", "difficulty"]
    data = [
        [r, f"{(4/3)*pi*r**3:.2f}", f"+{r*5}"]
        for r in range(1,7)
    ]
    md = Markdown(tabulate(data, headers=header, tablefmt="pipe"))
    display(md)



========== ===================== ==========
r (meters) volume (cubic meters) difficulty
========== ===================== ==========
1          4.19                  +5
2          33.51                 +10
3          113.1                 +15
4          268.08                +20
5          523.6                 +25
6          904.78                +30
========== ===================== ==========


We’ve started this journey by uncovering a tiny editing error in an
obscure corner of the rules. Two spells with incorrect computations for
difficulty.

This is only the start of a much longer journey into a wilderness of
TTRPG rules. We’ll turn to the never-officially-published *OpenD6 Magic
Guide*.

Magic Guide Additional Shapes
-----------------------------

The (unpublished) *OpenD6 Magic Guide* has a number of other shapes that
are part of the Area of Effect aspect:

-  2D shapes. We’ll skip these, they rules seem simple enough.

   -  Circle. :math:`A = \pi r ^ 2`.
   -  Wall. :math:`A = h w`.
   -  Blast. :math:`A = \pi r ^ 2`. The radius varies with the distance
      from the caster. This seems to matter when sorting out the targets
      of a spell during play.

-  3D shapes.

   -  Hemisphere. :math:`V = \frac{2}{3} \pi r^3`.
   -  Cone. :math:`V = \frac{1}{3} h \pi r^2`.
   -  Cuboid. :math:`V = h w d`.
   -  Cylinder. :math:`V = h \pi r^2`.
   -  Pyramid. (Incorrectly stated in the rules)
      :math:`V = \frac{1}{3} h w_b l_b`.

The rules provide some “rule of thumb” computations for difficulty. The
idea is to avoid the complex-looking math required to work out a
difficulty based on volume. The rules of thumb seem vaguely wrong.

Further, when we look specifically at cuboid and compare the difficulty
results with the four Fantasy Location spells, we have a serious
discrepancy. The cuboid rules for volume of 268 cubic meters seem to
assign a difficuilty of 268!

That’s not sensible.

We can try to use the Value-Measure table, but the difficulty winds up
12 instead of 26.

Since these rules were unpublished, it seems sensible to assume that
this detail suffered from a lack of play-testing and editorial
oversight. It’s simply wrong.

What can we do? We’ll need to wander through the forest of shapes to see
how we can work with other shapes as simply as spheres. We’ll start with
a deep dive into spheres.

Core Difficulty and Volume
~~~~~~~~~~~~~~~~~~~~~~~~~~

The rules overall seem clear enough on one point: for three-dimensional
shapes, the difficulty grows with the volume. The volume of a sphere,
:math:`V`, with radius :math:`r`, is stated explicitly, with one tiny
omission.

The difficulty for a spherical Area of Effect is computed directly from
the radius, :math:`r`: :math:`d = 5 \times r`.

We’ll take this as a golden truth. We can turn this relationship around:
given a volume, we can work out the radius of a sphere with that volume.
This approach lets us compute the difficulty for any given volume,
:math:`V`.

In order to do the algebra correctly, we need help. We’re going to rely
on software tools. Specifically, the **sympy** package. See
https://docs.sympy.org/latest/index.html.

A little setup: we’ll import the package, initialize formula printing,
and define a few symbols that will be used through the rest of the
story.

.. code:: ipython3

    from sympy import *
    init_printing()
    V, R, r, l, w, h, d = symbols("V R r l w h d")

Here’s the formula for volume of a Sphere.

We’ll start with spheres because the answers are known. This easily
generalizes to any shape that has a volume. What matters is the value
for :math:`V`.

.. code:: ipython3

    sphere = Eq(V, Rational(4,3)*pi*r**3)
    sphere




.. math::

    \displaystyle V = \frac{4 \pi r^{3}}{3}



We can solve this for :math:`r`.

.. code:: ipython3

    Eq(r, solve(sphere, r)[0])




.. math::

    \displaystyle r = \frac{\sqrt[3]{6} \sqrt[3]{V}}{2 \sqrt[3]{\pi}}



In the sphere case, computing volume from radius and then solving for
the radius is obviously pointless. In all other cases, however, we will
start with some formula that gives us a volume. From that volume, we can
then deduce the equivalent sphere radius and the difficulty for the
given shape.

The problem with solving for :math:`r` is we get an ugly-looking
formula. Really paralyzingly ugly. Kind of turn-to-stone if you look at
it, Medusa-scale of ugly.

The good news, is it has a form of :math:`S_s \sqrt[3]{V}`, where the
:math:`S_s` is the shape-specific constant, appropriate for spheres. You
don’t have to trust me on this. We’ll get out the crowbar and take these
formulae apart to see how the work inside.

The goal is to have a different constant for each of the other shapes.
We’re going to work out :math:`S_h` for hemisphere, :math:`S_c` for
cone, :math:`S_u` for cuboid, :math:`S_y` for cylinder and :math:`S_p`
for a pyramid.

We can, with some patience, manually extract the constant factor
(:raw-latex:`\frac{\sqrt[3]{6}}{2 \sqrt[3]{\pi}}`) from the above
equation. This is an unpleasant, error-prone manual operation. Here’s
what it looks like.

.. code:: ipython3

    N((6**(1/3))/(2*pi**(1/3)))*V**Rational(1,3)




.. math::

    \displaystyle 0.6203504908994 \sqrt[3]{V}



We can confirm that the algebra was done error-free, by trying to
simplify it. The messy-looking code blob represents the :math:`R_s`
constant value from the original equation.

.. code:: ipython3

    nsimplify((6**(1/3))/(2*pi**(1/3)), [pi])




.. math::

    \displaystyle \frac{\sqrt[3]{6}}{2 \sqrt[3]{\pi}}



Doing algebra manually to separate constants from variables is
unpleasantly complicated. We can do better. We have tools.

The formula crowbar
~~~~~~~~~~~~~~~~~~~

Specifically, the **sympy** toolbox has a crowbar we can use to pry the
formula into two distinct parts: a part with variables, and a part with
the constants.

How does this work?

Let’s visualize the formula by depicting the computation operations.
Each operation is shown in an oval which points to the arguments for
that operation. The final literal values (and the variable, :math:`V`)
are in ovals that don’t point anywhere.

What we see is the overall form of the equation is a multiplication. It
has four arguments, the first three of which are constants, and the
fourth includes a volume variable, :math:`V`.

.. code:: ipython3

    import graphviz

.. code:: ipython3

    graphviz.Source(dotprint(solve(sphere, r)[0]))




.. image:: area_effect_computations_files/area_effect_computations_21_0.svg



We can see the four arguments, with arrows flying out of the overall
``Mul`` operator node. A cube root operation, :math:`\sqrt[3]x`, is
represented internally using a ``Pow`` node, meaning
:math:`x^\frac{1}{3}`, which seems kind of awkward at first. However,
the pretty-printed output looks like an ordinary cube-root, allowing us
to disregard the nuances of the internal structure.

.. code:: ipython3

    solve(sphere, r)[0].args




.. math::

    \displaystyle \left( \frac{1}{2}, \  \sqrt[3]{6}, \  \frac{1}{\sqrt[3]{\pi}}, \  \sqrt[3]{V}\right)



We can compute the product of the first three factors, the constant
part. From these we can compute a simple-looking weighting factor that
converts the shape’s volume to the radius of a sphere.

.. code:: ipython3

    N(solve(sphere, r)[0].args[0] * solve(sphere, r)[0].args[1] * solve(sphere, r)[0].args[2])




.. math::

    \displaystyle 0.6203504908994



Pragmatically, we can’t guarantee that all of the shapes will have the
same node structure. To overcome the variability, we’ll define a
function to parse the formula, separating the constant factors from the
part of the expression with variables in it.

This **only** works for volume computations that are a simple multiply.
This is true for the five shapes we’re working with.

It avoids the need to do algebra manually.

.. code:: ipython3

    def constants(expr):
        """Only looks at the top-level Mul() node for constants and non-constant parts."""
        assert isinstance(expr, Mul), "Not a simple product"
        vars = [arg for arg in expr.args if not arg.is_constant()]
        cons = [arg for arg in expr.args if arg.is_constant()]
        if len(vars) == 1:
            return Mul(*cons), vars[0]
        else:
            return Mul(*cons), Mul(*vars)

Here’s how we use this function to decompose a formula into the
constants and the variables. Note that when we multiple the constant
product by the variable product, the equation is unchanged. This is
proof we haven’t damaged anything.

.. code:: ipython3

    cons, vars = constants(solve(sphere, r)[0])
    cons * vars




.. math::

    \displaystyle \frac{\sqrt[3]{6} \sqrt[3]{V}}{2 \sqrt[3]{\pi}}



.. code:: ipython3

    cons * vars == solve(sphere, r)[0]




.. parsed-literal::

    True



The ugly formula gives us an exact value for converting a Volume to a
radius. It doesn’t *seem* useful because it involves a bunch of
irrational numbers.

We can compute a useful approximation for the contant factor,
:raw-latex:`\frac{\sqrt[3]{6}}{2 \sqrt[3]{\pi}}`, which isn’t so
ugly.

.. code:: ipython3

    N(cons) * vars




.. math::

    \displaystyle 0.6203504908994 \sqrt[3]{V}



This approach lets us use volume equations for any shape. We can solve
for the radius of a sphere with the same volume. We can extract the
constants and have a tidy :math:`R = S_x\sqrt[3]V` kind of equation that
yields a radius that can be plugged into the difficulty computation,
:math:`d = 5R`.

There will be one exception, the hemisphere. It’s simpler than the
others.

Hemisphere
~~~~~~~~~~

A Hemisphere has a smaller volume for a given radius, :math:`r`. As with
a sphere, the volume is characterized by a single number, :math:`r`.

.. code:: ipython3

    hemisphere = Eq(Rational(2,3)*pi*r**3, Rational(4,3)*pi*R**3)
    hemisphere




.. math::

    \displaystyle \frac{2 \pi r^{3}}{3} = \frac{4 \pi R^{3}}{3}



We can solve for :math:`R` to find the effective radius of a sphere with
the same volume.

.. code:: ipython3

    Eq(R, solve(hemisphere, R)[0])




.. math::

    \displaystyle R = \frac{2^{\frac{2}{3}} r}{2}



We can extract the constants and compute an approximate value that’s
easier to use.

.. code:: ipython3

    cons, vars = constants(solve(hemisphere, R)[0])
    N(cons) * vars




.. math::

    \displaystyle 0.7937005259841 r



Here’s a depiction of the formula, just to show that there are only two
constant arguments, and single variable argument to the top-level
``Mul`` node.

.. code:: ipython3

    graphviz.Source(dotprint(solve(hemisphere, R)[0]))




.. image:: area_effect_computations_files/area_effect_computations_41_0.svg



Cone
~~~~

A cone’s volume is described by a height, :math:`h`, and a radius,
:math:`r`. We’ll define an equation using the cone’s parameters and the
radius, :math:`R`, of the equivalent sphere.

.. code:: ipython3

    cone = Eq(Rational(1,3)*h*pi*r**2, Rational(4,3)*pi*R**3)
    cone




.. math::

    \displaystyle \frac{\pi h r^{2}}{3} = \frac{4 \pi R^{3}}{3}



.. code:: ipython3

    Eq(R, solve(cone, R)[0])




.. math::

    \displaystyle R = \frac{\sqrt[3]{2} \sqrt[3]{h r^{2}}}{2}



We can decompose this into a constant value and a volume-related
expression. This gives us a computation for :math:`R`, from which we get
difficulty, :math:`5R`.

.. code:: ipython3

    cons, vars = constants(solve(cone, R)[0])
    N(cons) * vars




.. math::

    \displaystyle 0.629960524947437 \sqrt[3]{h r^{2}}



Here’s a depiction of the formula showing the first two arguments, which
are the constants, and the third argument, which has the variables in
it.

.. code:: ipython3

    graphviz.Source(dotprint(solve(cone, R)[0]))





.. image:: area_effect_computations_files/area_effect_computations_48_0.svg



In the *OpenD6 Magic Guide* the cone has a simplified computation of
difficulty.

::

       +5 for a basic cone two meters long and a base with
       a one-meter radius

       and +1 for each additional half meter of
       length or meter of base radius.

       Example: A cone
       that’s three meters long with a base two meters wide (radius
       of one meter) has a cost of +7.

This is :math:`2h+r`. Let’s compare.

.. code:: ipython3

    data = []
    for h_val in range(2, 7):
        for r_val in range(1, 4):
            R_val = (cons * vars).evalf(subs={"h": h_val, "r": r_val})
            D_val = R_val * 5
            d_val = 2*h_val + r_val
            if D_val-2 <= d_val < D_val+3:
                error = "close"
            else:
                error = f"{abs(D_val - d_val):.1f}"
            data.append(
                [h_val, r_val, f"{D_val:.1f}", d_val, error]
            )
    
    md = Markdown(
        tabulate(data, headers=["h","r","exact","approx","error"], tablefmt="pipe")
    )
    display(md)



= = ===== ====== =====
h r exact approx error
= = ===== ====== =====
2 1 4     5      close
2 2 6.3   6      close
2 3 8.3   7      close
3 1 4.5   7      close
3 2 7.2   8      close
3 3 9.4   9      close
4 1 5     9      4.0
4 2 7.9   10     close
4 3 10.4  11     close
5 1 5.4   11     5.6
5 2 8.5   12     3.5
5 3 11.2  13     close
6 1 5.7   13     7.3
6 2 9.1   14     4.9
6 3 11.9  15     3.1
= = ===== ====== =====


For a few values of :math:`h` and :math:`r` the :math:`2h+r` difficulty
is close to the exact difficulty based on volume. As the cone gets
longer (6m or more), the error increases.

Cuboid
~~~~~~

A Cuboid’s volume is decribed by the height, :math:`h`, width,
:math:`w`, and depth, :math:`d`. We can compute the cuboid volume, and
then solve for the equilavent sphere’s radius, :math:`R`.

.. code:: ipython3

    cuboid = Eq(h*w*d, Rational(4,3)*pi*R**3)
    cuboid




.. math::

    \displaystyle d h w = \frac{4 \pi R^{3}}{3}



.. code:: ipython3

    Eq(R, solve(cuboid, R)[0])




.. math::

    \displaystyle R = \frac{\sqrt[3]{6} \sqrt[3]{d h w}}{2 \sqrt[3]{\pi}}



.. code:: ipython3

    cons, vars = constants(solve(cuboid, R)[0])
    N(cons) * vars




.. math::

    \displaystyle 0.6203504908994 \sqrt[3]{d h w}



.. code:: ipython3

    graphviz.Source(dotprint(solve(cuboid, R)[0]))





.. image:: area_effect_computations_files/area_effect_computations_56_0.svg



Cylinder
~~~~~~~~

A Cylinder’s volume is described by the a height, :math:`h`, and a
radius, :math:`r`.

.. code:: ipython3

    cylinder = Eq(h*pi*r**2, Rational(4,3)*pi*R**3)
    cylinder




.. math::

    \displaystyle \pi h r^{2} = \frac{4 \pi R^{3}}{3}



.. code:: ipython3

    Eq(R, solve(cylinder, R)[0])




.. math::

    \displaystyle R = \frac{\sqrt[3]{6} \sqrt[3]{h r^{2}}}{2}



.. code:: ipython3

    cons, vars = constants(solve(cylinder, R)[0])
    N(cons) * vars




.. math::

    \displaystyle 0.90856029641607 \sqrt[3]{h r^{2}}



.. code:: ipython3

    graphviz.Source(dotprint(solve(cylinder, R)[0]))





.. image:: area_effect_computations_files/area_effect_computations_61_0.svg



Pyramid
~~~~~~~

A Pyramid has a height, :math:`h`, and a base width and length,
:math:`w`, :math:`l`. This is the general case of a pyramid with a base
that’s not square. As we’ll see, a square base is not a signficant
simplification.

.. code:: ipython3

    pyramid = Eq(Rational(1,3)*h*w*l, Rational(4,3)*pi*R**3)
    pyramid




.. math::

    \displaystyle \frac{h l w}{3} = \frac{4 \pi R^{3}}{3}



.. code:: ipython3

    Eq(R, solve(pyramid, R)[0])




.. math::

    \displaystyle R = \frac{\sqrt[3]{2} \sqrt[3]{h l w}}{2 \sqrt[3]{\pi}}



.. code:: ipython3

    cons, vars = constants(solve(pyramid, R)[0])
    N(cons) * vars




.. math::

    \displaystyle 0.43012700691405 \sqrt[3]{h l w}



For a square-based pyramid, :math:`l=w`. Not a very intersting
complication.

.. code:: ipython3

    graphviz.Source(dotprint(solve(pyramid, R)[0]))





.. image:: area_effect_computations_files/area_effect_computations_67_0.svg



Additional Shapes and Difficulty Computations
---------------------------------------------

We’ve got all of the necessary computations reduced to a
:math:`R = S_s\sqrt[3]V` kind of formula. We can use this to compute
difficulty, as :math:`5R`.

Let’s summarize this in a tidy table we can use when designing spells
with complicated areas of effect.

.. code:: ipython3

    from pathlib import Path
    import csv
    import re

.. code:: ipython3

    details = {
        'Hemisphere': ("radius $r$", hemisphere),
        'Cone': ("height $h$, base radius $r$", cone),
        'Cuboid': ("height $h$, width $w$, depth $d$", cuboid),
        'Cylinder': ("height $h$, radius $r$", cylinder),
        'Pyramid': ("height $h$, base width $w$, base length $l$", pyramid),
    }
    
    def rules() -> tuple[str, str, float, str, str]:
        """Yields shape name, arg text, constant, and Latex for base formula, and difficulty formula."""
        for shape, (arg, eq) in details.items():
            cons, vars = constants(solve(eq, R)[0])
            cons_r = cons.evalf(2)
            yield shape, arg, cons, latex(cons_r * vars), latex(cons_r * 5 * vars)
    
    rule_supplement_path = Path.cwd() / "area_effect_shapes.csv"
    with open(rule_supplement_path, "w") as rules_file:
        writer = csv.writer(rules_file)
        writer.writerow(["Shape", "Measures", "Equivalent Sphere R", "Difficulty"])
        rst_form = (
            [shape, re.sub(r"\$(\w+)\$", r":math:`\1`", arg), f":math:`{radius_formula}`", f":math:`{diff_formula}`"]
            for shape, arg, cons, radius_formula, diff_formula in rules()
        )
        writer.writerows(rst_form)
    print("See", rule_supplement_path)
    
    header = [
        "Shape","Measures","Equivalent Sphere R","Difficulty Weight"
    ]
    data = [
        ["Sphere", "radius $r$", "$R = r$", "$5r$"]
    ]
    
    for shape, arg, cons, radius_formula, diff_formula in rules():
        data.append(
            [shape, arg, f"$R = {radius_formula}$", f"${diff_formula}$"]
        )
    
    md = Markdown(tabulate(data, headers=header, tablefmt="pipe"))
    display(md)


.. parsed-literal::

    See /Users/slott/Documents/Hobbies/Gaming/OpenD6/opend6-tools/notebooks/area_effect_shapes.csv



+------+---------------------------+------------------+---------------+
| S    | Measures                  | Equivalent       | Difficulty    |
| hape |                           | Sphere R         | Weight        |
+======+===========================+==================+===============+
| Sp   | radius :math:`r`          | :math:`R = r`    | :math:`5r`    |
| here |                           |                  |               |
+------+---------------------------+------------------+---------------+
| He   | radius :math:`r`          | :m               | :math:`4.0 r` |
| misp |                           | ath:`R = 0.79 r` |               |
| here |                           |                  |               |
+------+---------------------------+------------------+---------------+
| Cone | height :math:`h`, base    | :m               | :ma           |
|      | radius :math:`r`          | ath:`R = 0.63 \s | th:`3.1 \sqrt |
|      |                           | qrt[3]{h r^{2}}` | [3]{h r^{2}}` |
+------+---------------------------+------------------+---------------+
| Cu   | height :math:`h`, width   | :math:`R = 0.62  | :             |
| boid | :math:`w`, depth          | \sqrt[3]{d h w}` | math:`3.1 \sq |
|      | :math:`d`                 |                  | rt[3]{d h w}` |
+------+---------------------------+------------------+---------------+
| Cyli | height :math:`h`, radius  | :m               | :ma           |
| nder | :math:`r`                 | ath:`R = 0.91 \s | th:`4.5 \sqrt |
|      |                           | qrt[3]{h r^{2}}` | [3]{h r^{2}}` |
+------+---------------------------+------------------+---------------+
| Pyr  | height :math:`h`, base    | :math:`R = 0.43  | :             |
| amid | width :math:`w`, base     | \sqrt[3]{h l w}` | math:`2.2 \sq |
|      | length :math:`l`          |                  | rt[3]{h l w}` |
+------+---------------------------+------------------+---------------+


