class ControlGame:

	import pyautogui,time

	pyautogui.keyDown('alt')
	time.sleep(.2)
	pyautogui.press('tab')
	time.sleep(.2)
	pyautogui.keyUp('alt')
	time.sleep(.2)
	pyautogui.press('esc')
	time.sleep(.2)
	pyautogui.press('F11')
	time.sleep(.2)
	pyautogui.press('r')