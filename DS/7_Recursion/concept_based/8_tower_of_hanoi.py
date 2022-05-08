# https://www.youtube.com/watch?v=usOtwunz0oM


def tower_of_hanoi(n, src, util, dest):

    # if we have only one disk then simply put to destination
    if n == 1:
        print(f"Move {n} from {src} to {dest}")
        return

    # this call will make the input smaller/
    # it will put all the n-1 disk to util in proper order
    # here we just put disk from src to  util using destination
    tower_of_hanoi(n - 1, src, dest, util)

    print(f"Move {n} from {src} to {dest}")

    # this call will put all the disk to proper told place
    # from util we have put the disk to destination using src as helper pole
    tower_of_hanoi(n - 1, util, src, dest)


tower_of_hanoi(2, "src", "util", "dest")
