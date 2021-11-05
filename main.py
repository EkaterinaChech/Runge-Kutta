import config as c
import matplotlib.pyplot as plt
import numpy as np

a = c.a
b = c.b
h = c.h
x = np.arange(a, b, h)


def main():
    u = []
    u1 = [c.u(a)]
    u2 = [c.du(a)]
    for x_i in x:
        phi_0 = c.f2(x_i, u1[-1], u2[-1])
        psi_0 = c.f1(u2[-1])

        phi_1 = c.f2(x_i + h / 2, u1[-1] + h * psi_0 / 2, u2[-1] + h * phi_0 / 2)
        psi_1 = c.f1(u2[-1] + h * phi_0 / 2)

        phi_2 = c.f2(x_i + h / 2, u1[-1] + h * psi_1 / 2, u2[-1] + h * phi_1 / 2)
        psi_2 = c.f1(u2[-1] + h / 2)

        phi_3 = c.f2(x_i + h, u1[-1] + h * psi_2, u2[-1] + h * phi_2);
        psi_3 = c.f1(u2[-1] + h)

        u1.append(u1[-1] + h / 6 * (psi_0 + 2 * psi_1 + 2 * psi_2 + psi_3))
        u2.append(u2[-1] + h / 6 * (phi_0 + 2 * phi_1 + 2 * phi_2 + phi_3))

    plt.style.use('fast')
    fig, ax = plt.subplots(figsize=(16, 9))
    line = ax.plot(x, u1[:-1], linewidth=5, color='black')
    plt.show()

    for i in range(len(u1)):
        print([i], u1[i], u2[i])


if __name__ == '__main__':
    main()
