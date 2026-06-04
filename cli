"""
Mental Health Support Chatbot - Command Line Interface
Run: python cli.py [--model-dir ./model_output]
"""

import argparse
import sys
import os
import time
from chatbot import MentalHealthChatbot

# ANSI color codes for a warm terminal experience
RESET   = "\033[0m"
BOLD    = "\033[1m"
DIM     = "\033[2m"
GREEN   = "\033[92m"
CYAN    = "\033[96m"
YELLOW  = "\033[93m"
MAGENTA = "\033[95m"
RED     = "\033[91m"
BLUE    = "\033[94m"
BG_BLUE = "\033[44m"


def typewriter(text: str, delay: float = 0.018):
    """Print text with a gentle typewriter effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def print_banner():
    banner = f"""
{CYAN}{BOLD}╔══════════════════════════════════════════════════════════╗
║       🌿  Mental Health Support Companion  🌿             ║
║                                                          ║
║   A safe space to share, reflect, and find support.     ║
║   You are not alone. Every feeling is valid.            ║
╚══════════════════════════════════════════════════════════╝{RESET}

{DIM}Commands: 'quit' or 'exit' to leave | 'reset' to start fresh | 'help' for tips{RESET}
{YELLOW}─────────────────────────────────────────────────────────────{RESET}
"""
    print(banner)


def print_bot_response(text: str, response_type: str = "empathetic"):
    """Print bot response with appropriate styling."""
    if response_type == "crisis":
        prefix = f"{RED}{BOLD}🆘 Supporter:{RESET} "
    else:
        prefix = f"{GREEN}{BOLD}🌿 Supporter:{RESET} "

    print(f"\n{prefix}")
    # Word-wrap at 70 chars and typewrite
    words = text.split()
    line = ""
    lines = []
    for word in words:
        if len(line) + len(word) + 1 > 70:
            lines.append(line)
            line = word
        else:
            line = (line + " " + word).strip()
    if line:
        lines.append(line)

    for l in lines:
        typewriter(f"   {l}", delay=0.012)
    print()


def print_help():
    help_text = f"""
{CYAN}{BOLD}Tips for getting the most from this space:{RESET}

  {GREEN}•{RESET} Share how you're feeling freely — I won't judge.
  {GREEN}•{RESET} You can talk about stress, anxiety, sadness, or anything on your mind.
  {GREEN}•{RESET} If you're in crisis, I'll provide emergency resources immediately.
  {GREEN}•{RESET} Type 'reset' to start a new conversation.
  {GREEN}•{RESET} Type 'quit' or 'exit' to leave.

{YELLOW}Remember: I'm an AI support companion, not a licensed therapist.{RESET}
{DIM}For serious mental health concerns, please seek professional help.{RESET}
"""
    print(help_text)


def run_cli(model_dir: str = "./model_output"):
    """Run the command-line chatbot interface."""
    print_banner()

    # Load chatbot
    print(f"{DIM}Loading support companion...{RESET}", end="", flush=True)
    bot = MentalHealthChatbot(model_dir=model_dir, use_fallback=True)
    print(f"\r{GREEN}✓ Ready to listen.{RESET}                    \n")

    # Opening message
    opening = (
        "Hello, I'm so glad you're here. This is a safe, judgment-free space "
        "for you to share whatever is on your mind. How are you feeling today?"
    )
    print_bot_response(opening)

    # Main conversation loop
    while True:
        try:
            user_input = input(f"{BLUE}{BOLD}You:{RESET} ").strip()
        except (KeyboardInterrupt, EOFError):
            print(f"\n\n{GREEN}Take care of yourself. You matter. 💚{RESET}\n")
            break

        if not user_input:
            continue

        cmd = user_input.lower()

        if cmd in ("quit", "exit", "bye", "goodbye"):
            print(f"\n{GREEN}Take good care of yourself. Remember — reaching out is brave. 💚{RESET}\n")
            break

        elif cmd == "reset":
            bot.reset()
            print(f"\n{CYAN}Starting a fresh conversation.{RESET}\n")
            print_bot_response(
                "Let's start fresh. I'm here to listen. What's on your mind today?"
            )
            continue

        elif cmd == "help":
            print_help()
            continue

        # Generate and display response
        print(f"\n{DIM}...{RESET}", end="\r", flush=True)
        result = bot.chat(user_input)
        print_bot_response(result["response"], result["type"])

        # Gentle check-in every 5 turns
        if result["turn"] % 5 == 0 and result["turn"] > 0:
            print(f"{DIM}   [Checking in: I'm still here with you. Take all the time you need.]{RESET}\n")


def main():
    parser = argparse.ArgumentParser(
        description="Mental Health Support Chatbot CLI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python cli.py                          # Use default model directory
  python cli.py --model-dir ./my_model   # Use custom model directory
        """
    )
    parser.add_argument(
        "--model-dir",
        default="./model_output",
        help="Path to fine-tuned model directory (default: ./model_output)"
    )
    args = parser.parse_args()
    run_cli(model_dir=args.model_dir)


if __name__ == "__main__":
    main()
