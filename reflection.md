# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
    The first time I ran the game, I was excited to guess the number. Inputting my guess was easy to do, however, once I started putting my guesses, I started noticing the bugs right away as the hints given were not accurate. 

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  1. The hints was not accurate (was saying lower when in reality number was higher (inversed))

  2. No way to start new round without refreshing the page (once game is done, screen is frozen)

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.
1. The code is written in lexicographic form rather than numerical. 

Hence why when I put in the number 60. It labeled the comparison 60 > 100 as TRUE because in string comparison, the character: “6” > “1” 

2. After correctly guessing the number, the game does not provide a way to start a new round. The user must manually refresh the page to continue playing.

3. The score changes inconsistently after guesses. Sometimes it goes from -10 to -5, and sometimes it does not update at all.


| Input Used | Expected Behavior | Actual Behavior | Console Error / Output |
|------------|------------------|-----------------|
| Guess of 55, then 60 (secret number was 100) | Both guesses should indicate the number is higher because 100 is greater than both guesses. | 55 returned "Go Higher" but 60 returned "Go Lower," even though the answer was 100. | None |
------------|------------------|-----------------|
| Correctly guessed the secret number | Game should allow the user to start a new round without refreshing the page. | After winning, the game could not be played again until the browser page was refreshed. | None |
------------|------------------|-----------------|
| Multiple guesses during a game | Score should update consistently according to the scoring rules. | Score changed unexpectedly (for example, from -10 to -5) or sometimes did not update after a guess. | None |

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

  For this, I utilized the VS Code Chat feature. I gave it the bugs I discovered and attatched the files I wanted it to read. From there I went one bug at a time. 

  For example, first I wanted to address the "page refresh bug". So I put in the chat the problem alongside the files, and then had it show exactly where the bug occured. Then, I put in the #FIX ME Comment in order to organize the code, but also have it display for future chat reference. 

  Then I went ahead and did the same with the other bugs I identified. I also utizlied Chat GBT when I needed help with running the app again (giving me what to write in terminal).

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
AI successfully identified that the value, "secret" in the code was a string and performed lexiographic comparison rather than numeric. I verified this was right as based on the output I was getting from hints when playing the game, it made sense to why the hints would say "guess higher" even though in reality the result was lower. This was because it was displaying in ASCII form. 

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  At first when I talked about the bug being in the String format rather than numerical, the result did not update in the app. 

  Then from there, when I tried the game, the same mistake occured where the hint was inaccurate to the guess. So I made sure to prompt better when it came to chat. By walking through the user journey. 

  Example: If user enters a value > secret. Output should give "hint: number is lower"

  else : if user enters value < secret. Output should give "hint: number is higher" 

  -- once I did this, the code updated and when I launched the game again, the change was working great !
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

  I decided if the bug was really fixed by trying the game myself. From a user perspective, seeing if the problem was still there from the first attempt. 

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

  What I ran manually was guessing the numbers in the games. I had to see exactly where the problem was occuring before being able to identify that there was a bug. From there, I was able to see that there was a error in the way the code was inputted causing the hints to be inaccurate (due to string & integer mixed)

- Did AI help you design or understand any tests? How?
Yes, AI helped me design the code. Although I was able to identify the bugs pretty quick, AI was able to quickly identify exactly where in the code it was occuring and how to fix it. 

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.

  One habit I want to reuse in future labs is putting in the work to use my brain to identify the user problem. I did this through testing myself the game. Because of this I was able to identify the bottleneck. Then I used AI as a tool rather than my only way of solving the problem, to help guide me to a quicker solution. 

- What is one thing you would do differently next time you work with AI on a coding task?
  Next time I would spend more time asking the AI to explain the code before asking for fixes. I found that understanding the logic first helped me identify the real cause of bugs, such as the hint system comparing values lexicographically instead of numerically. Once I understood the problem, it was easier to evaluate whether the AI's suggested fixes actually made sense.

- In one or two sentences, describe how this project changed the way you think about AI generated code.
The project taught me that AI is a useful tool for explaining and debugging code but its suggestions still need to be verified. Testing and understanding the logic behind the code are just as important as using AI to generate solutions.

