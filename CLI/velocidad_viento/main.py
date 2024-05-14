"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import pandas as pd
from prototools import progressbar, text_align

from utils import get_data, set_params, get_sheetname

URL = "https://www.datos.gov.co/resource/sgfv-3yp8.json?{}"
PARAMS = "$where=fechaobservacion between '{}' and '{}'"


def main():
    text_align("Start")
    for y in range(2008, 2020):
        with pd.ExcelWriter(f"{y}.xlsx") as w:
            for m in progressbar(range(1, 13)):
                data = get_data(URL, set_params(PARAMS, y, m))
                df = pd.DataFrame(data)
                df.to_excel(w, sheet_name=get_sheetname())
        text_align(f"{y} files done!")
    text_align("Finish")


if __name__ == "__main__":
    main()
