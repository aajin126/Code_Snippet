while True:
    n = int(input())
    if n == -1:
        break
    else:
        list_num = []
        for i in range(1, n):
            if n % i == 0:
                list_num.append(i)
        if sum(list_num) == n:
            new_list = []
            for j in list_num:
                new_list.append(str(j))
            num_str = ' + '.join(new_list)
            print('{} = {}'.format(n, num_str))
        else:
            print('{} is NOT perfect.'.format(n))