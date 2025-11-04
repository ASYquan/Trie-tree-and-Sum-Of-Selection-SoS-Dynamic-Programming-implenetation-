# Tries and Subset Sum (SOS): A Curious Exploration

I built this small project out of curiosity after learning about the underlying concepts in school. It combines two elegant ideas from algorithms: prefix trees (tries) and dynamic programming for the “sum of selections” (a subset-sum style problem). The goal was to understand the mechanics deeply, write clean implementations, and have a compact playground to experiment with.

## Why this is interesting

- Tries make prefix operations fast and deterministic. They show up in autocomplete, spell-check, routing tables, and anywhere lexicographic structure matters. Implementing one from scratch clarifies how nodes, child maps, and end-of-word flags cooperate to represent a set of strings.
- Subset sum with dynamic programming is a classic problem that teaches how to formalize state, define transitions, and explore two complementary strategies: bottom-up tabulation and top-down memoization. It’s a great way to internalize the trade-offs between precomputation and on-demand computation.

## What’s included

- Exercise 1 — Trie (Prefix Tree)
  - Uncompressed trie for lowercase words.
  - `insert(word)`: adds a word; inserting duplicates doesn’t change the structure.
  - `lookUp(word)`: checks if the exact word exists in the trie.
  - `printTree()`: deterministic, alphabetical string representation of the trie’s prefix structure.
  - Example combined representation:
    ```
    ((al(gorithm)(l))(inter(n(ally)(et))(view))(w(eb)(orld)))
    ```

- Exercise 2 — Sum of Selections (SOS) via Dynamic Programming
  - Bottom-up approach:
    - Builds a boolean table indicating which sums are achievable from prefixes of the sequence.
    - Returns one valid subset achieving target $K$, or `null` if none exists.
  - Top-down approach:
    - Memoized recursion that computes only the states needed for the requested $K$.
    - Supports repeated queries by reusing memoized results.

## How it works (brief)

- Trie
  - Each node stores a map from character → child and a boolean “end-of-word” flag.
  - Printing is a pre-order traversal that emits nested parenthesized substrings in alphabetical order.

- SOS Dynamic Programming
  - State: whether a sum $s$ is achievable using the first $i$ elements.
  - Bottom-up recurrence:
    ```math
    \text{DP}[i][s] =
      \begin{cases}
        \text{true} & \text{if } \text{DP}[i-1][s] \\
        \text{true} & \text{if } s \ge t_i \text{ and } \text{DP}[i-1][s - t_i] \\
        \text{false} & \text{otherwise}
      \end{cases}
    ```
  - Top-down (memoized) view:
    ```math
    \text{can}(i, s) =
      \begin{cases}
        \text{true} & \text{if } s = 0 \\
        \text{false} & \text{if } i = 0 \text{ and } s \ne 0 \\
        \text{can}(i-1, s) \lor \text{can}(i-1, s - t_i) & \text{if } s \ge t_i
      \end{cases}
    ```
    Only computed states are stored; unknowns remain `null` until visited.

## What I learned

- Translating problem statements into minimal, composable data structures and clear invariants (tries).
- Defining DP states and transitions that match the problem constraints and lead to efficient, correct solutions.
- The practical differences between bottom-up tabulation (fast for many queries, higher memory) and top-down memoization (focused computation, great for single queries or sparse exploration).

## Using the code

- Trie: create the trie, insert words, call `lookUp`, then `printTree` to inspect the structure.
- SOS:
  - Bottom-up class precomputes a table for the whole sequence and can answer multiple $K$ values quickly.
  - Top-down class initializes borders and answers a specific $K$ by exploring only the needed states.

If you’d like, I can add minimal code samples and a quick-start guide tailored to your preferred language (Python, Java, etc.).
