import config as cfg
import matplotlib.pyplot as plt


def runge_cutta_4(u1, u2):
    h = cfg.h
    x = cfg.x
    for i in x:
        phi0 = cfg.f2(i, u1[-1], u2[-1])
        psi0 = cfg.f1(u2[-1])

        phi1 = cfg.f2(i + h / 2, u1[-1] + psi0 * h / 2, u2[-1] + phi0 * h / 2)
        psi1 = cfg.f1(u2[-1] + phi0 * h / 2)

        phi2 = cfg.f2(i + h / 2, u1[-1] + psi1 * h / 2, u2[-1] + phi1 * h / 2)
        psi2 = cfg.f1(u2[-1] + phi1 * h / 2)

        phi3 = cfg.f2(i + h, u1[-1] + psi2 * h, u2[-1] + phi2 * h)
        psi3 = cfg.f1(u2[-1] + phi2 * h)

        u1.append(u1[-1] + h / 6 * (psi0 + 2 * psi1 + 2 * psi2 + psi3))
        u2.append(u2[-1] + h / 6 * (phi0 + 2 * phi1 + 2 * phi2 + phi3))


def main():
    h = cfg.h
    x = cfg.x
    a = cfg.a
    b = cfg.b
    u1 = [cfg.u_a]
    u2 = [cfg.du_a]
    print(u2)
    runge_cutta_4(u1, u2)
    for i in range(len(u1)):
        print([i], u1[i], u2[i])


if __name__ == '__main__':
    main()
