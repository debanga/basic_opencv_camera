""" Capture Using a Single Camera """

# Import packages
import os
import cv2
import traceback
import matplotlib.pyplot as plt
import time
import camera_utils


if __name__ == '__main__':
    save_path = 'results/camera0'
    camera0 = None

    try:
        # Create capture object
        camera0 = cv2.VideoCapture(0)

        # Set properties    
        ret, camera0 = camera_utils.set_framesize(camera0, 3264, 2448)
        print(f"Framesize set: {ret}")
        ret, camera0 = camera_utils.set_fps(camera0, 30)
        print(f"FPS set: {ret}")
        ret, camera0 = camera_utils.set_exposure(camera0, -1)
        print(f"Exposure set: {ret}")
        ret, camera0 = camera_utils.set_rawcapture(camera0, True)
        print(f"Raw capture set: {ret}")
        
        # Print camera parameter values
        camera_utils.print_params(camera0)

        # Create result directory
        os.makedirs(save_path, exist_ok=True)
        
        i = 0
        while i < 2:    
            return_value, image0 = camera0.read()

            #image0_rgb = cv2.cvtColor(image0, cv2.COLOR_BGR2RGB)
            cv2.imwrite(os.path.join(save_path, str(i) + '_raw.png'), image0)
            
            i += 1

    except Exception:
        print('Something went wrong with image capture')
        print(traceback.print_exc())
    finally:
        if camera0 is not None:
            del camera0
        