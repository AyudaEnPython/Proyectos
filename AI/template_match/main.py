import cv2 as cv # type: ignore
import numpy as np
from numpy import ndarray

ORIGINAL_PATH = "website.png"
TEMPLATE_PATH = "template.png"

METHOD = cv.TM_CCOEFF_NORMED
COLORS = {
    "red": (0, 0, 255),
    "green": (0, 255, 0),
    "blue": (255, 0, 0),
    "yellow": (0, 255, 255),
    "magenta": (255, 0, 255),
    "cyan": (255, 255, 0),
    "white": (255, 255, 255),
    "black": (0, 0, 0)
}


def show_image(img: ndarray, msg="Found!") -> None:
    cv.imshow(msg, img)
    cv.waitKey(0)


def find_template(
    img_rgb: ndarray,
    img_gray: ndarray,
    template: ndarray,
    threshold: float = 0.8,
    method: int = METHOD,
    color: str = "green",
) -> ndarray:
    w, h = template.shape[::-1]
    res = cv.matchTemplate(img_gray, template, method)
    pos = np.where(res >= threshold)
    for pt in zip(*pos[::-1]):
        cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), COLORS[color], 2)
    return img_rgb


def main():
    img_rgb = cv.imread(ORIGINAL_PATH)
    img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
    template = cv.imread(TEMPLATE_PATH, 0)
    img = find_template(img_rgb, img_gray, template)
    show_image(img)
    cv.imwrite("res.png", img)


if __name__ == "__main__":
    main()