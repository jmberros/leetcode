## Backtracking

As a reminder, backtracking is a general algorithm for finding all (or some) solutions to some computational problems. The idea is that it incrementally builds candidates to the solutions, and abandons a candidate ("backtrack") as soon as it determines that this candidate cannot lead to a final solution.

At any instant, we can only be at one of the nodes.
When we _backtrack_, we are moving from a node to its parent node.

An important detail on choosing the next number for the combination is that we select the candidates in order, where the total candidates are treated as a list.

Once a candidate is added into the current combination, we will
**not look back** to all the previous candidates in the next explorations.