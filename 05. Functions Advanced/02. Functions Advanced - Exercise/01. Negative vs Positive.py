def neg_pos(args):
    positives = sum(int(x) for x in args if int(x) > 0)
    negatives = sum(int(x) for x in args if int(x) < 0)
    print(negatives)
    print(positives)
    print(f"The negatives are stronger than the positives") if abs(negatives) > positives else \
        print(f"The positives are stronger than the negatives")


neg_pos(input().split())

