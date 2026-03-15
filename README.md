hello 

# LLM council project
_(contents are suseptible to changes as per the need)_

## Overview

The intial stages is of the project is intended to create a basic workflow to create a small functioning centered workbase before continuing . The starter flow would look something like - 

User Prompt
   │
   ▼
API Request
   │
   ▼
Council Models Generate Responses
   │
   ▼
Peer Review Ranking
   │
   ▼
Final Response Sythesis
   │
   ▼
Final Output(Frontend UI)

## Minimum Version

This is the minimum version and functionalities to be included to call his a working space . These would include the below -
1. User Prompt
2. Models _(in our case instances of same model with diffrent roles)_
3. Chairman _(the final model to review the peeer grades and relay th e final verdict/response)_

Initially no frontend is required as this is only the testing and prototyping phase ot make sure that we are on the correct path and have something to work with.

## Project Structure

```
cabinet/
│
├── backend/
│   ├── main.py        (main file)
│   ├── config.py      (stores constants and settings)
│   ├── council.py     (sends prompts to multiple roles and receives responses)
│   ├── review.py      (models receive responses and rank/grade them)
│   ├── chairman.py    (receives responses and rankings to produce final verdict)
│   ├── prompts.py     (contains prompt templates for each model)
│   ├── models.py      (data structures used across the system)
│   └── utils.py       (helper functions)
│
├── frontend/          (ignored during phase 1)
│   ├── app.jsx
│   └── api.js
│
├── data/              (stores runtime conversation data)
│
└── README.md
```




