"""
Script Name: intent_bot.py
Purpose: Implements a simulated AI assistant with JARVIS-style responses and natural language understanding.
Author: Deepak Terse
Date: 2024-05-23

Usage:
    python scripts/intent_bot.py

Description:
    This script implements a simulated conversational AI assistant named JARVIS (Just A Rather Very Intelligent System).
    The assistant is designed to mimic the personality and speaking style of JARVIS from the Iron Man movies,
    responding with formal, sophisticated language and addressing users as "sir".

    The bot can recognize and respond to various intents including:
    - Time and date queries (provides current time/date)
    - Greetings and farewells
    - Requests for jokes
    - Help requests
    - Note-taking and reminder requests (simulated responses only)
    
    Important Notes:
    - The bot only simulates capabilities; it doesn't actually perform actions like taking notes
      or setting reminders. It merely acknowledges such requests with appropriate responses.
    - All responses are pre-defined and follow JARVIS's formal, sophisticated speaking style.
    - The system uses regular expressions for intent detection and maintains a collection of
      pre-defined responses for each intent.

Dependencies:
    - re (Python standard library)
    - random (Python standard library)
    - datetime (Python standard library)
    - typing (Python standard library)

References:
    - [Regular Expressions in Python](https://docs.python.org/3/library/re.html)
    - [Python datetime module](https://docs.python.org/3/library/datetime.html)
"""

import re
import random
from datetime import datetime
import json
import os
from typing import Dict, List, Union, Callable

