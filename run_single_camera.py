""" Capture Using a Single Camera """

# Import packages
import os
import cv2
import traceback
import matplotlib.pyplot as plt


if __name__ == '__main__':
    save_path = 'camera0'
    camera0 = None

    try:
        camera0 = cv2.VideoCapture(0)
        camera0.set(cv2.CAP_PROP_FRAME_WIDTH, 3840)
        camera0.set(cv2.CAP_PROP_FRAME_HEIGHT, 2160)
        os.makedirs(save_path, exist_ok=True)
        i = 0
        while True:
            return_value, image0 = camera0.read()
            image0_rgb = cv2.cvtColor(image0, cv2.COLOR_BGR2RGB)
            plt.imshow(image0_rgb)
            plt.show()
            cv2.imwrite(os.path.join(save_path, str(i) + '.png'), image0)
            i += 1
    except Exception:
        print('Something went wrong with image capture')
        print(traceback.print_exc())
    finally:
        if camera0 is not None:
            del camera0