def func(limit: int) -> None:
    digits = []
    answers = []
    n = 1
    while n < limit:
        digits = [int(i) for i in str(n)]
        for i in digits:
            if all((i % 2) == 0 for i in digits):
                answers.append(n)
        n = n + 1
        digits = []
    true_answers = list(set(answers))
    print(true_answers)
      
