def convert_bin(ip):
    # convert ip to 32bits bin
    ret = ''
    for i in ip.split('.'):
        ret += '{:>08}'.format(bin(int(i))[2:])
    return ret


def convert_dec(ip):
    return '.'.join([str(int(ip[i:i + 8], 2)) for i in range(0, 32, 8)])


def checkio(data):
    bin_data = []
    for i in data:
        bin_data.append(convert_bin(i))

    # find the longest match for all bin string
    mask_length = 0
    while mask_length <= 32:
        if len(set([i[mask_length] for i in bin_data])) == 1:
            mask_length += 1
        else:
            break

    # 'cut off' the unmasked part
    summaried_bin = bin_data[0][:mask_length] + '0' * (32 - mask_length)
    return convert_dec(summaried_bin) + '/' + str(mask_length)


# These "asserts" using only for self-checking and not necessary for
# auto-testing
if __name__ == '__main__':  # pragma: no cover
    assert (checkio(["172.16.12.0", "172.16.13.0", "172.16.14.0",
                     "172.16.15.0"]) == "172.16.12.0/22"), "First Test"
    assert (checkio(["172.16.12.0", "172.16.13.0", "172.155.43.9"])
            == "172.0.0.0/8"), "Second Test"
    assert (checkio(["172.16.12.0", "172.16.13.0", "172.155.43.9",
                     "146.11.2.2"]) == "128.0.0.0/2"), "Third Test"
