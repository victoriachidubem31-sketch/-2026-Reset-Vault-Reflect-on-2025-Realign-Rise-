# 🌠 2026 Reset Vault – Reflect on 2025, Realign & Rise
# A Python tool to reflect on 2025, plan for 2026, and step into the new year with clarity, calm, and intention.

import random

print("🌠 Welcome to the 2026 Reset Vault 🌠")
print("Reflect on 2025. Realign. Rise into 2026.\n")

# ---------------- Calm & Mental Check ----------------
print("🧘 Mental State Check-In")
calm_score = int(input("On a scale of 1 to 5, how would you rate your current mental state? "))

# Determine feedback based on user choice
if calm_score == 1:
    mood_message = "Your mental state seems very low. 2026 will be about rest and rebuilding."
elif calm_score == 2:
    mood_message = "Your mental state is a bit drained. Focus on self-care and recovery in 2026."
elif calm_score == 3:
    mood_message = "You managed to survive a demanding year. Balance will be your power."
elif calm_score == 4:
    mood_message = "You adapted well. Keep up the calm and consistency into 2026."
elif calm_score == 5:
    mood_message = "You are very calm and balanced. You’re ready to thrive in 2026!"
else:
    mood_message = "Invalid input. We'll consider your state neutral."

# Show the feedback clearly and pause
print("\n" + mood_message + "\n")
input("Press Enter to continue to 2025 Reality Reflection...")

# ---------------- 2025 Reality Reflection (Multiple Choice) ----------------
print("\n🌍 2025 Reality Reflection")
print("In 2025, many people faced several common experiences. Pick the one that affected you the most:")
print("1. Rapid technology changes")
print("2. Academic and career pressure")
print("3. Digital overload and comparison")
print("4. Personal growth challenges")
print("5. Other / Unique experience")

# Get user choice and convert to description
while True:
    try:
        choice = int(input("Enter the number corresponding to your experience (1-5): "))
        if choice == 1:
            relate = "Rapid technology changes"
        elif choice == 2:
            relate = "Academic and career pressure"
        elif choice == 3:
            relate = "Digital overload and comparison"
        elif choice == 4:
            relate = "Personal growth challenges"
        elif choice == 5:
            relate = input("Please briefly describe your unique experience: ")
        else:
            print("Please enter a valid number between 1 and 5.")
            continue
        break
    except ValueError:
        print("Please enter a valid number between 1 and 5.")

print(f"\nYou selected: {relate}\n")

# ---------------- Personal Wins ----------------
print("🏆 Your 2025 Wins")
win1 = input("One achievement you are proud of in 2025: ")
win2 = input("One moment you proved strength or consistency: ")

# ---------------- Challenges Audit ----------------
print("\n⚠️ 2025 Challenges Audit")
challenge1 = input("One challenge that slowed you down: ")
challenge2 = input("One habit or situation that didn’t serve you: ")

# ---------------- 2025 Habit Audit ----------------
print("\n🔍 2025 Habit Audit")
print("Let’s look honestly at your habits from 2025.\n")

bad_habit = input("One habit or behavior in 2025 that slowed you down: ")
bad_reason = input("Why do you think this habit existed? ")
bad_change = input("One realistic way you can reduce or change this habit in 2026: ")

print()

good_habit = input("One habit or behavior in 2025 that helped you grow: ")
good_reason = input("Why did this habit work well for you? ")
good_improve = input("One way you can improve or strengthen this habit in 2026: ")

# ---------------- Carry, Drop, Transform ----------------
print("\n🔄 Carry • Drop • Transform")
carry = input("One thing you want to carry into 2026: ")
drop = input("One thing you want to drop after 2025: ")
transform = input("One thing you want to transform or improve: ")

# ---------------- Focus Word ----------------
print("\n✨ 2026 Focus Word")
focus_word = input("Choose ONE word to define your 2026 (e.g., Focus, Peace, Discipline): ")

# ---------------- Identity Statement ----------------
print("\n🪞 2026 Identity Statement")
identity = input("Complete this sentence: In 2026, I am someone who... ")

# ---------------- Goal Planning ----------------
print("\n🎯 2026 Priority Goal")
main_goal = input("Your MAIN goal for 2026: ")
first_step = input("One small step you will take in January: ")

# ---------------- Weekly Reset Ritual ----------------
print("\n📅 Weekly Reset Ritual")
weekly_reset = input("One simple thing you’ll do weekly to stay balanced: ")

# ---------------- Affirmations ----------------
affirmations = [
    "You adapted in 2025 — you will thrive in 2026.",
    "Slow growth is still real growth.",
    "You don’t need to compete. You need to continue.",
    "The lessons of 2025 are the strength of 2026.",
    "Clarity comes from consistency, not pressure."
]

daily_affirmation = random.choice(affirmations)

# ---------------- Final Summary ----------------
print("\n🌟 YOUR 2026 RESET VAULT SUMMARY 🌟\n")

print(f"🧠 Mental score: {calm_score}/5")
print(f"🌍 2025 challenge you related to: {relate}")
print(f"✨ Focus word for 2026: {focus_word}\n")

print("🏆 2025 Highlights:")
print(f"- Achievement: {win1}")
print(f"- Strength moment: {win2}\n")

print("⚠️ Challenges to learn from:")
print(f"- {challenge1}")
print(f"- {challenge2}\n")

print("🔍 Habit Reflection:")
print(f"- Habit that slowed you down: {bad_habit}")
print(f"  Why it existed: {bad_reason}")
print(f"  How you’ll change it: {bad_change}\n")

print(f"- Habit that helped you: {good_habit}")
print(f"  Why it worked: {good_reason}")
print(f"  How you’ll improve it: {good_improve}\n")

print("🔄 Transition Plan:")
print(f"- Carry forward: {carry}")
print(f"- Drop behind: {drop}")
print(f"- Transform: {transform}\n")

print("🚀 2026 Direction:")
print(f"- Identity: {identity}")
print(f"- Priority goal: {main_goal}")
print(f"- January step: {first_step}")
print(f"- Weekly reset ritual: {weekly_reset}\n")

print("💖 Affirmation for You:")
print(f"“{daily_affirmation}”\n")

print("🔐 Final Note:")
print("2025 shaped you — it does not define your limits.")
print(f"Let '{focus_word}' guide you calmly into 2026.")
print("Welcome to your reset. You are ready 🌱✨")
