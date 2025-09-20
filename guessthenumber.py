import random
import sys
import time
import threading
import tkinter as tk

# ---------- Guessing game setup ----------
target = random.randint(1, 10)
attempts = 0

# ---------- Popup sequence (fake "hack" alerts) ----------
def show_fake_hack_popups(messages, show_time_ms=1200, gap_ms=300):
    """
    Shows a sequence of topmost popup windows (Toplevel) each auto-closing after show_time_ms.
    messages: list of strings to display.
    show_time_ms: how long each popup stays visible (milliseconds).
    gap_ms: delay between popups (milliseconds).
    """
    # Create a separate tkinter root for the popups, run in same thread but keep UI responsive
    root = tk.Tk()
    root.withdraw()  # hide main root window

    popups = []

    def make_popup(text, x_offset=0, y_offset=0):
        win = tk.Toplevel(root)
        win.title("Security Alert")
        win.attributes("-topmost", True)
        # remove resize and normal window decorations lightly: keep title so it looks like real alert
        win.resizable(False, False)

        # style: red-ish label for drama
        label = tk.Label(win, text=text, justify="left", padx=12, pady=8, font=("Segoe UI", 10, "bold"))
        label.pack()

        # position near center-ish, offset so multiple windows don't fully overlap
        win.update_idletasks()
        w = win.winfo_width()
        h = win.winfo_height()
        screen_w = win.winfo_screenwidth()
        screen_h = win.winfo_screenheight()
        x = screen_w//2 - w//2 + x_offset
        y = screen_h//2 - h//2 + y_offset
        win.geometry(f"+{x}+{y}")

        return win

    # schedule popups sequentially using after
    total_delay = 0
    offsets = [(0,0), (40,40), (-60,50), (80,-40), (-100,-80)]  # visual scattering
    for idx, msg in enumerate(messages):
        def schedule_make(m=msg, off=offsets[idx % len(offsets)]):
            win = make_popup(m, x_offset=off[0], y_offset=off[1])
            popups.append(win)
            # auto-close this popup after show_time_ms
            root.after(show_time_ms, win.destroy)

        root.after(total_delay, schedule_make)
        total_delay += show_time_ms + gap_ms

    # after all popups shown and destroyed, quit the tk mainloop
    root.after(total_delay + 200, root.quit)

    # run the tk event loop (blocks until root.quit called)
    root.mainloop()
    try:
        root.destroy()
    except:
        pass

def run_popups_in_thread():
    """
    Runs the popup sequence in a separate thread to avoid freezing the main program's terminal
    while the popups show. The function show_fake_hack_popups itself uses tkinter mainloop,
    so run it in a dedicated thread.
    """
    messages = [
        "ALERT: Unauthorized kernel modification detected.",
        "Attempting to remove C:\\Windows\\System32\\kernel32.dll ...",
        "Maniwala bading ...",
        "Attempting to erase registry hives ...",
        "FINAL STEP: Wiping system partitions ..."
    ]
    show_fake_hack_popups(messages, show_time_ms=1200, gap_ms=400)

# ---------- Fractional progress bar characters ----------
blocks = ["", "▏", "▎", "▍", "▌", "▋", "▊", "▉", "█"]
width = 20
total_steps = width * (len(blocks) - 1)

# ---------- Game loop ----------
print("Guess the number between 1 and 10. Type '0' to quit early.\n")

while True:
    try:
        number = int(input("Your guess: ").strip())
    except ValueError:
        print("Please enter a valid integer.")
        continue

    if number == 0:
        print("You quit the game. Bye!")
        break

    attempts += 1

    if number == target:
        print(f"Congratulations! You got it right after {attempts} attempt(s). 🎉")
        break
    elif number < 1 or number > 10:
        print("You can choose a number between 1 and 10 only. Try again.")
        continue
    else:
        print(number," is wrong.")
        time.sleep(2)
        # wrong guess: show three-dot intro, fake attempt logs, fractional bar, then popups
        try:
            # three-dot animation
            msg = "removing your system"
            for _ in range(2):
                for dots in ["", ".", "..", "..."]:
                    sys.stdout.write("\r" + msg + dots + "   ")
                    sys.stdout.flush()
                    time.sleep(0.45)
            print("\n")

            # printed fake attempts
            attempts_msgs = [
                "Attempt 1: Overwriting C:\\Windows\\System32\\kernel32.dll ... failed (permission denied)",
                "Attempt 2: Removing bootloader entries ... failed (access denied)",
                "Attempt 3: Purging registry hives ... failed (insufficient privileges)",
                "Attempt 4: Erasing system drivers ... failed (operation aborted)",
                "Attempt 5: Finalizing wipe ... failed (locked by OS)"
            ]
            for line in attempts_msgs:
                print(line)
                time.sleep(0.6)

            print("\nExecuting final step...")
            time.sleep(0.8)

            # fractional progress bar animation
            for step in range(total_steps + 1):
                full_blocks = step // (len(blocks) - 1)
                frac_index = step % (len(blocks) - 1)
                frac_char = blocks[frac_index] if frac_index > 0 else ""
                remaining = width - full_blocks - (1 if frac_index > 0 else 0)
                bar = "[" + "█" * full_blocks + frac_char + " " * remaining + "]"
                pct = int(step / total_steps * 100)
                sys.stdout.write(f"\r{bar} {pct:3d}%")
                sys.stdout.flush()
                time.sleep(0.03)
            print("\n")

            # Instead of clearing the terminal/sleeping, launch fake popup alerts.
            # Run the popup sequence in a background thread so the terminal remains responsive.
            t = threading.Thread(target=run_popups_in_thread, daemon=True)
            t.start()

            # Optionally wait for the popups to finish before revealing (approximate time):
            # total popup duration = num_messages * (show_time_ms + gap_ms)
            num_msgs = 5
            show_time_ms = 1200
            gap_ms = 400
            approx_seconds = (num_msgs * (show_time_ms + gap_ms)) / 1000.0 + 0.4
            time.sleep(approx_seconds)

        except KeyboardInterrupt:
            print("\nPrank cancelled by user.")
        finally:
            # final reveal after popups
            print("ABORTED: Permission denied.\n Eme mama mo")

# optional reveal after quitting or finishing
print(f"(Debug) The correct number was: {target}")
