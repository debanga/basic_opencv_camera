""" Camera controls """
"""
# Ref: https://docs.opencv.org/3.4/d4/d15/group__videoio__flags__base.html

Camera properties to control: (@doing[debanga] which properties are supported by our camera?)
    - Exposure
    - Gain
    - FrameSize
    - Brightness
    - Contrast
    - Gamma
    - AutoExposure
    - AutoWhiteBalance
    - WhiteBalanceColorTemperature
    - FPS
"""


import cv2


def print_params(camera):
    """
    Print current parameter values
    """
    width = camera.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = camera.get(cv2.CAP_PROP_FRAME_HEIGHT)
    exposure = camera.get(cv2.CAP_PROP_EXPOSURE)
    auto_exposure = camera.get(cv2.CAP_PROP_AUTO_EXPOSURE)
    brightness = camera.get(cv2.CAP_PROP_BRIGHTNESS)
    contrast = camera.get(cv2.CAP_PROP_CONTRAST)
    gain = camera.get(cv2.CAP_PROP_GAIN)
    saturation = camera.get(cv2.CAP_PROP_SATURATION)
    fps = camera.get(cv2.CAP_PROP_FPS)
    auto_wb = camera.get(cv2.CAP_PROP_AUTO_WB)
    
    print("Current values of the camera parameters:")
    print(f"Image shape: ({width}, {height})")
    print(f"Exposure: {exposure}")
    print(f"Auto exposure: {auto_exposure}")
    print(f"Brightness: {brightness}")
    print(f"Contrast: {contrast}")
    print(f"Gain: {gain}")
    print(f"Saturation: {saturation}")
    print(f"FPS: {fps}")
    print(f"Auto White Balance: {auto_wb}")


def set_framesize(camera, width=1920, height=1080):
    """
    Set capture frame size
    """
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    return camera


def set_fps(camera, fps):
    """
    Set capture fps (frame per second)
    """
    camera.set(cv2.CAP_PROP_FPS, fps)
    return camera

