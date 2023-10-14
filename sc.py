import mss
import time 
import keyboard 
import pytesseract
from PIL import Image

# write text using key press on screen
def write_using_keyboard(text:str) -> None:
  for char in text.strip():
    keyboard.press(char)
    keyboard.release(char)
    time.sleep(0.06)

# Extract text from the image 
def extract_text_from_image(filepath:str) -> str:
  # Read the image
  img = Image.open(filepath)
  # Convert the image to grayscale
  gray = img.convert('L')
  # Apply thresholding to the image
  thresh = gray.point(lambda x: 255 if x > 127 else 0)
  # Recognize the text in the image
  text = pytesseract.image_to_string(thresh)
  
  return text


# capture the image of text on screen , pass the precise parameters for result
def take_screenshot(width:int , height:int  , top:int  , left:int) -> str:
  with mss.mss() as sct:
    # The screen part to capture
      monitor = {"top": top , "left": left , "width": width, "height": height}
      output = f"sct-{top}x{left}_{width}x{height}.png"
    # Grab the data
      sct_img = sct.grab(monitor)

    # Save to the picture file
      mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
  return output


def main():
  # adjust the desired width and height 
  desired_width =1000
  desired_height = 180
  top = 320
  left = 250
  
  print("Press Enter to take a screenshot. Press 'q' to exit.")
  while True:
    # esc take screenshot of screen 
      if keyboard.is_pressed('esc'):
          image_name=take_screenshot(desired_width , desired_height , top , left)
          text=extract_text_from_image(image_name)
          if text== None or len(text)<10:
            pass
          else:
            write_using_keyboard(text)
            #print(text)
     # q quit the program 
      elif keyboard.is_pressed('q'):
          print("Exiting...")
          break
if __name__ == "__main__":
  main()
#desired_width =1000
#desired_height = 180

# Take the screenshot
#take_screenshot(desired_width, desired_height)
