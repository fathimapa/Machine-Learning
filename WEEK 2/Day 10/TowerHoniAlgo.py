def hanoi_solver(n):
    rods = [
        list(range(n, 0, -1)),  # source rod
        [],                     # auxiliary rod
        []                      # target rod
    ]

    moves = []

    def record_state():
        moves.append(f"{rods[0]} {rods[1]} {rods[2]}")

    def move_disks(num, source, auxiliary, target):
        if num == 1:
            disk = rods[source].pop()
            rods[target].append(disk)
            record_state()
        else:
            move_disks(num - 1, source, target, auxiliary)
            move_disks(1, source, auxiliary, target)
            move_disks(num - 1, auxiliary, source, target)

    # record initial state
    record_state()
    move_disks(n, 0, 1, 2)

    return "\n".join(moves)