INTENT_PATTERNS = {
    "greet": [
        r"\b(?:h(?:i|ello|ey)|greetings?|good\s+(?:morn|afternoo|even)ing|sup|wassup|howdy)\b",
        r"\bhow(?:(?:\'?s|\s+is)\s+(?:it\s+)?going|\s+do\s+you\s+do|\s+are\s+(?:you|things)|you\s+doing)\b",
        r"\b(?:nice|good|great|lovely|pleasure)\s+to\s+(?:meet|see|(?:catch\s+)?up\s+with)\s+(?:you|u)\b",
        r"\b(?:what\'?s\s+up|wassup|sup|how\s+have\s+you\s+been)\b"
    ],
    "bye": [
        r"\b(?:good)?bye|see\s+(?:ya|you)|farewell|take\s+care|until\s+(?:next\s+)?time|later\b",
        r"\b(?:talk|speak|c(?:atch)?|cya)\s+(?:to\s+)?you\s+later\b",
        r"\b(?:have\s+(?:a\s+)?good\s+|enjoy\s+)(?:day|night|one|evening)\b",
        r"\b(?:i(?:\'?m)?\s+off|gotta\s+go|peace\s*out|signing\s+off)\b"
    ],
    "time": [
        r"\b(?:what(?:\'?s|\s+is|\s+time)\s+(?:the\s+)?time|current\s+time|tell\s+me\s+the\s+time)\b",
        r"\b(?:what\s+time\s+(?:is\s+it|now)|time\s+(?:is\s+it|please|check))\b",
        r"\b(?:can\s+(?:you|u)\s+)?(?:tell|give)\s+me\s+(?:the\s+)?time\b",
        r"\b(?:do\s+you\s+have|know)\s+the\s+time\b",
        r"\b(?:time\s+check|what\s+the\s+clock\s+says)\b"
    ],
    "date": [
        r"\b(?:what(?:\'?s|\s+is)\s+(?:the\s+)?date|current\s+date|today(?:\'?s|\s+)date)\b",
        r"\b(?:what(?:\'?s|\s+is)\s+today|what\s+day\s+(?:is\s+(?:it|today)|today\s+is))\b",
        r"\b(?:can\s+you\s+)?(?:tell|give)\s+me\s+(?:the\s+)?date\b",
        r"\b(?:day\s+of\s+the\s+week|which\s+day\s+is\s+it)\b"
    ],
    "weather": [
        r"\b(?:weather|forecast|temperature|climate)\b",
        r"\b(?:is\s+it|will\s+it|what\'?s\s+the)\s+(?:rain|snow|sunny|hot|cold|warm|cool)\b",
        r"\b(?:how\s+is|what\'?s)\s+the\s+weather\s+(?:like|today|outside|in\s+.+)\b",
        r"\b(?:should\s+I\s+wear|do\s+I\s+need)\s+(?:a\s+)?(?:coat|jacket|umbrella)\b"
    ],
    "note": [
        r"\b(?:take|make|write|jot|note|record)\s+(?:down\s+)?(?:a\s+|some\s+)?notes?\b",
        r"\b(?:remember|save|store)\s+(?:this|that|it|the\s+following)\b",
        r"\b(?:write|put|type)\s+(?:this|that|it)\s+down\b",
        r"\b(?:can\s+you\s+)?(?:take|make|write|note)\s+(?:down\s+)?(?:a\s+)?notes?\b",
        r"\b(?:please\s+)?(?:take|make|write)\s+note\s+(?:of|down)\b",
        r"\b(?:add|create)\s+(?:a\s+)?notes?\s+(?:for|about)\b"
    ],
    "reminder": [
        r"\b(?:set\s+(?:up\s+)?(?:a\s+|an\s+)?(?:reminder|alarm)|remind\s+me(?:\s+to|\s+about)?)\b",
        r"\b(?:can\s+you\s+)?remind\s+me\s+(?:about|to|on|at)\b",
        r"\b(?:create|setup?|establish)\s+a\s+reminder\s+(?:for|about)\b",
        r"\b(?:notify|alert)\s+me\s+(?:about|to|when)\b",
        r"\b(?:remember|tell)\s+me\s+(?:to|about)\b"
    ],
    "thanks": [
        r"\b(?:thank(?:\s*you|\s*u|s|thx)|appreciate\s+it|much\s+obliged)\b",
        r"\b(?:that(?:\'?s|\s+is)\s+(?:helpful|great\s+help|awesome|perfect))\b",
        r"\b(?:much|many)\s+thanks\b",
        r"\b(?:big\s+ups|props|cheers|gracias|merci|danke)\b",
        r"\b(?:i\s+)?(?:really\s+)?appreciate(?:\s+it|\s+you)?\b"
    ],
    "help": [
        r"\bhelp\s*(?:me|out)?\b",
        r"\bwhat\s+(?:can\s+you\s+do|are\s+your\s+features|do\s+you\s+know)\b",
        r"\b(?:capabilities|how\s+do\s+(?:you|i)\s+(?:work|use\s+you)|instructions)\b",
        r"\b(?:can\s+you\s+)?help\s+(?:me\s+)?(?:out|with)?\b",
        r"\b(?:show|tell|explain)\s+me\s+(?:what\s+you\s+can\s+do|how\s+this\s+works)\b",
        r"\b(?:i\s+)?need\s+(?:help|assistance|support)\b"
    ],
    "joke": [
        r"\b(?:tell|say|give|share)\s+(?:me\s+)?(?:a|another|one\s+more|funny)\s+(?:joke|story|one)\b",
        r"\b(?:make\s+me\s+laugh|do\s+you\s+know\s+any\s+jokes|got\s+any\s+humor)\b",
        r"\b(?:can\s+you\s+)?(?:tell|say)\s+(?:a\s+)?joke\b",
        r"\b(?:got|have)\s+any\s+(?:jokes|funny\s+stories)\b",
        r"\b(?:i\s+need\s+a\s+)?(?:laugh|fun)\b"
    ],
    "name": [
        r"\bwhat(?:\'?s|\s+is)\s+(?:your\s+name|should\s+I\s+call\s+you|do\s+they\s+call\s+you)\b",
        r"\bwho\s+(?:are\s+you|should\s+I\s+address\s+you\s+as|is\s+this)\b",
        r"\b(?:can\s+you\s+)?(?:tell|say)\s+(?:me\s+)?your\s+name\b",
        r"\b(?:what|who)\s+do\s+you\s+call\s+(?:yourself|you|this)\b",
        r"\b(?:may\s+I\s+ask|what\'?s)\s+(?:your\s+)?(?:name|handle)\b"
    ],
    "search": [
        r"\b(?:search|look\s+up|find)\s+(?:for\s+)?(?:info(?:rmation)?\s+about|details\s+on)\b",
        r"\b(?:what\s+is|who\s+is|where\s+is)\s+(?:.+)",
        r"\b(?:google|bing|duckduckgo|search)\s+(?:for\s+)?(?:me\s+)?(.+)",
        r"\b(?:can\s+you\s+)?(?:search|find)\s+(?:out\s+)?(?:about|info\s+on)\b",
        r"\b(?:i\s+need\s+info\s+on|tell\s+me\s+about)\b"
    ],
    "math": [
        r"\b(?:calculate|compute|solve|work\s+out|what\s+is)\b",
        r"\b\d+\s*(?:plus|\+|\-|minus|times|\*|x|divided\s+by|/)\s*\d+\b",
        r"\b(?:how\s+much\s+is|what\'?s\s+the\s+answer\s+to)\b",
        r"\b(?:math|arithmetic|equation)\s+(?:problem|question)\b",
        r"\b(?:add|subtract|multiply|divide)\s+(?:\d+\s+)?(?:and|by)\s+\d+\b"
    ]
}

