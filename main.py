import pyautogui
import time

time.sleep(5)

mode = 2
anchorX = -7500
anchorZ = -10500

x = 15500
z = 12500

if mode == 1:

    endX = anchorX * -1 + x
    endZ = anchorZ * -1 + z

    step = 200
    delay = 2

    toggle = True

    total_points = 0
    current_point = 0

    for z_offset in range(0, endZ + step, step):
        if toggle:
            x_range = range(0, endX + step, step)
        else:
            x_range = range(endX, -step, -step)
        for x_offset in x_range:
            total_points += 1


    for z_offset in range(0, endZ + step, step):
        if toggle:
            x_range = range(0, endX + step, step)
            yaw = 90
        else:
            x_range = range(endX, -step, -step)
            yaw = -90

        for x_offset in x_range:
            targetX = anchorX + x_offset
            targetZ = anchorZ + z_offset

            pyautogui.press("t")
            pyautogui.typewrite(f"/tp KompetenzL0s {targetX} 120 {targetZ} {yaw} 0")
            pyautogui.press("enter")

            current_point += 1
            progress = (current_point / total_points) * 100

            print(f"[{current_point}/{total_points}] "
                  f"Teleport zu ({targetX}, {targetZ}) "
                  f"– {progress:.1f}% – Warte {delay}s")

            time.sleep(delay)

        toggle = not toggle
else:
    step = 500
    delay = 40

    total_points = 0
    current_point = 0

    for x_offset in range(anchorX, x + 1, step):
        total_points += 1

    for z_offset in range(anchorZ + step, z + 1, step):
        total_points += 1

    for x_offset in range(x - step, anchorX - 1, -step):
        total_points += 1

    for z_offset in range(z - step, anchorZ, -step):
        total_points += 1

    for x_offset in range(anchorX, x + 1, step):
        pyautogui.press("t")
        pyautogui.typewrite(f"/tp KompetenzL0s {x_offset} 120 {anchorZ}")
        pyautogui.press("enter")

        current_point += 1
        progress = (current_point / total_points) * 100

        print(f"[{current_point}/{total_points}] "
              f"Obere Kante: Teleport zu ({x_offset}, {anchorZ}) "
              f"– {progress:.1f}% – Warte {delay}s")

        time.sleep(delay)

    for z_offset in range(anchorZ + step, z + 1, step):
        pyautogui.press("t")
        pyautogui.typewrite(f"/tp KompetenzL0s {x} 120 {z_offset}")
        pyautogui.press("enter")

        current_point += 1
        progress = (current_point / total_points) * 100

        print(f"[{current_point}/{total_points}] "
              f"Rechte Kante: Teleport zu ({x}, {z_offset}) "
              f"– {progress:.1f}% – Warte {delay}s")

        time.sleep(delay)

    for x_offset in range(x - step, anchorX - 1, -step):
        pyautogui.press("t")
        pyautogui.typewrite(f"/tp KompetenzL0s {x_offset} 120 {z}")
        pyautogui.press("enter")

        current_point += 1
        progress = (current_point / total_points) * 100

        print(f"[{current_point}/{total_points}] "
              f"Untere Kante: Teleport zu ({x_offset}, {z}) "
              f"– {progress:.1f}% – Warte {delay}s")

        time.sleep(delay)

    for z_offset in range(z - step, anchorZ, -step):
        pyautogui.press("t")
        pyautogui.typewrite(f"/tp KompetenzL0s {anchorX} 120 {z_offset}")
        pyautogui.press("enter")

        current_point += 1
        progress = (current_point / total_points) * 100

        print(f"[{current_point}/{total_points}] "
              f"Linke Kante: Teleport zu ({anchorX}, {z_offset}) "
              f"– {progress:.1f}% – Warte {delay}s")

        time.sleep(delay)