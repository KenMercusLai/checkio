__author__ = 'KenMercusLai'
import math

def fit(X, Y):

    """
    linear regression
    :param X:
    :param Y:
    :return: regression function
    """

    def mean(Xs):
        return sum(Xs) / len(Xs)
    m_x = mean(X)
    m_y = mean(Y)

    def std(Xs, m):
        normalizer = len(Xs) - 1
        return math.sqrt(sum((pow(x - m, 2) for x in Xs)) / normalizer)
    # assert np.round(Series(X).std(), 6) == np.round(std(X, m_x), 6)

    def pearson_r(Xs, Ys):

        sum_xy = 0
        sum_sq_v_x = 0
        sum_sq_v_y = 0

        for (x, y) in zip(Xs, Ys):
            var_x = x - m_x
            var_y = y - m_y
            sum_xy += var_x * var_y
            sum_sq_v_x += pow(var_x, 2)
            sum_sq_v_y += pow(var_y, 2)
        return sum_xy / math.sqrt(sum_sq_v_x * sum_sq_v_y)


    r = pearson_r(X, Y)

    b = r * (std(Y, m_y) / std(X, m_x))
    a = m_y - b * m_x

    def line(x):
        return b * x + a
    return line


def predict_ghost(values):
    return fit(range(len(values)), values)(10)

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    from random import choice, random
    TESTS_QUANTITY = 30
    SCORE_DIST = 0.1

    def generate_formula(prob_x=0.5, prob_bracket=0.2, prob_trig=0.25):
        formula = "x"
        for _ in range(15):
            operation = choice(["+", "-", "*", "/"])
            formula += operation
            if random() < prob_x:
                formula += "x"
            else:
                formula += str(round(random() * 10, 3))
            if random() < prob_bracket:
                formula = "(" + formula + ")"
            if random() < prob_trig:
                formula = "math." + choice(["sin", "cos"]) + "(" + formula + ")"
        return formula

    def calculate_score(f):
        score = 0
        for count in range(TESTS_QUANTITY):
            formula_x = generate_formula()
            values = []
            for x in range(1, 12):
                try:
                    i = round(eval(formula_x), 3)
                    values.append(i)
                except OverflowError:
                    count -= 1
                    break
            else:
                if abs(max(values) - min(values)) < 1:
                    count -= 1
                else:
                    score_distance = (max(values) - min(values)) * SCORE_DIST
                    user_result = f(values[:-1])
                    distance = abs(user_result - values[-1])
                    if distance < score_distance:
                        score += round(100 * ((score_distance - distance) / score_distance))
        print("Total score: {}".format(score))
        return score

    calculate_score(predict_ghost)