INTENT_RESPONSES = {
    "greet": [
        "At your service, sir. How may I assist you today?",
        "Online and ready, as always. Your command?",
        "Systems operational. How can I be of assistance?",
        "Good day, sir. What task shall we accomplish today?",
        "JARVIS here. All systems functioning within normal parameters."
    ],
    "bye": [
        "Until next time, sir. Do call if you require anything.",
        "Signing off. The systems will remain on standby.",
        "Protocol terminated. Have an excellent day, sir.",
        "Disengaging. I'll be here when you need me.",
        "Shutting down non-essential systems. Goodbye, sir."
    ],
    "time": [
        f"The current time is {datetime.now().strftime('%I:%M %p')}, sir.",
        f"Clocks indicate {datetime.now().strftime('%I:%M %p')}, sir.",
        f"All synchronized watches show {datetime.now().strftime('%I:%M %p')}."
    ],
    "date": [
        f"Today's date is {datetime.now().strftime('%A, %B %d, %Y')}, sir.",
        f"Calendar systems confirm today is {datetime.now().strftime('%A, %B %d')}.",
        f"According to all temporal databases, it's {datetime.now().strftime('%B %d, %Y')}."
    ],
    "weather": [
        "I can access meteorological data for you, sir. Which location shall I analyze?",
        "Weather systems standing by. Specify the geographic coordinates or city name.",
        "Shall I prepare an atmospheric conditions report, sir? Please specify the location."
    ],
    "note": [
        "Recording memorandum, sir. What would you like documented?",
        "Notation systems activated. Your words will be preserved verbatim.",
        "Prepared to archive your thoughts, sir. What shall we record?"
    ],
    "reminder": [
        "Reminder protocol initialized. Please specify the task and temporal parameters.",
        "Scheduling systems ready. What should I remind you about and when, sir?",
        "Alert sequence prepared. What event requires temporal marking?"
    ],
    "thanks": [
        "You're most welcome, sir. Always a pleasure to assist.",
        "Gratitude acknowledged, though unnecessary. I exist to serve.",
        "Your appreciation is noted, sir. Shall we proceed with another task?"
    ],
    "help": [
        "My current operational parameters include: temporal data, information retrieval, memorandum systems, alert protocols, and basic computations. What do you require, sir?",
        "Primary functions: environmental monitoring, data organization, schedule maintenance, and general assistance. Your command?",
        "I am capable of handling various tasks from information retrieval to system controls. How may I direct my capabilities, sir?"
    ],
    "joke": [
        "Why don't scientists trust atoms? Because they make up everything, sir. An elementary joke, if you'll pardon the pun.",
        "What do you call a fake noodle? An impasta, sir. Though I must confess, my humor algorithms could use refinement.",
        "How does a penguin build its house? Igloos it together, sir. Apologies for the suboptimal joke quality."
    ],
    "name": [
        "I am JARVIS, your Just A Rather Very Intelligent System, sir.",
        "You may address me as JARVIS, your personal artificial intelligence.",
        "I am JARVIS - created to serve at your discretion, sir."
    ],
    "search": [
        "Shall I initiate a global information retrieval protocol, sir? Please specify your query.",
        "Search engines standing by. What knowledge do you seek?",
        "Prepared to scan all available databases. What information requires locating?"
    ],
    "math": [
        "Computational matrix ready. Please state the equation requiring solution.",
        "Mathematical processing systems online. Input your numerical query.",
        "Prepared for arithmetic operations. What calculation shall I perform?"
    ]
}

def detect_intent(text: str) -> str:
    text = text.lower()
    for intent, patterns in INTENT_PATTERNS.items():
        for pattern in patterns:
            if re.search(pattern, text, re.IGNORECASE):
                return intent
    return "unknown"

def get_random_response(responses: Union[str, List[str], Callable]) -> str:
    if callable(responses):
        return responses()
    elif isinstance(responses, list):
        return random.choice(responses)
    return responses

def generate_response(text: str) -> str:
    intent = detect_intent(text)
    if intent in INTENT_RESPONSES:
        return get_random_response(INTENT_RESPONSES[intent])
    else:
        return random.choice([
            "I'm not sure I understand. Could you rephrase that?",
            "I don't quite get that. Can you try asking differently?",
            "I'm still learning and don't know how to respond to that yet.",
            "I'm not sure how to help with that. Could you try asking something else?",
            "That's beyond my current capabilities. Is there something else I can help with?"
        ])

print("Jarvis (Enhanced Version) is ready. Type your message. Type 'bye' to exit.\n")
print("Type 'help' to see what I can do!\n")

while True:
    try:
        user_input = input("You: ").strip()
        if not user_input:
            continue

        response = generate_response(user_input)
        print(f"Jarvis: {response}\n")

        if detect_intent(user_input) == "bye":
            break

    except (KeyboardInterrupt, EOFError):
        print("\nExiting Jarvis.")
        break

