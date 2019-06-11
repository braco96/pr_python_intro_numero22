# -*- coding: utf-8 -*-
import re
def normalizar_espacios(s):
    return re.sub(r"\s+", " ", (s or "")).strip()

