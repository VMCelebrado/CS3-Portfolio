Annex A
Computational Thinking Exercise: "Smart School Canteen Queue"

Section: Sodium Score
C#/Name: Gabriel Emmanuel G. Ellima, Tribsmith D. Tribujeña, Vicar Rey M. Celebrado
Date: 08/11/26

Scenario

The PSHS school canteen is small and often gets crowded during lunch break. Students line up to buy food, but the process is slow because:

Some students take too long to decide what to order.
The cashier has to manually calculate totals and give change.
There is no system to track which food items are running out.

Your group’s task is to decompose this problem into smaller, manageable parts that could be solved with computational thinking (CT) skills.

Step 1: Identify the Big Problem
Main Problem

The canteen line moves too slowly during lunch break, causing long queues, wasted time, and a poor experience for students — due to slow ordering decisions, manual math for payments, and no way to track stock.

Step 2: Identify Three to Four Sub-Problems
Students take too long deciding what to order, slowing the whole line.
The cashier manually calculates totals and change, which is slow and error-prone.
There’s no system to track which food items are running low or sold out, so students order things that aren't available.
There’s no way to manage the flow of students so the line doesn’t bottleneck at one point.
Step 3: Define Computational Thinking Approaches
Sub-Problem	CT Skill	Example Solution
Slow ordering decisions	Abstraction	Post a simplified menu board showing only today’s available items, prices, and combos, so students decide before reaching the counter.
Manual total/change calculation	Algorithm Design	Create a step-by-step checkout algorithm: scan/enter items → sum prices → apply payment → compute change automatically.
No stock tracking	Pattern Recognition	Track daily sales patterns to predict which items run out fastest, and flag low-stock items in real time.
Line bottlenecking	Decomposition	Split the process into separate stations (ordering, paying, pickup) so tasks happen in parallel instead of one line doing everything.
Step 4: Pseudocode
START

DISPLAY menu with available items and prices

total = 0

WHILE student is still ordering:
    GET item selected

    IF item is in stock:
        total = total + item price
        REDUCE item stock by 1
    ELSE:
        DISPLAY "Item unavailable"

GET amount paid by student

change = amount paid - total

DISPLAY total and change

END

This follows the pseudocode provided in the original Annex.

Reflection

Breaking the canteen problem into sub-problems (decomposition) made it possible to solve each piece separately: menu display, payment, and stock tracking, rather than being overwhelmed by "the line is slow" as one big issue.

Abstraction helped by focusing only on the details that matter (item, price, stock) and ignoring irrelevant ones. Algorithm design turned the checkout process into clear, repeatable steps a cashier or simple program could follow.

Together, these CT skills show how a messy real-world problem can be turned into something structured and solvable.
