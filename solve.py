import numpy as np
import config as cfg
from math import exp


def u_next(x, u_1=cfg.u_a, u_2=cfg.du_a):
    psi_0 = cfg.f1(u_2)
    fi_0 = cfg.f2(x, u_1, u_2)

    psi_1 = cfg.f1(u_2 + cfg.h * fi_0)
    fi_1 = cfg.f2(x + cfg.h, u_1 + cfg.h * psi_0, u_2 + cfg.h * fi_0)

    return {'x': x,
            'u_1': (u_1 + cfg.h * (psi_0 + psi_1) / 2),
            'u_2': (u_2 + cfg.h * (fi_0 + fi_1) / 2)
            }

def calc(): # 2-go poryadka
    X = np.linspace(cfg.a, cfg.b, int((cfg.b - cfg.a )/ cfg.h), endpoint=False)
    res = [{
        'x': 'START',
        'u_1': -exp(1),#cfg.u_a,
        'u_2': 2 * exp(1)#cfg.du_a
    }]
    y = []
    for x in X:
        u = u_next(x, res[-1]['u_1'], res[-1]['u_2'])
        res.append(u)
        y.append(u['u_1'])
    print(res)
    return y