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

cabinet/
│
├── backend/
│   │
|   ├── main.py _(main file)_
|   ├── config.py _(storing constants and settings)_
|   ├── council.py _(sending prompts to multiple roles and recieve responses)_
|   ├── review.py _(models recieve resposnes and are graded)_
|   ├── chairman.py _(recieves the responses and rankings to give verdict)_
|   ├── prompts.py _(contains the prompts to be given to each model)_
|   ├── models.py _(contains data sturctures fo r the system)_
|   └── utils.py _(helper functions)_
│
├── frontend/ _(to be ignored during the first phase)_
│   ├── app.jsx
│   └── api.js
│
├── data/
│
└── README.md





