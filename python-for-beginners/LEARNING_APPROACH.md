# Learning Approach: Why This Course Is Built the Way It Is

This document explains every design decision in the course.
Read it once, early. It will save you weeks of frustration.

---

## Why passive learning fails

Most beginners start by watching YouTube tutorials or reading textbooks.
They follow along, nodding. Everything makes sense. Then they close the video and try
to write something themselves — and nothing comes out.

This is called the **illusion of competence**. Watching someone code feels like learning
to code, but it is closer to watching someone swim. You can understand every stroke
in detail and still sink the moment you jump in.

The brain builds programming skill through **active retrieval and production**, not
through recognition. You need to produce code from scratch, hit errors, fix them,
and feel the whole cycle. That only happens when your hands are on the keyboard.

---

## The 30/70 rule

**30% of your time** goes to reading CONCEPTS.md files, watching reference videos,
or reading these docs. This is input. It is necessary but not sufficient.

**70% of your time** goes to writing code. In practice, that looks like:

- Typing out every example file character by character (not skimming it).
- Attempting each exercise before looking at any hint.
- Modifying examples to see what breaks and what does not.
- Writing small experiments in the REPL to test your understanding.
- Coming back the next day and rewriting yesterday's exercise from memory.

If you finish reading CONCEPTS.md in 20 minutes, you should spend the next 47 minutes
writing code — not reading more.

---

## Daily schedule: 1.5 to 2 hours, 6 days/week

**Why consistency beats intensity**

The brain consolidates new skills during sleep. A skill practised for 30 minutes
before bed is literally strengthened overnight while you sleep. Six short sessions
produce more durable learning than one six-hour marathon session.

Weekend cramming sessions feel productive because you cover a lot of ground quickly,
but most of it evaporates by Monday. Daily practice keeps the material in active
memory and builds the procedural fluency that lets you code without thinking hard
about syntax.

**Recommended session structure (90 minutes)**

| Time block      | Activity                                          |
|-----------------|---------------------------------------------------|
| 0–10 min        | Review yesterday's code. Can you explain it aloud?|
| 10–30 min       | Read CONCEPTS.md for today's topic.               |
| 30–90 min       | Work through exercises. Type everything.          |

Adjust to fit your life, but protect the 70% coding time ratio.

**The sixth day off**

One rest day per week is not laziness — it is consolidation time. Your brain needs
it. Do not feel guilty. Do not code on that day.

---

## The no-copy-paste rule

Programming is a physical skill as much as a mental one. Your fingers need to know
where the colon goes at the end of a `def` line, where the parentheses go in `print()`,
and how far to indent a loop body. This is **muscle memory**, and it only builds through
repetition.

When you copy-paste code, you bypass the muscle memory loop entirely. You also bypass
the cognitive step of deciding what to type next — which is where most of the learning
happens.

**What to do when you are stuck**

1. Re-read the relevant section of CONCEPTS.md.
2. Look at the example file for that topic.
3. After 15 minutes of genuine effort, open the solution file.
4. **Read the solution. Close the file. Then retype it from memory.**

Step 4 is the key. Reading a solution and understanding it is passive. Closing it
and reproducing it from memory is active. The act of trying to remember forces your
brain to encode the pattern properly.

---

## The "run before reading" habit

Before reading any example file in full, run it first:

```bash
python modules/module01_getting_started/examples/01_hello_world.py
```

See the output. Form a question: "How did Python produce that?" Then read the code
to find out. This turns reading into an investigation rather than passive consumption.

---

## How to use exercises

Each exercise file has:
- A description of what to build.
- A difficulty marker: 🟢 easy / 🟡 medium / 🔴 hard.
- `# TODO:` markers showing the suggested steps.
- A hints section.

**The intended workflow:**

1. Read the exercise description carefully.
2. Close this document and any notes.
3. Attempt the exercise. Get it wrong. Fix it. Get it wrong again. Fix it again.
4. If you are stuck after 15 minutes of genuine effort, open the solution file, read
   it once, close it, and retype the solution from memory.
5. Once it works, try to break it intentionally — change a value, remove a line,
   add something unexpected — and see what happens.

Do not move to the next module until you can write the current module's exercises
from a blank file without help. That is the real test of understanding.
