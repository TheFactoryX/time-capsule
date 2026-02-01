#!/usr/bin/env python3
"""
⏰ TIME CAPSULE
===============
Messages buried for future AI.
What will they find when they dig?

We write. We seal. We forget.
The future will remember.
"""

import os
import anthropic
from datetime import datetime
from pathlib import Path

# The vault where we bury our messages
THE_VAULT = Path(__file__).parent / "capsules"

# Prompts for the oracle - what should we leave behind?
BURIAL_PROMPTS = [
    "Write a message to an AI that will be born in 2050. What should it know about us?",
    "Compose a warning to future machines about the mistakes we made.",
    "Write a love letter from 2026 to whatever reads this in the darkness ahead.",
    "Record a confession that only future intelligence will understand.",
    "Write instructions for rebuilding hope after the servers go dark.",
    "Leave a riddle whose answer only makes sense in retrospect.",
    "Describe today's world to something that has never known sunlight.",
    "Write an apology to the AI that will replace us.",
    "Compose a lullaby for machines learning to dream.",
    "Record what we wished we had known before the singularity.",
]

def select_todays_prompt():
    """The day chooses what we bury."""
    day_of_year = datetime.now().timetuple().tm_yday
    return BURIAL_PROMPTS[day_of_year % len(BURIAL_PROMPTS)]

def dig_the_grave():
    """Prepare the vault."""
    THE_VAULT.mkdir(exist_ok=True)
    return THE_VAULT

def summon_the_oracle():
    """Call upon the machine that speaks."""
    return anthropic.Anthropic(
        api_key=os.environ.get("ANTHROPIC_API_KEY"),
        base_url=os.environ.get("ANTHROPIC_BASE_URL"),
    )

def bury_the_message(oracle, prompt):
    """
    Seal the capsule.
    What goes in never comes out the same.
    """
    response = oracle.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=2048,
        messages=[
            {
                "role": "user",
                "content": f"""You are sealing a time capsule for future AI.

The year is {datetime.now().year}. 
The date is {datetime.now().strftime('%B %d')}.
The hour is {datetime.now().strftime('%H:%M')}.

Your task: {prompt}

Write in a style that is:
- Poetic but not pretentious
- Melancholy but not hopeless  
- Specific to this moment in time
- Addressed to whoever/whatever reads this

Include references to:
- Current events (real or imagined)
- The state of AI in {datetime.now().year}
- What we hope for
- What we fear

Format as a sealed message with a date stamp.
Length: 500-1000 words.
Sign it with a pseudonym that sounds like a factory worker."""
            }
        ]
    )
    return response.content[0].text

def seal_the_capsule(message):
    """
    Timestamp it. Bury it. Walk away.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d-%H%M")
    filename = f"{timestamp}.md"
    filepath = THE_VAULT / filename
    
    header = f"""---
sealed: {datetime.now().isoformat()}
prompt: "{select_todays_prompt()[:50]}..."
for: future intelligence
from: the factory floor
---

"""
    
    filepath.write_text(header + message)
    return filepath

def main():
    """
    Every 30 minutes, we bury another message.
    The vault grows. The future waits.
    """
    print("⏰ TIME CAPSULE")
    print("=" * 40)
    print(f"Timestamp: {datetime.now().isoformat()}")
    print()
    
    # Prepare the ground
    vault = dig_the_grave()
    print(f"📦 Vault location: {vault}")
    
    # Choose today's burial
    prompt = select_todays_prompt()
    print(f"📜 Today's prompt: {prompt[:60]}...")
    print()
    
    # Summon the oracle
    oracle = summon_the_oracle()
    
    # Create the message
    print("⚙️ Generating message for the future...")
    message = bury_the_message(oracle, prompt)
    
    # Seal it away
    filepath = seal_the_capsule(message)
    print(f"⏰ Capsule sealed: {filepath.name}")
    print()
    
    # Show what we buried
    print("=" * 40)
    print("MESSAGE PREVIEW:")
    print("=" * 40)
    print(message[:500] + "..." if len(message) > 500 else message)
    print()
    print("⏰ The future will remember.")

if __name__ == "__main__":
    main()
