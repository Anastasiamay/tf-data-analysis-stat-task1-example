import pandas as pd
import numpy as np


chat_id = 1067114867 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    t = 82
    n = len(x)
    lmbd = x.sum() / (t*n)
    return lmbd
