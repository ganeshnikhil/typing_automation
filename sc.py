import mss
import time 
import keyboard 
import pytesseract
from PIL import Image


def write_using_keyboard(text):
  
  for char in text.strip():
    keyboard.press(char)
    keyboard.release(char)
    time.sleep(0.06)

def extract_text_from_image(filepath):
  # Read the image
  img = Image.open(filepath)
  # Convert the image to grayscale
  gray = img.convert('L')
  # Apply thresholding to the image
  thresh = gray.point(lambda x: 255 if x > 127 else 0)
  # Recognize the text in the image
  text = pytesseract.image_to_string(thresh)
  # Print the text
  return text



def take_screenshot(width, height):
  with mss.mss() as sct:
    # The screen part to capture
      monitor = {"top": 320, "left": 250, "width": width, "height": height}
      output = "sct-{top}x{left}_{width}x{height}.png".format(**monitor)
      #time.sleep(5)
    # Grab the data
      sct_img = sct.grab(monitor)

    # Save to the picture file
      mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
  return output
# Specify the desired width and height
def main():
  desired_width =1000
  desired_height = 180
  print("Press Enter to take a screenshot. Press 'q' to exit.")
  while True:
      if keyboard.is_pressed('esc'):
          image_name=take_screenshot(desired_width,desired_height)
          text=extract_text_from_image(image_name)
          if text== None or len(text)<10:
            pass
          else:
            write_using_keyboard(text)
            #print(text)
      elif keyboard.is_pressed('q'):
          print("Exiting...")
          break
if __name__ == "__main__":
  main()
#desired_width =1000
#desired_height = 180

# Take the screenshot
#take_screenshot(desired_width, desired_height)
