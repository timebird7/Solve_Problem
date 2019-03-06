TC = int(input())

for tc in range(TC):
    word = list(input())
    n = len(word)

    print('..#.'*n,end='.')
    print()
    print('.#'*(2*n),end='.')
    print()    
    for s in word:
        print(f'#.{s}.',end='')
    print('#')
    print('.#' * (2 * n), end='.')
    print()
    print('..#.' * n, end='.')
    print()