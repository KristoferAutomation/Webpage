#!/usr/bin/env python3
from streamlit.web import cli as stcli
import sys
import MyGlobals


if __name__ == "__main__":
  script_path = MyGlobals.THIS_PATH + "/app.py"
  sys.argv = ["streamlit", "run", script_path]
  stcli.main()